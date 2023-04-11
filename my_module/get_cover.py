import urllib
import os
import streamlit as st
from PIL import Image
def is_true_path(path):
    folder = os.path.exists(path)
    # 判断是否存在文件夹如果不存在则创建为文件夹
    if not folder:
            # os.makedirs 传入一个path路径，生成一个递归的文件夹；如果文件夹存在，就会报错,因此创建文件夹之前，需要使用os.path.exists(path)函数判断文件夹是否存在；
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    else:
            pass


def get_cover(cover_image):
  with st.spinner('Wait for it...'):
    try:
        is_true_path('./封面')
        filename = f"./封面/封面.jpg"
        urllib.request.urlretrieve(url=cover_image, filename=filename)
        image = Image.open(f'./封面/封面.jpg')
        st.image(image, caption='•这是你选择B站视频的封面图', use_column_width=True)
        with open("./封面/封面.jpg", "rb") as file:
            btn = st.download_button(
                label="你可以点击这个按钮将这个视频封面下载下来",
                data=file,
                file_name="封面.png",
                mime="jpg/png"
            )
    except:
        pass