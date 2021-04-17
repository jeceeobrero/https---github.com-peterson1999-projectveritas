import pandas as pd
import numpy as np
import nltk
import tensorflow_hub as hub
from tensorflow.keras.models import Sequential
import tensorflow as tf
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.models import Model
from keras.models import load_model
from newspaper import Article
import datetime as date
import os
import hashlib

class Credibility():
    def loadCredibility(self,url):
        print("Here 1:load everything")
        #embed = tf.saved_model.load('home\saved_model.pb')
        #os.environ["TFHUB_MODEL_LOAD_FORMAT"] = "UNCOMPRESSED"
        os.environ["TFHUB_CACHE_DIR"] = 'D:/Dev/News Aggregator/tmp/tfhub'
        handle = "https://tfhub.dev/google/Wiki-words-250/2"
        hashlib.sha1(handle.encode("utf8")).hexdigest()
        embed = hub.load("https://tfhub.dev/google/Wiki-words-250/2")
        
        misleading = 'home\model_misleading.h5'
        opinion = 'home\model_opinion.h5'
        sarcasm = 'home\model_sarcasm.h5'


        print("Here 2:parse article and build model")
        article = Article(url)
        article.download() 
        article.parse()
        news_title= article.title
        news_image = article.top_image


        model = Sequential()
        model.add(LSTM(32))
        model.add(Dense(2, activation='softmax'))
        model.compile(loss='categorical_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy'])

        model.built = True

        print("Here 3: load opinion model")
        opinion_prediction = self.opinionScore(self,opinion,url,embed)
        #print('Predicted class: ', prediction)
        #print('Real class:  ', sample_Y)



        print("Here 4:load sarcasm model")
        sarcasm_prediction = self.sarcasmScore(self,sarcasm,embed,news_title)
        #print('Predicted class: ', prediction)
       # print('Real class:  ', sample_Y)



        print("Here 5:load misleading model")
        misleading_prediction = self.misleadingScore(self,misleading,embed,news_title)
        #print('Predicted class: ', misleading_prediction)
        #print('Real class:  ', sample_Y)
        print("Here 6: get relevance score")
        rel_score = self.relevanceScore(article)
        
        return misleading_prediction, opinion_prediction, sarcasm_prediction, rel_score, news_title, news_image

    def opinionScore(self,opinion,url,embed):
        new_model=load_model(opinion)
        new_model.summary()

        article_list = {'corpus': [url],
                'label': [1]
                }
        article_sample = pd.DataFrame(article_list, columns = ['corpus', 'label'])

        article_sample= article_sample[article_sample['corpus'].notnull()]
        max_length = self.get_max_length_url(self,article_sample)
        sample_X, sample_Y = self.preprocess_url(self,article_sample,embed,max_length)
        opinon_prediction = new_model.predict(sample_X)[0][1]

        return opinon_prediction*100

    def sarcasmScore(self,sarcasm,embed,news_title):
        new_model=load_model(sarcasm)
        new_model.summary()

        article_list = {'corpus': [news_title],
                'label': [1]
                }
        article_sample = pd.DataFrame(article_list, columns = ['corpus', 'label'])

        article_sample= article_sample[article_sample['corpus'].notnull()]
        max_length = self.get_max_length_url(self,article_sample)
        sample_X, sample_Y = self.preprocess_url(self,article_sample,embed,max_length)
        sarcasm_prediction = new_model.predict(sample_X)[0][1]

        return sarcasm_prediction*100

    def misleadingScore(self,misleading,embed,news_title):
        new_model=load_model(misleading)
        new_model.summary()
        article_list = {'corpus': [news_title],
                'label': [1]
                }
        article_sample = pd.DataFrame(article_list, columns = ['corpus', 'label'])
        article_sample= article_sample[article_sample['corpus'].notnull()]
        max_length = self.get_max_length(self,article_sample)
        sample_X, sample_Y = self.preprocess(self,article_sample,embed,max_length)
        misleading_prediction = new_model.predict(sample_X)[0][1]

        return misleading_prediction*100

    def relevanceScore(article):
        today = date.datetime.now()
        newsDate = article.publish_date

        if (newsDate!=None):
            rel = today - newsDate 
            d = rel.days 
            score = 100
        #print(days, "day(s)")
        else:
            d=0
            score=50
       
        #score = 100
        multiplier = 1

        if d//7 >= 4:
            multiplier = 2
        elif d > 7:
            multiplier = multiplier + ((d // 7) * 0.5)
        elif d >= 5:
            multiplier = multiplier + 0.35
        elif d >= 3:
            multiplier = multiplier + 0.3
        elif d >= 2:
            multiplier = multiplier + 0.25

        rel_score = score - (d * multiplier)
        if rel_score < 0:
            rel_score = 0

        return rel_score

    def get_max_length_url(self,df):
        """
        get max token counts from train data, 
        so we use this number as fixed length input to RNN cell
        """
        max_length = 0
        
        for row in df['corpus']:
            if len(row.split("/")) > max_length:
                max_length = len(row.split("/"))
        return max_length
    def get_word2vec_enc_url(self,reviews,embed):
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
    def preprocess_url(self,df,embd,maxlength):
        """
        encode text value to numeric value
        """
        # encode words into word2vec
        reviews = df['corpus'].tolist()
        
        encoded_reviews = self.get_word2vec_enc_url(self,reviews,embd)
        padded_encoded_reviews = self.get_padded_encoded_reviews(self,encoded_reviews,maxlength)
        # encoded labels
        labels = df['label'].tolist()
        encoded_labels = [self.labels_encode(self,label) for label in labels]
        X = np.array(padded_encoded_reviews)
        Y = np.array(encoded_labels)
        return X, Y
    

    def get_max_length(self,df):
        """
        get max token counts from train data, 
        so we use this number as fixed length input to RNN cell
        """
        max_length = 0
        
        for row in df['corpus']:
            if len(row.split(" ")) > max_length:
                max_length = len(row.split(" "))
        return max_length

    def get_word2vec_enc(self,reviews,embed):
        """
        get word2vec value for each word in sentence.
        concatenate word in numpy array, so we can use it as RNN input
        """
        encoded_reviews = []
        for review in reviews:
            
            try:
            #print(review)
                tokens = review.split(" ")
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

    def get_padded_encoded_reviews(self,encoded_reviews,max_length):
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

    def labels_encode(self,label):
        """
        return one hot encoding for Y value
        """
        if label == 1:
            return [1,0]
        else:
            return [0,1]
        
    def preprocess(self,df,embd,maxlength):
        """
        encode text value to numeric value
        """
        # encode words into word2vec
        reviews = df['corpus'].tolist()
        
        encoded_reviews = self.get_word2vec_enc(self,reviews,embd)
        padded_encoded_reviews = self.get_padded_encoded_reviews(self,encoded_reviews,maxlength)
        # encoded labels
        labels = df['label'].tolist()
        encoded_labels = [self.labels_encode(self,label) for label in labels]
        X = np.array(padded_encoded_reviews)
        Y = np.array(encoded_labels)
        return X, Y
    def credtest(self,urlTest):
        misleading, opinion,sarcasm,rel_score,news_title,news_image=self.loadCredibility(self,urlTest)
        return misleading, opinion, sarcasm, rel_score,news_title,news_image
