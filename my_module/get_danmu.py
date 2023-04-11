import  requests
import  os
import re
import bs4
import pandas as pd
import streamlit as st
import numpy as np
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import jieba
from collections import Counter
from pylab import mpl
import random
# os.path.exists 函数判断文件夹是否存在
def is_true_path(path):
    folder = os.path.exists(path)
    # 判断是否存在文件夹如果不存在则创建为文件夹
    if not folder:
            # os.makedirs 传入一个path路径，生成一个递归的文件夹；如果文件夹存在，就会报错,因此创建文件夹之前，需要使用os.path.exists(path)函数判断文件夹是否存在；
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    else:
            pass



def GetWordCloud(str):
    path_img = "./ciyun.png"
    background_image = np.array(Image.open(path_img))
    # 结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云,感兴趣的朋友可以去查一下，有多种分词模式
    # Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

    wordcloud = WordCloud(
        # 设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
        font_path="C:/Windows/Fonts/simfang.ttf",
        background_color="white",
        # mask参数=图片背景，必须要写上，另外有mask参数再设定宽高是无效的
        mask=background_image).generate(str)
    # 生成颜色值
    image_colors = ImageColorGenerator(background_image)
    # 下面代码表示显示图片
    # plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
    # plt.axis("off")
    # plt.show()
    wordcloud.to_file('./弹幕/弹幕词云图.jpg')  # 保存图片
    image = Image.open(f'./弹幕/弹幕词云图.jpg')
    with st.expander("User barrage word cloud map"):
        st.image(image, caption='This is the cloud map of bullet screen words', use_column_width=True)
        with open('./弹幕/弹幕词云图.jpg', "rb") as file:
            btn = st.download_button(
                label="你可以点击这个按钮将这个弹幕词云图下载下来",
                data=file,
                file_name="danmu_ciyun.png",
                mime="image/png"
            )
def danmu_tongji(text):
    # 去掉不想要的字
    color_map = ['#FFE4C4', '#87CEFA', '#FFB6C1', '#F5DEB3', '#808080', '#8A2BE2', '#DC143C', '#FFA07A', '#9370DB',
                 '#708090', '#F0E68C', '#87CEEB', '#E6E6FA', '#6B8E23', '#FFC0CB', '#E0FFFF', '#DAA520', '#CD5C5C',
                 '#FF69B4', '#00CED1']

    text = ' '.join(jieba.cut(text))
    exclude = {'的', '了', '和', '是', '在', '我们', '我', '你', '哈哈哈', '哈哈哈哈', '哈哈', '呜呜', '也', '都', '就',
               '是', '啊', '真的', '就是', '所以', '这句',
               '这么', '这个', '他', '他们', '可以', '没有', '有', '太', '好', '\n ', '这', '，', '。', '：', '！', '？',
               '/', ';', '(', ')', '《', '》', '{', '}'}
    words_list = jieba.cut(text)
    words = list(words_list)
    # 计算每个词语频率
    freqs = Counter([word for word in words if (word not in exclude and len(word) > 1)])
    # 选出频率大于10次的词语
    selected_words = {word: freq for word, freq in freqs.items() if freq >= 5}
    # 绘制饼状图
    labels = list(selected_words.keys())
    sizes = list(selected_words.values())
    data = [random.randint(1, 100) for i in range(len(labels))]
    colors = {}
    for i in range(len(data)):
        colors[i] = random.choice(color_map)
    plt.figure(figsize=(14, 14), dpi=100)
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140,colors=[colors[x] for x in range(len(data))],shadow=True)
    mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
    plt.axis('equal')
    plt.title('Barrage Word Frequency')
    plt.legend(title='Words', loc='center left')
    plt.savefig('./弹幕/弹幕统计图.jpg')
    with st.expander("User barrage statistics chart"):
        st.pyplot(plt, caption='这是弹幕统计图', use_column_width=True)
        with open('./弹幕/弹幕统计图.jpg', "rb") as file:
            btn = st.download_button(
                label="你可以点击这个按钮将这个视频的弹幕统计图下载下来",
                data=file,
                file_name="danmu_tongji.jpg",
                mime="png/jpg"
            )


def get_danmu(danmu_url):
    with st.spinner('Wait for it...'):
        is_true_path('./弹幕')
        df = pd.DataFrame(columns=["视频弹幕"])
        file_name = f"./弹幕/弹幕.csv"  # 弹幕保存文件
        # 获取页面
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        request = requests.get(url=danmu_url, headers=headers)
        request.encoding = "utf-8"
        # 提取弹幕
        soup = bs4.BeautifulSoup(request.text, "lxml")
        results = soup.find_all("d")
        # 数据处理
        data = [data.text for data in results]
        for i in range(0, len(data)):  # 正则去掉多余的空格和换行
            m = re.sub("\s+", " ", data[i])
            data[i]=m
        b = 1
        df.loc[0] = '视频弹幕'
        for j in range(0, len(data)):
            df.loc[b] = data[j]
            b = b + 1
        df.to_csv(file_name,index=False, header=None, encoding="utf_8_sig")
        df = pd.read_csv(file_name)
        word = jieba.lcut(' '.join(data))  # 将数据精确成词语
        str = ' '.join(word)  # 再将词语转换成字符串,为后续词云作准备
        text = open('./弹幕/弹幕.csv', encoding="utf-8").read()
        with st.expander("评论用户弹幕"):
            st.dataframe(df)
            with open('./弹幕/弹幕.csv', "rb") as file:
                btn = st.download_button(
                    label="你可以点击这个按钮将这个视频的弹幕下载下来",
                    data=file,
                    file_name="danmu.txt",
                    mime="txt/csv"
                )
        GetWordCloud(str)
        danmu_tongji(text)
