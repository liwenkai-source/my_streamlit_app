import requests
from lxml import etree
import  re
import streamlit as st
def get_viedo(bilibili_url):
  with st.spinner('Wait for it...'):
    url=bilibili_url
    try:
        st.header('下面是该视频的音频和视频')
        headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53',
                    'cookie':"buvid3=E8854EBD-E4BF-04B5-29C7-D9C2F1556CBD36385infoc; i-wanna-go-back=-1; _uuid=10CD96C36-B72F-92EF-3387-E2D7C1104E10EC37078infoc; buvid_fp=02b331c2843088f1f0807f484002d8e5; DedeUserID=1482172628; DedeUserID__ckMd5=e0a0fde62d6df8d1; LIVE_BUVID=AUTO9916622943658682; nostalgia_conf=-1; CURRENT_BLACKGAP=0; rpdid=|(J|~YkYJYR~0J'uYYkkmRYl|; b_ut=5; is-2022-channel=1; fingerprint3=422debf2fe4e989460ab9d489e170256; hit-dyn-v2=1; b_nut=100; blackside_state=1; buvid4=A2624E58-6142-0769-6562-952F0BC4C2CA37882-022090420-qz8RgjSxjvRz0D%2FGMBrHuw%3D%3D; fingerprint=2eee4eaff4ec547d4cb609306f4ca5f9; CURRENT_QUALITY=80; SESSDATA=d5481655%2C1680267023%2C28b64%2Aa1; bili_jct=9e3a77dab6036ae77211714e6a06aa53; sid=808exllu; CURRENT_FNVAL=4048; b_lsid=C8A104A810_1839D719071; theme_style=light; bp_video_offset_1482172628=712769644222480400; PVID=5",
                    'referer': 'https://www.bilibili.com/video/BV1m54y1Y7nR/?spm_id_from=autoNext&vd_source=9c73a36d562e50cb87942b740ace868b'

                }
        response = requests.get(url=url,headers=headers)
        data = response.text
        html_obj = etree.HTML(data)
        title=html_obj.xpath('//div/div//h1/@title')[0]
        url_str=html_obj.xpath('//script[contains(text(),"window.__playinfo__")]/text()') [0]
        video_url=re.findall(r'"video":\[{"id":\d+,"baseUrl":"(.*?)",',url_str)[0]
        audio_url=re.findall(r'"audio":\[{"id":\d+,"baseUrl":"(.*?)",',url_str)[0]
        response_video_url=requests.get(url=video_url,headers=headers)
        response_audio_url=requests.get(url=audio_url,headers=headers)
        data_video_url=response_video_url.content
        data_audio_url=response_audio_url.content
        with open (f"./视频音频/{title}.mp4",'wb') as f:
                    f.write(data_video_url)
        with open(f"./视频音频/{title}.mp3", 'wb') as f:
                    f.write(data_audio_url)
        # audio = ffmpeg.input(f"./视频音频/{title}.mp3")
        # video = ffmpeg.input(f"./视频音频/{title}.mp4")
        # out = ffmpeg.output(video, audio,f"./视频音频/{title}_finally.mp4")
        # out.run()
        # os.system(f'./ffmpeg.exe -i "./视频音频/{title}.mp4" -i  "./视频音频/{title}.mp3" -c copy "./视频音频/{title}_finally.mp4" ')

        audio_file = open(f"./视频音频/{title}.mp3", 'rb')
        audio_bytes = audio_file.read()
        st.video(audio_bytes)
        with open(f"./视频音频/{title}.mp3", "rb") as file:
            btn = st.download_button(
                label="你可以点击这个按钮将这个音频下载下来",
                data=file,
                file_name="视频.mp3",
                mime="mp3"
            )
        video_file = open(f"./视频音频/{title}.mp4", 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        with open(f"./视频音频/{title}.mp4", "rb") as file:
            btn = st.download_button(
                label="你可以点击这个按钮将这个视频下载下来",
                data=file,
                file_name="视频.mp4",
                mime="mp4/avi"
            )

        os.remove(f"./视频音频/{title}.mp4")
        os.remove(f"./视频音频/{title}.mp3")
    except :
        pass
