import streamlit as st
from my_module.get_cover_url import get_cover_url
from my_module.get_cover import get_cover
from my_module.get_oidcid import get_oidcid
from my_module.get_pinglun_user import get_pinglun_user
from my_module.get_like import get_like
from my_module.get_name import get_name
from my_module.get_viedo import get_viedo
from my_module.get_dammu_url import get_danmu_url
from my_module.get_danmu import get_danmu
from my_module.get_pinglun_time import get_pinglun_time
from my_module.get_pinglun import get_pinglun
from my_module.sentiment_analysis import sentiment_analysis
import random
st.set_page_config(
    page_title="B站视频数据爬取的可视化APP",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    },


)
# # 背景图片的网址
# img_url = 'https://pic.dmjnb.com/pic/a3739ef73101cb8abc0f53fa128d66de'
#
# # 修改背景样式
# st.markdown('''<style>.css-fg4pbf{background-image:url(''' + img_url + ''');
# background-size:100% 100%;background-attachment:fixed;}</style>
# ''', unsafe_allow_html=True)
#
# # 侧边栏样式
# st.markdown('''<style>#root > div:nth-child(1) > div > div > div > div >
# section.css-1lcbmhc.e1fqkh3o3 > div.css-1adrfps.e1fqkh3o2
# {background:rgba(255,255,255,0.5)}</style>''', unsafe_allow_html=True)
#
# # 底边样式
# st.markdown('''<style>#root > div:nth-child(1) > div > div > div > div >
# section.main.css-1v3fvcr.egzxvld3 > div > div > div
# {background-size:100% 100% ;background:rgba(207,207,207,0.9);
# color:red; border-radius:5px;} </style>''', unsafe_allow_html=True)
st.sidebar.title("这是一个基于B站视频数据爬取的可视化APP!:sunglasses:")
st.sidebar.image('https://pic1.zhimg.com/50/v2-c2cf9cba078351279b79d36c187a0da0_720w.webp?source=1940ef5c')
@st.cache_resource
def get_audio_bytes(music):
    audio_file = open(f'./音乐/{music}-周杰伦.mp3', 'rb')
    audio_bytes = audio_file.read()
    audio_file.close()
    return audio_bytes
music=st.sidebar.radio('Select Music You Like',['七里香','稻香','发如雪'],index=random.choice(range(3)))
st.sidebar.write(f'正在播放{music}-周杰伦 :musical_note:')
audio_bytes=get_audio_bytes(music)
st.sidebar.audio(audio_bytes, format='audio/mp3')

BV=st.sidebar.text_input('请输入你要爬取视频的BV号')


if not BV:
  st.sidebar.warning('Please input a BV.')
  st.stop()
st.sidebar.success('Thank you for inputting a BV.')

try:
    st.sidebar.header("请在这里筛选:")
    select = houxuan_ciyu = st.sidebar.selectbox('选择你要查看的内容',
    ['NULL', '视频封面', '视频信息', '视频观看', '评论用户信息',
     '弹幕&弹幕词云图&弹幕统计图', '评论时间', '评论','弹幕情感分析'])
    bibili_url = "https://www.bilibili.com/video/" + BV
    if('视频信息' in select):
        with st.spinner('Wait for it...'):
            st.header("你的输入对应的视频网址为")
            st.markdown(bibili_url)
            name = get_name(bibili_url=bibili_url)
            st.header("视频的名称为")
            st.markdown(name)
            st.title("该视频的信息如下")
            get_like(BV)
            oid, cid = get_oidcid(bibili_url)
            st.write(f"视频的oid为:\n{oid}")
            st.write(f"视频的cid为:\n{cid}")
            danmu_url = f"https://comment.bilibili.com/{cid}.xml"
            st.write(f"视频的弹幕网址为:\n{danmu_url}")
            # get_danmu_url(danmu_url)
            st.sidebar.success('You did it !', icon="✅")
            st.balloons()
    elif('视频封面' in select):
        cover_image=get_cover_url(bibili_url=bibili_url)
        st.header("视频所对应的封面网址为")
        st.markdown(cover_image)
        name = get_name(bibili_url=bibili_url)
        get_cover(cover_image)
        st.sidebar.success('You did it !', icon="✅")
        st.balloons()
    elif('视频观看' in select):
        st.header('•原视频如下')
        get_viedo(bilibili_url=bibili_url)
        st.sidebar.success('You did it !', icon="✅")
        st.balloons()
    elif('评论用户信息' in select):
        oid, cid = get_oidcid(bibili_url)
        get_pinglun_user(oid)
        st.sidebar.success('You did it !', icon="✅")
        st.balloons()
    elif ('评论时间' in select):
        oid, cid = get_oidcid(bibili_url)
        get_pinglun_time(oid)
        st.sidebar.success('You did it !', icon="✅")
        st.balloons()
    elif ('评论' in select):
        oid, cid = get_oidcid(bibili_url)
        get_pinglun(oid)
        st.sidebar.success('You did it !', icon="✅")
        st.balloons()
    elif ('弹幕&弹幕词云图&弹幕统计图' in select):
        oid, cid = get_oidcid(bibili_url)
        danmu_url = f"https://comment.bilibili.com/{cid}.xml"
        st.header('弹幕&弹幕词云图&弹幕统计图')
        get_danmu(danmu_url)
        st.sidebar.success('You did it !', icon="✅")
        st.balloons()
    elif ('弹幕情感分析' in select):
        st.header('弹幕情感分析如下')
        sentiment_analysis()
except:
    pass


