# -*- coding: utf-8 -*-
"""

Model testing

"""

########################################### DEPENDENCIES ############################################

import pandas as pd
import pickle
from scipy.spatial.distance import jensenshannon
from IPython.display import HTML, display

########################################### FUNCTIONS ###############################################

def get_k_nearest_docs(doc_dist, k=5):
    distances = topic_dist.apply(lambda x: jensenshannon(x, doc_dist), axis=1)
   # else:
            #diff_df = topic_dist.sub(doc_dist)
            #distances = np.sqrt(np.square(diff_df).sum(axis=1)) # euclidean distance 
        
    return distances[distances != 0].nsmallest(n=k).index

def relevant_articles(vectorizer, tasks, k=5):
    
    tasks = [tasks] if type(tasks) is str else tasks 
    
    tasks_tf = vectorizer.transform(tasks)
    tasks_topic_dist = pd.DataFrame(best_lda_model.transform(tasks_tf))

    # from vectorized task, retrieve the nearest documents using the Jensen-Shannon distance

    for index, bullet in enumerate(tasks):
        print(bullet)
        recommended = get_k_nearest_docs(tasks_topic_dist.iloc[index], k)
        recommended = df.iloc[recommended]
        
        h = '<br/>'.join(['<a href="' + l + '" target="_blank">'+ n + '</a>' for l, n in recommended[['doi','title']].values])
        display(HTML(h))


########################################### EXECUTION ###############################################


# read cleaned data set
df=pd.read_csv('cleaned_data.csv')

# import vectorizer and define tfidf matrix
with open('count_vectorizer.pkl', 'rb') as pickle_file:
    vectorizer = pickle.load(pickle_file)
news_matrix =  vectorizer.fit_transform(df.abstract)

# import LDA model and generate topics
with open('best_model.pkl', 'rb') as pickle_file:
    best_lda_model = pickle.load(pickle_file)
    lda_matrix = best_lda_model.transform(news_matrix)
topic_dist = pd.DataFrame(lda_matrix)

# define tasks for testing model
task= ['What do we know about COVID-19 risk factors?',   
'What do we know about vaccines and therapeutics?',
'What do we know about Diagnostics and Surveillance?',
'What do we know about Genetic Origin and Evolution?',
'What do we know about Information Sharing?']
relevant_articles(vectorizer, task, 3)
relevant_articles(vectorizer, task, 5)