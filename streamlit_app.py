import altair as alt
import math
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


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

col1, col2, col3 = st.columns(3)
with st.container():
    with col1:
        st.subheader('CO2 Emissions by Country')
        arr = np.random.normal(1, 1, size=100)
        fig, ax = plt.subplots()
        ax.hist(arr, bins=20)
    with col2:
        st.subheader('Temp')
        arr = np.random.normal(1, 1, size=100)
        fig, ax = plt.subplots()
        ax.hist(arr, bins=20)
    with col3:
        arr = np.random.normal(1, 1, size=100)
        fig, ax = plt.subplots()
        ax.hist(arr, bins=20)

# Display an interactive chart to visualize CO2 Emissions by Top N Countries
with st.container():
    st.subheader('Input comments')
    with st.expander(""):
        df = pd.DataFrame(columns=['name','id','comment'])
        
        config = {
            'name' : st.column_config.TextColumn('Name (required)', width='large', required=True),
            'id' : st.column_config.TextColumn('ID',max_chars=50),
            'comment': st.column_config.TextColumn('ID',max_chars=500),
        
        }

        result = st.data_editor(df, column_config = config, num_rows='dynamic')

        if st.button('Get results'):
            st.write(result)


    