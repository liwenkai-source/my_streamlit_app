import  requests
import  os
import re
import json
import altair as alt
import streamlit as st
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
def radar_chart(*args):
    matplotlib.rcParams['font.family'] = 'SimHei'  # 将字体设置为黑体'SimHei'
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    if(len(args)==3):
        labels = np.array(["boy", "girl", "secret"])
        dataLenth = 3  # 数据长度
        data = np.array(args)
        angles = np.linspace(0, 2 * np.pi, dataLenth, endpoint=False)  # 根据数据长度平均分割圆周长
        # 闭合
        data = np.concatenate((data, [data[0]]))
        angles = np.concatenate((angles, [angles[0]]))
        labels = np.concatenate((labels, [labels[0]]))  # 对labels进行封闭
        fig = plt.figure(facecolor="white",figsize=(10,8))  # facecolor 设置框体的颜色
        plt.subplot(111, polar=True)  # 将图分成1行1列，画出位置1的图；设置图形为极坐标图
        plt.plot(angles, data, 'black', linewidth=2)
        plt.fill(angles, data, facecolor='g', alpha=0.25)  # 填充两条线之间的色彩，alpha为透明度
        plt.thetagrids(angles * 180 / np.pi, labels)  # 做标签
        plt.figtext(0.52,0.95,'User gender radar map',ha='center')   #添加雷达图标题
        plt.grid(True)
        st.pyplot(plt)
    elif(len(args)==5):
        labels = np.array(["level2","level3","level4","level5","level6"])
        dataLenth = 5  # 数据长度
        data = np.array(args)
        angles = np.linspace(0, 2 * np.pi, dataLenth, endpoint=False)  # 根据数据长度平均分割圆周长
        # 闭合
        data = np.concatenate((data, [data[0]]))
        angles = np.concatenate((angles, [angles[0]]))
        labels = np.concatenate((labels, [labels[0]]))  # 对labels进行封闭
        fig = plt.figure(facecolor="white",figsize=(10,8))  # facecolor 设置框体的颜色
        plt.subplot(111, polar=True)  # 将图分成1行1列，画出位置1的图；设置图形为极坐标图
        plt.plot(angles, data, 'black', linewidth=2)
        plt.fill(angles, data, facecolor='g', alpha=0.25)  # 填充两条线之间的色彩，alpha为透明度
        plt.thetagrids(angles * 180 / np.pi, labels)  # 做标签
        plt.figtext(0.52,0.95,'User level radar map',ha='center')   #添加雷达图标题
        plt.grid(True)
        st.pyplot(plt)
# os.path.exists 函数判断文件夹是否存在
def is_true_path(path):
    folder = os.path.exists(path)
    # 判断是否存在文件夹如果不存在则创建为文件夹
    if not folder:
            # os.makedirs 传入一个path路径，生成一个递归的文件夹；如果文件夹存在，就会报错,因此创建文件夹之前，需要使用os.path.exists(path)函数判断文件夹是否存在；
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    else:
            pass

def get_pinglun_user(oid):
    with st.spinner('Wait for it...'):
        try:
            is_true_path('./评论用户信息')
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
            'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62',
            }
            sort = 2
            # type  所属类型
            url=f'https://api.bilibili.com/x/v2/reply?pn=1&type=1&oid={oid}&sort={sort}'

            reponse = requests.get(url,headers=headers)
            a = json.loads(reponse.text)
            df = pd.DataFrame(columns=["用户性别", "用户名称", "用户等级"])
            page=1000
            nan, nv, baomi = 0, 0, 0
            all_sex = []
            all_usename = []
            all_usename_level = []
            all_comment = []
            number_huiyuan=0
            number_no_huiyuan=0
            for i in range(1, page):
                url = f'https://api.bilibili.com/x/v2/reply?pn={i}&type=1&oid={oid}&sort={sort}'
                reponse = requests.get(url, headers=headers)
                data = reponse.text
                # 用户的评论
                if (data.find('需要升级成为lv2会员后才可以评论，先去答题转正吧！') < 500):
                    break
                comment = re.findall('"content":{"message":(.*?),"members"', data)
                # 用户的性别
                sex = re.findall('"sex":"(.*?)","sign"', data)
                # 用户的ip
                ip = re.findall('"location":"(.*?)"', data)
                huiyuan = re.findall('"vipStatus":(.*?)"', data)
                # 用户的昵称
                usename = re.findall('"uname":"(.*?)"', data)
                # 用户的b站等级
                usename_level = re.findall('"current_level":(.*?),', data)
                huiyuan = re.findall('"vipStatus":(.*?)"', data)
                is_huiyuan = []
                for i in huiyuan:
                    i = i.split(',')
                    is_huiyuan.append(int(i[0]))

                number_huiyuan +=is_huiyuan.count(1)
                number_no_huiyuan+= is_huiyuan.count(0)
                for j in range(0, len(sex)):
                    if (usename[j] not in all_usename):
                        if sex[j] == '男':
                            nan = nan + 1
                        elif sex[j] == '女':
                            nv = nv + 1
                        elif sex[j] == '保密':
                            baomi = baomi + 1
                        all_sex.append(sex[j])
                        all_usename.append(usename[j])
                        all_usename_level.append(usename_level[j])
                for k in comment:
                    if (k not in all_comment):
                        all_comment.append(k)
            people = nan + nv + baomi
            all_huiyuan = number_huiyuan + number_no_huiyuan
            st.header('下面是该视频下面的评论用户的信息')
            st.markdown('•据统计,评论区中:' + '男：%d，女：%d，保密：%d' % (nan, nv, baomi))
            st.markdown('•据统计,评论区中:' + '大会员：%d，非大会员：%d' % (number_huiyuan, number_no_huiyuan))
            st.markdown('•大会员百分之%.2f，非大会员的占百分之%.2f' % (number_huiyuan / all_huiyuan * 100, number_no_huiyuan / all_huiyuan * 100))
            st.markdown('•男的占百分之%.2f，女的占百分之%.2f，保密的占百分之%.2f' % (nan / people*100, nv / people*100, baomi / people*100))
            b = 0

            for j in range(0, len(all_sex)):
                df.loc[b] = [all_sex[j], all_usename[j], all_usename_level[j]]
                b = b + 1
            df.to_csv(f'./评论用户信息/评论用户信息.csv', index=False)
            data = pd.read_csv(f'./评论用户信息/评论用户信息.csv')
            with st.expander("评论用户信息"):
                st.dataframe(data)
                with open(f'./评论用户信息/评论用户信息.csv', "rb") as file:
                    btn = st.download_button(
                        label="你可以点击这个按钮将这个视频的评论用户信息下载下来",
                        data=file,
                        file_name="pinglun_user.txt",
                        mime="txt/csv"
                    )
            counts1 = data['用户性别'].value_counts()
            sexs = pd.DataFrame({'sex': counts1.index, 'numbers': counts1.values})
            counts2 = data['用户等级'].value_counts()
            levels = pd.DataFrame({'level': counts2.index, 'numbers': counts2.values})
            try:
                levels = levels[-levels.level.isin([0, 1])]
            except:
                pass
            level6 = levels.loc[levels['level'] == 6, 'numbers'].tolist()[0]
            level5 = levels.loc[levels['level'] == 5, 'numbers'].tolist()[0]
            level4 = levels.loc[levels['level'] == 4, 'numbers'].tolist()[0]
            level3 = levels.loc[levels['level'] == 3, 'numbers'].tolist()[0]
            level2 = levels.loc[levels['level'] == 2, 'numbers'].tolist()[0]
            sex_list = [nan, nv, baomi]
            level_list = [level2,level3,level4,level5,level6]
            with st.expander("我们先来看一下用户性别和等级分布的雷达图,了解一下大致的用户分布情况"):
                radar_chart(*sex_list)
                radar_chart(*level_list)
            # 标签和比例
            labels = ['boy', 'girl', 'secret']
            sizes = [sexs[sexs['sex'] == '男'].iat[0, 1],
                     sexs[sexs['sex'] == '女'].iat[0, 1]
                , sexs[sexs['sex'] == '保密'].iat[0, 1]]

            # 颜色
            colors = ['#ff9999', '#66b3ff', '#99ff99']

            # 创建饼状图
            fig, ax = plt.subplots()
            # fig=plt.figure(figsize=(10,6))
            ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                   shadow=True, startangle=90)

            # 设置标题
            ax.set_title('male-female ratio')

            chart2 = alt.Chart(levels).mark_line().encode(
                alt.Y('numbers'),
                alt.X('level'),
            )
            plot = alt.Chart(levels).mark_bar(size=40).encode(
                alt.Y('numbers'),
                alt.X('level'),
            )

            chart4 = alt.Chart(sexs).mark_line().encode(
                alt.Y('numbers'),
                alt.X('sex'),
            )
            plot2 = alt.Chart(sexs).mark_bar(size=40).encode(
                alt.Y('numbers'),
                alt.X('sex'),
            )
            with st.expander("下面是一些关于评论用户更加详细的统计图"):
                st.pyplot(fig)
                st.altair_chart(chart2, use_container_width=True)
                st.altair_chart(plot, use_container_width=True)
                st.altair_chart(chart4, use_container_width=True)
                st.altair_chart(plot2, use_container_width=True)

        except:
            pass


