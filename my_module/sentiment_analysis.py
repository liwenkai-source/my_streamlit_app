from snownlp import SnowNLP
import pandas as pd
import streamlit as st
def sentiment_analysis():
    fenxi = []
    with st.spinner('Wait for it...'):
        try:
            data = pd.read_csv('./弹幕/弹幕.csv')
            danmu = data['视频弹幕'].tolist()
            for text in danmu:
                s = SnowNLP(text)
                polarity = s.sentiments
                if polarity > 0.5:
                    fenxi.append('积极')
                else:
                    fenxi.append('消极')
            data['情感分析'] = fenxi
            with st.expander("弹幕情感分析"):
                    st.dataframe(data)
        except:
            pass
        st.header('请输入你想要分析的弹幕文本')
        with st.spinner('Wait for it...'):
            text = st.text_input('')
            s = SnowNLP(text)
            polarity = s.sentiments
            if polarity > 0.5:
                st.header('是积极的')
                st.success('You did it !', icon="✅")
                st.balloons()
            else:
                st.header('是消极的')
                st.success('You did it !', icon="✅")
                st.balloons()

