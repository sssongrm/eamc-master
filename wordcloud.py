#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

def wordcloud_file(filename,inputnum):
    import jieba
    import re
    import matplotlib.pyplot as plt
    import pandas as pd  # 导入Pandas
    from matplotlib import pyplot as plt
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    import jieba
    import numpy as np
    from PIL import Image
    sourceTxt = str(filename)
    print("source:{}".format(sourceTxt))
    targetTxt = 'wordcloud/target.txt'
    with open(sourceTxt, 'r', encoding='utf-8') as sourceFile, open(targetTxt, 'w', encoding='utf-8') as targetFile:
        for line in sourceFile:
            seg = jieba.cut(line.strip(), cut_all=False)
            output = '/'.join(seg)
            targetFile.write(output)
            targetFile.write('\n')
        print('写入成功！')
        sourceFile.close()
        targetFile.close()

    txt = open("wordcloud/target.txt", "r", encoding='utf-8').read()
    txt00 = open("wordcloud/shuchu.txt", "w", encoding='utf-8')
    words = jieba.lcut(txt)
    counts = {} 
    lt = ['三炮', '##', '......', '24', '10', '30', '2020', '14', '31', '11', '13', '20', '15', '28', '17', '16',
            '29', '微博']
    stopkeyword = [line.strip() for line in open('wordcloud/stopwords.txt', encoding='utf-8').readlines()]
    for word in words:
        if len(word) == 1:
            continue
        elif word in stopkeyword:
            rword = " "
        else:
            rword = word
        counts[rword] = counts.get(rword, 0) + 1
    items = list(counts.items())
    print(items)
    items.sort(key=lambda x: x[1], reverse=True)
    N = inputnum
    wordlist = list()
    r1 = re.compile(r'\w')
    r2 = re.compile(r'[^\d]')
    r3 = re.compile(r'[\u4e00-\u9fa5]')
    r4 = re.compile(r'[^_]')
    for i in range(N):
        word, count = items[i]
        txt00.write("{0:<10}{1:<5}".format(word, count))
        txt00.write('\n')
        if r1.match(word) and r2.match(word) and r3.match(word) and r4.match(word):
            continue
    txt00.close()

    txt = open("wordcloud/shuchu.txt", "r", encoding='utf-8').read()
    words = jieba.lcut(txt)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        elif word == "三炮" or  word == "#" or word== "##" or word=="24" or word=="RAP" or word=="video":
            rword = " "
        else:
            rword = word
        counts[rword] = counts.get(rword, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    N = inputnum
    wordlist = list()
    for i in range(N):
        word, count = items[i]
        wordlist.append(word)
    wl = ' '.join(wordlist)
    cloud_mask = np.array(Image.open("wordcloud/love.jpg"))

    wc = WordCloud(
        background_color="white",
        mask=cloud_mask,
        max_words=100,
        font_path='wordcloud/simsun.ttf',
        height=1200,
        width=1600,
        max_font_size=1000,
        random_state=1000,
    )

    myword = wc.generate(wl)
    plt.imshow(myword)
    plt.axis("off")
    tmp = filename.replace(".txt","")
    wc.to_file(tmp+'.jpg')

wordcloud_file('孤勇者.txt',100)