import pandas as pd
import numpy as np
import nltk
import tensorflow_hub as hub
from tensorflow.keras.models import Sequential
import tensorflow as tf
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.models import Model
from keras.models import load_model


class Sample():
    def loadSample(self,url):
        print("HEYYY")
        embed = hub.load("https://tfhub.dev/google/Wiki-words-250/2")


        model = Sequential()
        model.add(LSTM(32))
        model.add(Dense(2, activation='softmax'))
        model.compile(loss='categorical_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy'])

        model.built = True
        new_model=load_model('D:/Dev/News Aggregator/model_opinion.h5')
        new_model.summary()
        print("hi")

        article_list = {'url': [url],
                'is_opinion': [1]
                }
        article_sample = pd.DataFrame(article_list, columns = ['url', 'is_opinion'])

        article_sample= article_sample[article_sample['url'].notnull()]
        max_length = self.get_max_length(self,article_sample)
        sample_X, sample_Y = self.preprocess(self,article_sample,embed,max_length)
        prediction = new_model.predict(sample_X)
        print('Predicted class: ', prediction)
        print('Real class:  ', sample_Y)

    def get_max_length(self,df):
        """
        get max token counts from train data, 
        so we use this number as fixed length input to RNN cell
        """
        max_length = 0
        
        for row in df['url']:
            if len(row.split("/")) > max_length:
                max_length = len(row.split("/"))
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
        reviews = df['url'].tolist()
        
        encoded_reviews = self.get_word2vec_enc(self,reviews,embd)
        padded_encoded_reviews = self.get_padded_encoded_reviews(self,encoded_reviews,maxlength)
        # encoded labels
        labels = df['is_opinion'].tolist()
        encoded_labels = [self.labels_encode(self,label) for label in labels]
        X = np.array(padded_encoded_reviews)
        Y = np.array(encoded_labels)
        return X, Y
    def sampletest(self,urlTest):
        self.loadSample(self,urlTest)
        return urlTest+"hello1111"

class relevance():
    from newspaper import Article
    import datetime as d

    url = 'https://cnnphilippines.com/news/2021/4/10/new-community-quarantine-classification-ncr-plus.html'
    article = Article(url)
    #use this to access other functions of the article
    article.download() 
    article.parse()

    #get today's datetime and also the article's published datetime
    today = d.datetime.now()
    newsDate = article.publish_date

    rel = today - newsDate 
    days = rel.days 
    print(days, "day(s)")
    def relevanceScore(d):
        score = 100
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

        score = score - (d * multiplier)
        if score < 0:
            score = 0
        return score

    print(relevanceScore(days))