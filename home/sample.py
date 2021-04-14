import pandas as pd
import numpy as np
import nltk
import tensorflow_hub as hub
from tensorflow.keras.models import Sequential
import tensorflow as tf
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.models import Model
from keras.models import load_model

print("HEYYY")
embed = hub.load("https://tfhub.dev/google/Wiki-words-250/2")


model = Sequential()
model.add(LSTM(32))
model.add(Dense(2, activation='softmax'))
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.built = True
new_model=load_model('C:/Users/Peterson/Documents/model_opinion.h5')
new_model.summary()
print("hi")
def get_max_length(df):
    """
    get max token counts from train data, 
    so we use this number as fixed length input to RNN cell
    """
    max_length = 0
    
    for row in df['url']:
        if len(row.split("/")) > max_length:
            max_length = len(row.split("/"))
    return max_length

def get_word2vec_enc(reviews):
    """
    get word2vec value for each word in sentence.
    concatenate word in numpy array, so we can use it as RNN input
    """
    encoded_reviews = []
    for review in reviews:
        
        try:
          #print(review)
          tokens = review.split("/")
          print(tokens)
        #for token in tokens:
            #encoded_reviews.append(embed1[token])
          word2vec_embedding = embed(tokens)
        #print(word2vec_embedding)
          encoded_reviews.append(word2vec_embedding)
        except:
          continue
    #print(len(encoded_reviews))
    return encoded_reviews

def get_padded_encoded_reviews(encoded_reviews):
    """
    for short sentences, we prepend zero padding so all input to RNN has same length
    """
    padded_reviews_encoding = []
    count=1
    for enc_review in encoded_reviews:
        print(count)
        count+=1
        zero_padding_cnt = max_length - enc_review.shape[0]
        pad = np.zeros((1, 250))
        for i in range(zero_padding_cnt):
            enc_review = np.concatenate((pad, enc_review), axis=0)
        padded_reviews_encoding.append(enc_review)
    return padded_reviews_encoding

def labels_encode(label):
    """
    return one hot encoding for Y value
    """
    if label == 1:
        return [1,0]
    else:
        return [0,1]
    
def preprocess(df):
    """
    encode text value to numeric value
    """
    # encode words into word2vec
    reviews = df['url'].tolist()
    
    encoded_reviews = get_word2vec_enc(reviews)
    padded_encoded_reviews = get_padded_encoded_reviews(encoded_reviews)
    # encoded labels
    labels = df['is_opinion'].tolist()
    encoded_labels = [labels_encode(label) for label in labels]
    X = np.array(padded_encoded_reviews)
    Y = np.array(encoded_labels)
    return X, Y
def sampletest(urlTest):
    return urlTest+"hello1111"