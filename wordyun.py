# -*- coding: utf-8 -*-

from wordcloud import WordCloud
import jieba
from scipy.misc import imread
import matplotlib.pyplot as plt

def main():
    comment_text = open("text.txt", 'r').read()  # txt文本
    cut_text = ' '.join(jieba.cut(comment_text))
    color_mask = imread("picture.jpg")  # 背景图片
    cloud = WordCloud(
        font_path = "msyh.ttf",  # 字体
        background_color = 'white',  # 背景色
        mask = color_mask,
        max_words = 2000,  # 允许最多词汇
        max_font_size = 5000  # 最大号字体
    )
    word_cloud = cloud.generate(cut_text)
    #image_colors = ImageColorGenerator(color_mask) # 用背景颜色填充
    #word_cloud.recolor(color_func=image_colors)
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()
    word_cloud.to_file("wordcloud.jpg")

if __name__ == '__main__':
    main()
