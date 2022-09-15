# -*- coding:utf-8 -*-
import os 
from os import path
from nlp.lstm import load_model, create_dictionaries
from gensim.models import Word2Vec
import jieba
import numpy as np
from nlp.lstm import lstm_predict_single
from wordcloud import wordcloud_file

def statistic(filename):
    model_lstm = load_model()
    model_word2vec = Word2Vec.load('nlp/model/lstm_model/Word2vec_model.pkl')
    intputbuf = open(str(filename),'r',encoding='utf-8')
    outputbuf = open('statistic.txt','a',encoding='utf-8')
    pcounter , ncounter = 0,0
    for line in intputbuf:        
        sentence = str(line).strip()        
        # result = lstm_predict_single(sentence)

        words = jieba.lcut(sentence)
        words = np.array(words).reshape(1, -1)
        _, _, data = create_dictionaries(model_word2vec, words)
        data.reshape(1, -1)
        predict_result = model_lstm.predict(data)

        if predict_result[0][1] >= 0.5:
            result='Positive'
        else:
            result='Negative'        

        if result=='Positive':pcounter+=1
        else:ncounter+=1
        print(filename,pcounter,ncounter)
        finalstr = str(filename)+','+str(pcounter)+','+str(ncounter)

    outputbuf.write(finalstr+'\n')

def scaner_file (url):
    file  = os.listdir(url)
    for f in file:
        real_url = path.join (url , f)
        if path.isfile(real_url):
            print(path.abspath(real_url))
            statistic(real_url)
            # wordcloud_file(real_url,100)
        elif path.isdir(real_url):
            scaner_file(real_url)
        else:
            pass

if __name__ == '__main__':

    statistic("孤勇者.txt")
    # scaner_file("网易云热歌榜200首") 
