# read cleaned data set
import pandas as pd
df=pd.read_csv('./cleaned_data.csv')

# load vectorizer model (count vectorizer)
import pickle
with open('count_vectorizer_model.pkl', 'rb') as pickle_file:
    vectorizer = pickle.load(pickle_file)

# define matrix of token counts
news_matrix = vectorizer.fit_transform(df.abstract)

# load LDA model (classify topics)
with open('lda_model.pkl', 'rb') as pickle_file:
    best_lda_model = pickle.load(pickle_file)
    lda_matrix = best_lda_model.transform(news_matrix)
topic_dist = pd.DataFrame(lda_matrix)

# function to get the nearest neighbours from LDA topics
from scipy.spatial.distance import jensenshannon
def get_k_nearest_docs(doc_dist, k=5):

            distances = topic_dist.apply(lambda x: jensenshannon(x, doc_dist), axis=1)
        
            return distances[distances != 0].nsmallest(n=k).index

def find_relevant_articles(tasks, k=5):
    tasks = [tasks] if type(tasks) is str else tasks 
    
    tasks_tf = vectorizer.transform(tasks)
    tasks_topic_dist = pd.DataFrame(best_lda_model.transform(tasks_tf))

    list_articles=[]

    for index, bullet in enumerate(tasks):
        print(bullet)
        recommended = get_k_nearest_docs(tasks_topic_dist.iloc[index], k)
        recommended = df.iloc[recommended]
        for l, n in recommended[['doi','title']].values:
            items = { 
                'title': n,
                'link': l, 
                }
            list_articles.append(items)
    return list_articles