import requests
from lxml import etree
import re
def get_oidcid(bibili_url):
    headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53',
                # 'cookie':"buvid3=E8854EBD-E4BF-04B5-29C7-D9C2F1556CBD36385infoc; i-wanna-go-back=-1; _uuid=10CD96C36-B72F-92EF-3387-E2D7C1104E10EC37078infoc; buvid_fp=02b331c2843088f1f0807f484002d8e5; DedeUserID=1482172628; DedeUserID__ckMd5=e0a0fde62d6df8d1; LIVE_BUVID=AUTO9916622943658682; nostalgia_conf=-1; CURRENT_BLACKGAP=0; rpdid=|(J|~YkYJYR~0J'uYYkkmRYl|; b_ut=5; is-2022-channel=1; fingerprint3=422debf2fe4e989460ab9d489e170256; hit-dyn-v2=1; b_nut=100; blackside_state=1; buvid4=A2624E58-6142-0769-6562-952F0BC4C2CA37882-022090420-qz8RgjSxjvRz0D%2FGMBrHuw%3D%3D; fingerprint=2eee4eaff4ec547d4cb609306f4ca5f9; CURRENT_QUALITY=80; SESSDATA=d5481655%2C1680267023%2C28b64%2Aa1; bili_jct=9e3a77dab6036ae77211714e6a06aa53; sid=808exllu; CURRENT_FNVAL=4048; b_lsid=C8A104A810_1839D719071; theme_style=light; bp_video_offset_1482172628=712769644222480400; PVID=5",
                         'referer': 'https://www.bilibili.com/video/BV1m54y1Y7nR/?spm_id_from=autoNext&vd_source=9c73a36d562e50cb87942b740ace868b',
                         'cookie': "b_nut=1663589137; i-wanna-go-back=-1; _uuid=C1086A3A7-5EE8-AC38-4A4F-710413B57A24E38587infoc; buvid4=5E1BC401-0708-8400-BFCB-FC21E5B75BE638861-022091920-cvpFMEeDpazqDNETbmWRKw%3D%3D; fingerprint3=e4c1229631855c2a7ea4b115eef0a6e9; buvid_fp_plain=undefined; DedeUserID=1482172628; DedeUserID__ckMd5=e0a0fde62d6df8d1; b_ut=5; CURRENT_BLACKGAP=0; nostalgia_conf=-1; header_theme_version=CLOSE; home_feed_column=4; rpdid=|(u|Jll)~RRm0J'uY~)u|~|)l; hit-new-style-dyn=0; hit-dyn-v2=1; fingerprint=576ce659ed26c17b8c94cc054afd398f; buvid3=7BCB7C32-71D2-4751-99E6-70D998F29E1E148795infoc; is-2022-channel=1; CURRENT_FNVAL=4048; CURRENT_QUALITY=120; b_lsid=5E4C9BEC_186F47B414E; SESSDATA=31e20796%2C1694690963%2C27429%2A31; bili_jct=a91392921ee18cb45c5d4cbb64ce0c17; innersign=1; PVID=1; bp_video_offset_1482172628=774387645991092200; buvid_fp=576ce659ed26c17b8c94cc054afd398f; sid=hb66z3mj"
            }
    response = requests.get(url=bibili_url,headers=headers)
    data = response.text
    html_obj = etree.HTML(data)
    try:
        res = requests.get(bibili_url).text
        oid = re.findall('"aid":(.*?)"bvid"',res)[0].split(',')[0]
        cid=re.findall('"cid":(.*?),"page":1,', res)[0].split(',')[0]
        return  oid,cid
    except:
        pass
