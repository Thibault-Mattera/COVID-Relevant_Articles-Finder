# -*- coding: utf-8 -*-
"""
Modelling

"""

########################################### DEPENDENCIES ############################################

# load cleaned dataset
import pandas as pd


import nltk
nltk.download('stopwords') # run this one time
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
stop_words.append('the')

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.model_selection import GridSearchCV
from sklearn.manifold import TSNE
import pickle
import seaborn as sns
import matplotlib.pyplot as plt

########################################### FUNCTIONS ###############################################

# analyse topics from LDA model
def print_topics(model, count_vectorizer, n_top_words):
    words = tf_vectorizer.get_feature_names()
    for topic_idx, topic in enumerate(model.components_):
      
        print("\nTopic #%d:" % topic_idx )
        print(" ".join([words[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))


def tsne_visualization(lda_matrix):
    model = TSNE(n_components=2, perplexity=30, learning_rate=100, 
                        n_iter=5000, verbose=1, random_state=0, angle=0.75)
    tsne_features = model.fit_transform(lda_matrix)
    df_1 = pd.DataFrame(tsne_features)
    df_1['topic'] = lda_matrix.argmax(axis=1)
    df_1.columns = ['TSNE1', 'TSNE2', 'topic']
    plt.figure(figsize=(15, 10))
    plt.title('T-SNE plot of different headlines ( headlines are clustered among their topics)')
    ax = sns.scatterplot(x = 'TSNE1', y = 'TSNE2', hue = 'topic', data = df_1, legend = 'full')
    plt.show()

########################################### EXECUTION ###############################################

df=pd.read_csv('cleaned_data.csv')

# vectorize articles' abstracts

min_word_frequency=10
count_vectorizer = CountVectorizer(min_df=min_word_frequency,stop_words=stop_words)

tf_vectorizer = TfidfVectorizer(stop_words=stop_words, max_features=1000)
news_matrix = tf_vectorizer.fit_transform(df.abstract)

#best results with Count vectorizer
pickle.dump(count_vectorizer, open("count_vectorizer.pkl", "wb"))

# Initate LDA model
lda = LatentDirichletAllocation(max_iter=100)

# Launch Grid Search to find optimal model parameters
search_params = {'n_components': [5, 6, 7, 8 , 9, 10], 'learning_decay': [.5, .7, .9]}
model = GridSearchCV(lda, param_grid=search_params, verbose=10)
model.fit(news_matrix)
best_lda_model = model.best_estimator_
print("Best Model's Params: ", model.best_params_)
print("Best Log Likelihood Score: ", model.best_score_)
print("Model Perplexity: ", best_lda_model.perplexity(news_matrix))

# save best model from Grid Search
filename = 'best_model.pkl'
pickle.dump(best_lda_model,open(filename,'wb'))

# Print the topics found by the LDA model
print("Topics found via LDA:")
print_topics(best_lda_model, news_matrix, 10)

# Visualize topics
with open('best_model.pkl', 'rb') as pickle_file:
    best_lda_model = pickle.load(pickle_file)
    lda_matrix = best_lda_model.transform(news_matrix)

tsne_visualization(lda_matrix)