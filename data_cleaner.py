import sklearn
import pandas as pd
import pymorphy2
import nltk
from nltk.stem import WordNetLemmatizer 

n_data = pd.read_csv('data/data.csv', sep=';', encoding='latin1')

dataset = n_data

dataset.columns = ['text', 'label']

morph = pymorphy2.MorphAnalyzer()

dataset.to_csv('data/cleaned_data.csv')