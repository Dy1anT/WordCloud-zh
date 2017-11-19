# -*- coding: utf-8 -*-
#色彩词云

from wordcloud import WordCloud, ImageColorGenerator
import jieba
from scipy.misc import imread
from os import path
import matplotlib.pyplot as plt

def draw_wordcloud():
    comment_text = open("word.txt",'r').read() #读入一个txt文件
    cut_text = ' '.join(jieba.cut(comment_text))
    color_mask = imread("picture.jpg") # 读取背景图片
    cloud = WordCloud(
        font_path = "msyh.ttf", #设置字体，不指定就会出现乱码        
        background_color = 'white', #设置背景色
        mask = color_mask, #词云形状
        max_words = 2000, #允许最大词汇
        max_font_size = 5000 #最大号字体
    )
    word_cloud = cloud.generate(cut_text)
    image_colors = ImageColorGenerator(color_mask)
    word_cloud.recolor(color_func = image_colors)
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()
    word_cloud.to_file("wordcloud.jpg") #保存图片

if __name__ == '__main__':
    draw_wordcloud()
