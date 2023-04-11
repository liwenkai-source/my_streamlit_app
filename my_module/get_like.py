import requests
import json
import streamlit as st
# 爬虫地址
alphabet = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'


def dec(x):  # BV号转换成AV号
    r = 0
    for i, v in enumerate([11, 10, 3, 8, 4, 6]):
        r += alphabet.find(x[v]) * 58 ** i
    return (r - 0x2_0840_07c0) ^ 0x0a93_b324

def get_like(BV):
    try:
        bid = BV
        aid = dec(bid)
        url = r'https://api.bilibili.com/x/web-interface/archive/stat?aid=' + str(aid)
        # 携带cookie进行访问
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
        }
        # 获取url
        response = requests.get(url, timeout=30, headers=headers)
        text = response.text
        jsonobj = json.loads(text)
        # 从Json对象获取视频基本信息并转入词典中
        view=jsonobj['data']['view']
        danmuku_num= jsonobj['data']['danmaku']
        reply_num= jsonobj['data']['reply']
        favorite_num= jsonobj['data']['favorite']
        coin_num=jsonobj['data']['coin']
        share_num=jsonobj['data']['share']
        like_num=jsonobj['data']['like']
        rank=jsonobj['data']['his_rank']
        col1, col2, col3,col4= st.columns(4)
        col5, col6, col7, col8=st.columns(4)

        col1.metric("播放量", view)
        col2.metric("弹幕数量", danmuku_num)
        col3.metric("评论数量", reply_num)
        col4.metric("收藏数量", favorite_num)
        col5.metric("硬币数量", coin_num)
        col6.metric("转发数量", share_num)
        col7.metric("点赞数量", like_num)
        col8.metric("全站最高排名", rank)
    except:
        pass






