import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

st.set_page_config(
     page_title="Histogram Charts ",
     page_icon="❀",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
    #     'Get Help': 'https://developers.snowflake.com',
#         'About': "This is an *extremely* cool app powered by Snowpark for Python, Snowflake Data Marketplace and Streamlit"
     }
)

def get_data(): 
    df = pd.read_csv('data/RAWDATA.csv')
    df = df.fillna(0.0)
    df =df.round(2)
    return df
st.subheader('Model Metrics/scores')

with st.container():
    df = get_data()
    fig = px.bar(df[['INTEL_KEY','TP_CNT','FP_CNT']], x="INTEL_KEY", y=['TP_CNT','FP_CNT'])
    st.plotly_chart(fig, use_container_width=True)
    
st.subheader('Table for scores')
with st.container():
    with st.expander(""):

        x = df[['INTEL_KEY','Precision_CNT','Precision_ATR']]
        x['Precision_CNT'] = ((df['Precision_CNT']*100).astype(int)).astype(str)+'%'
        x['Precision_ATR'] =((df['Precision_ATR']*100 ).astype(int)).astype(str)+'%'
        st.dataframe(x, use_container_width=True)




