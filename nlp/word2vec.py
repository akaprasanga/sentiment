import os
import pandas as pd
import nltk
import gensim
from gensim.models import Word2Vec
from gensim import corpora, models, similarities

# model = gensim.models.Word2Vec.load_word2vec_format('./model/GoogleNews-vectors-negative300.bin', binary=True)  

df=pd.read_csv('data.csv')


x=df['Tweets'].values.tolist()


corpus = x
  
tok_corp= [nltk.word_tokenize(sent) for sent in corpus]
       
           
model = gensim.models.Word2Vec(tok_corp, window=2, min_count=1, size = 300)

print(model)
# model.wv.save_word2vec_format('text.bin', binary=True)
# model = gensim.models.Word2Vec.load('test_model')
similar = model.most_similar('Cryptocurrency')
print(similar)
# dad = model['jgjdstyfgiuojhnbgvff']
# mom = model['mom']
# print((dad))
# print(dad.shape)
# print(dad[:10])
#model.most_similar([vector])