import pandas as pd

data=pd.read_csv('category.csv')
df1=data['Interested_Group']

from sklearn.feature_extraction.text import TfidVectorizer
from sklearn.pipeline import make_pipeline

from sklearn.naive_bayes import MultinomialNB
model=make_pipeline(TfidVectorizer(),MultinomialNB())
model.fit(df1)
model.save('model.h5')