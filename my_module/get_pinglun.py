import  requests
import  os
import re
import time
import streamlit as st
import pandas as pd
# os.path.exists 函数判断文件夹是否存在
def is_true_path(path):
    folder = os.path.exists(path)
    # 判断是否存在文件夹如果不存在则创建为文件夹
    if not folder:
            # os.makedirs 传入一个path路径，生成一个递归的文件夹；如果文件夹存在，就会报错,因此创建文件夹之前，需要使用os.path.exists(path)函数判断文件夹是否存在；
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    else:
            pass

def get_pinglun(oid):
    with st.spinner('Wait for it...'):
        try:
            is_true_path('./视频评论')
            headers={
            'authority': 'api.bilibili.com',
            'method': 'GET',
            'path': '/x/v2/reply/main?csrf=afe5ed4a9a6753b478d10edf98a3ae3b&mode=3&next=0&oid=727214708&plat=1&seek_rpid=&type=1',''
            'scheme': 'https',
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cookie': "buvid3=E8854EBD-E4BF-04B5-29C7-D9C2F1556CBD36385infoc; i-wanna-go-back=-1; _uuid=10CD96C36-B72F-92EF-3387-E2D7C1104E10EC37078infoc; LIVE_BUVID=AUTO9916622943658682; nostalgia_conf=-1; CURRENT_BLACKGAP=0; is-2022-channel=1; hit-dyn-v2=1; b_nut=100; blackside_state=1; buvid4=A2624E58-6142-0769-6562-952F0BC4C2CA37882-022090420-qz8RgjSxjvRz0D%2FGMBrHuw%3D%3D; fingerprint3=64bc8418ce8b5ea3534d44d23492eee9; hit-new-style-dyn=0; rpdid=|(J~J|RYl||l0J'uYY)mk||JJ; buvid_fp_plain=undefined; DedeUserID=1482172628; DedeUserID__ckMd5=e0a0fde62d6df8d1; b_ut=5; fingerprint=7793900de8ead50a552759b1c334326b; go_old_video=-1; home_feed_column=4; buvid_fp=7793900de8ead50a552759b1c334326b; CURRENT_QUALITY=116; header_theme_version=CLOSE; CURRENT_PID=31d54340-ca39-11ed-b18c-85d8b6c08eab; SESSDATA=660f99a6%2C1695466682%2C32618%2A31; bili_jct=afe5ed4a9a6753b478d10edf98a3ae3b; bp_video_offset_1482172628=777713363725582300; b_lsid=910DE79D3_18722E19563; bsource=search_baidu; sid=67q8mma3; CURRENT_FNVAL=4048; innersign=1; PVID=4",
            'origin': 'https://www.bilibili.com',
            'referer': 'https://www.bilibili.com/video/BV1QS4y1v74J/?spm_id_from=333.1007.top_right_bar_window_default_collection.content.click&vd_source=9c73a36d562e50cb87942b740ace868b',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62',
            }
            page=1000
            sort=2
            all_comment = []
            df = pd.DataFrame(columns=["视频评论"])
            for i in range(1, page):
                url = f'https://api.bilibili.com/x/v2/reply?pn={i}&type=1&oid={oid}&sort={sort}'
                reponse = requests.get(url, headers=headers)
                data = reponse.text
                # 用户的评论
                if (data.find('需要升级成为lv2会员后才可以评论，先去答题转正吧！') < 500):
                    break
                comment = re.findall('"content":{"message":(.*?),"members"', data)
                for k in comment:
                    if (k not in all_comment):
                        all_comment.append(k)
            b = 0
            for j in range(0, len(all_comment)):
                df.loc[b] = [all_comment[j]]
                b = b + 1
            df.to_csv(f'./视频评论/评论.csv', index=False)
            data = pd.read_csv(f'./视频评论/评论.csv')
            st.header('评论')
            with st.expander("There are their comments"):
                st.dataframe(data)
                with open(f'./视频评论/评论.csv', "rb") as file:
                    btn = st.download_button(
                        label="你可以点击这个按钮将这个视频的评论下载下来",
                        data=file,
                        file_name="pinglun.txt",
                        mime="txt/csv"
                    )
        except:
            pass

