# -*- coding: utf-8 -*-
"""
Data Cleaning

"""

########################################### DEPENDENCIES ############################################

import pandas as pd
pd.set_option("display.max_colwidth", 200)
import numpy as np # linear algebra 
import seaborn as sns

#pip install -U langdetect
from langdetect import detect
from tqdm import tqdm

import nltk
from nltk import FreqDist
nltk.download('stopwords') # run this one time
import re
import matplotlib.pyplot as plt

from nltk.corpus import stopwords


########################################### FUNCTIONS ###############################################

def replace_missing(d):
    if d.startswith('http://'):
        return d
    elif d.startswith('doi.org'):
        return f'http://{d}'
    else:
        return f'http://doi.org/{d}'

def freq_words(x, terms = 30):
         all_words = ' '.join([text for text in x])
         all_words = all_words.split()
         fdist = FreqDist(all_words)
         words_df = pd.DataFrame({'word':list(fdist.keys()), 'count':list(fdist.values())})

  # selecting top 20 most frequent words
         d = words_df.nlargest(columns="count", n = terms) 
         plt.figure(figsize=(20,5))
         ax = sns.barplot(data=d, x= "word", y = "count")
         ax.set(ylabel = 'Count')
         plt.show()

def remove_stopwords(rev):
    stop_words = stopwords.words('english')
    stop_words.append('the')
    rev_new = " ".join([i for i in rev if i not in stop_words])
    return rev_new

########################################### EXECUTION ###############################################

df=pd.read_csv('metadata.csv')
df=df.drop(['sha','source_x','pmcid','pubmed_id','license','publish_time','authors','journal'],axis=1)
df.shape
df=df.dropna(subset=['abstract'])#remove missing values on abstract typically

df.doi = df.doi.fillna('').apply(replace_missing)

# remove articles with empty abstract
df=df[df['abstract']!='http://virus.zoo.ox.ac.uk/rnavirusdb; http://hivweb.sanbi.ac.za/rnavirusdb; http://bioinf.cs.auckland.ac.nz/rnavirusdb; http://tree.bio.ed.ac.uk/rnavirusdb.']

tqdm.pandas()
abstracts=df['abstract'].tolist()

# create a new column language
df['language']=df['abstract'].progress_apply(lambda x: detect(x))
df['language'].value_counts()

# select only the articles written in English
df=df[df['language']=='en']

# save cleaned dataset in a csv file:
df.to_csv('cleaned_data.csv', index=False)

# remove unwanted characters, numbers and symbols
df['abstract'] = df['abstract'].str.replace("[^a-zA-Z#]", " ")

# remove short words (length < 3)
df['abstract'] = df['abstract'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>2]))
df.drop_duplicates(subset='abstract',inplace=True)
df.to_csv('cleaned_data.csv', index=False)

## EDA ## Word Frequency Distribution 
reviews = [remove_stopwords(r.split()) for r in df['abstract']]
reviews = [r.lower() for r in reviews]
freq_words(reviews, 15)