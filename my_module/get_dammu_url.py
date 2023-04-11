import requests
import bs4
import re
import pandas as pd
import os

path = './弹幕'
# os.path.exists 函数判断文件夹是否存在
folder = os.path.exists(path)
# 判断是否存在文件夹如果不存在则创建为文件夹
if not folder:
        # os.makedirs 传入一个path路径，生成一个递归的文件夹；如果文件夹存在，就会报错,因此创建文件夹之前，需要使用os.path.exists(path)函数判断文件夹是否存在；
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
else:
        pass


def get_danmu_url(danmu_url) :

    file_name=f"./弹幕/弹幕.csv"#弹幕保存文件
    #获取页面
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
    request=requests.get(url=danmu_url, headers=headers)
    request.encoding="utf-8"
    #提取弹幕
    soup=bs4.BeautifulSoup(request.text,"lxml")
    results=soup.find_all("d")
    #数据处理
    data=[data.text for data in results]
    for i in data:#正则去掉多余的空格和换行
        i=re.sub("\s+"," ",i)
    #查看数量
    # print("弹幕数量为{}".format(len(data)))
    #输出文件
    df=pd.DataFrame(data)
    df.to_csv(file_name,index=False,header=None,encoding="utf_8_sig")
