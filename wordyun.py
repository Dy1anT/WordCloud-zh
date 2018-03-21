# -*- coding: utf-8 -*-

from wordcloud import WordCloud
import jieba
from scipy.misc import imread
from os import path
import matplotlib.pyplot as plt

comment_text = open("text.txt",'r').read() #txt文件
cut_text = ' '.join(jieba.cut(comment_text))
color_mask = imread("pic.jpg") # 背景图片
cloud = WordCloud(
    font_path="msyh.ttf", #字体        
    background_color='white', #背景色
    mask=color_mask,
    max_words=2000, #允许最大词汇
    max_font_size=5000 #最大号字体
)
word_cloud = cloud.generate(cut_text)
plt.imshow(word_cloud)
plt.axis('off')
plt.show()
word_cloud.to_file("wordcloud.jpg")
