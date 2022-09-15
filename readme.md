# eamc-master
数据仓库与数据挖掘课程设计。基于自然语言处理的歌曲评论情感分析，通过爬虫爬取网易云音乐歌曲评论，并通过LSTM模型分析音乐评论的情感分布。

### 依赖
```
pip3 install -r requirements.txt
```

### 组成
* webspider.py 爬虫
* statistic.py 统计评论情感分布
* wordcloud 词云

### 运行
训练LSTM模型，使用的数据集在`nlp/data/`目录下：
```
cd nlp
python3 lstm.py 
```

爬取网易云歌曲评论：
```
python3 webspider.py
```

用LSTM评价歌曲评论：
```
python3 statistic.py
```

对歌曲评论绘制词云：
```
python3 wordcloud.py
```

### 参考
网易云歌曲评论爬虫部分参考CSDN链接：
>https://blog.csdn.net/qq_41573860/article/details/119775255
