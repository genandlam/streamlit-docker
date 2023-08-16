import altair as alt
import math
import pandas as pd
import streamlit as st
#import matplotlib.pyplot as plt
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

def get_data(): 
    df = pd.read_csv('./data/RAWDATA.csv')
    
#col1, col2= st.columns(2)
with st.container():
    with st.expander(""):
        st.subheader('Model Metrics/scores')
        df = get_data()
        df = pd.DataFrame(
                        [
                            {"command": "st.selectbox", "rating": 4, "is_widget": True},
                            {"command": "st.balloons", "rating": 5, "is_widget": False},
                            {"command": "st.time_input", "rating": 3, "is_widget": True},
                        ]
                    )

        
    st.dataframe(df, use_container_width=True)

"""
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

"""
    