import  requests
import  os
import re
import time
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
# os.path.exists 函数判断文件夹是否存在
def is_true_path(path):
    folder = os.path.exists(path)
    # 判断是否存在文件夹如果不存在则创建为文件夹
    if not folder:
            # os.makedirs 传入一个path路径，生成一个递归的文件夹；如果文件夹存在，就会报错,因此创建文件夹之前，需要使用os.path.exists(path)函数判断文件夹是否存在；
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    else:
            pass
#转换时间ctime的函数
def trans_date(v_timestamp):
    """10位时间戳转换为时间字符串"""
    timeArray = time.localtime(v_timestamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime
#在柱状图上方显示数据

def get_pinglun_time(oid):
    with st.spinner('Wait for it...'):
        try:
            is_true_path('./评论时间')
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
            df = pd.DataFrame(columns=["评论具体时间"])
            page=1000
            all_ctime = []
            sort=2
            b=0
            for i in range(1, page):
                url = f'https://api.bilibili.com/x/v2/reply?pn={i}&type=1&oid={oid}&sort={sort}'
                reponse = requests.get(url, headers=headers)
                data = reponse.text
                # 用户的评论
                if (data.find('需要升级成为lv2会员后才可以评论，先去答题转正吧！') < 500):
                    break
                ctime = re.findall('"ctime":(.*?),"rpid_str":', data)
                for i in range(0, len(ctime)):
                    all_ctime.append(trans_date(int(ctime[i])))

            for j in range(0, len(all_ctime)):
                df.loc[b] = all_ctime[j]
                b = b + 1
            df.to_csv(f'./评论时间/评论时间.csv', index=False)
            df = pd.read_csv(f'./评论时间/评论时间.csv')
            st.header('下面是视频评论的时间分布')
            with st.expander("Comment Time"):
                st.dataframe(df)
                with open(f'./评论时间/评论时间.csv', "rb") as file:
                    btn = st.download_button(
                        label="你可以点击这个按钮将这个视频的用户评论时间下载下来",
                        data=file,
                        file_name="Comment_Time.txt",
                        mime="txt/csv"
                    )


            months = ["01", "02", "03", "04", "05", "06",
                      "07", "08", "09", "10", "11", "12"]
            times = ['AM (6-12:00)', 'PM (12-18:00)', 'PM (18-00:00)', 'AM (0-6:00)']
            month_count = {}
            time_count = {}
            for month in months:
                month_count[month] = 0
            for time in times:
                time_count[time] = 0

            numbers = []
            time_period = []
            with open('./评论时间/评论时间.csv', 'r', encoding='utf-8') as f:
                lines = f.readlines()

            for i in range(1, len(lines)):
                numbers.append((lines[i][5:7]))
            for i in numbers:
                month_count[i] += 1
            keys = list(month_count.keys())
            values = list(month_count.values())
            # 创建画布和子图对象
            fig, ax = plt.subplots(figsize=(10, 6))
            # 设置背景颜色
            ax.set_facecolor('#F2F2F2')
            # 绘制条形图
            bars = ax.bar(keys, values, color='#4C72B0')
            # 添加数据标签
            for bar in bars:
                height = bar.get_height()
                ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 3),
                            textcoords="offset points", ha='center', va='bottom', color='black', fontsize=12)
            # 设置坐标轴标签和标题
            ax.set_xlabel('Monthly review', fontsize=14)
            ax.set_ylabel('quantity', fontsize=14)
            ax.set_title('Monthly statistics on the number of comments', fontsize=18)
            # 设置坐标轴刻度字体大小和颜色
            ax.tick_params(axis='both', which='major', labelsize=12, colors='black')
            # 隐藏上部和右侧的边框
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            # 调整 Y 轴下限，使顶部间隔更合理
            ax.set_ylim([0, max(values) * 1.1])
            # 显示图表
            with st.expander('评论时间段分布图(月份)'):
                 st.pyplot(fig)
            for i in range(1, len(lines)):
                time_period.append(int(lines[i][11:13]))
            for i in time_period:
                if (0 <= i < 6):
                    time_count['AM (0-6:00)'] += 1
                elif (6 <= i <= 12):
                    time_count['AM (6-12:00)'] += 1
                elif (12 < i <= 18):
                    time_count['PM (12-18:00)'] += 1
                else:
                    time_count['PM (18-00:00)'] += 1

            keys = list(time_count.keys())
            values = list(time_count.values())
            colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
            plt.title('Comment time distribution map (time of day)')
            plt.pie(values,colors=colors,labels=keys, explode=[0, 0.1, 0, 0], shadow=True, startangle=90, autopct='%1.1f%%')
            with st.expander('评论时间段分布图(一天的时段)'):
                 st.pyplot(plt)
        except:

            pass

