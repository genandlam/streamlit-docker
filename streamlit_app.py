import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [starting out docker commands] (https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker#prerequisites)

In the meantime, below is an example of what you can do with just a few lines of code:
"""


def create_table():
    df = pd.DataFrame(columns=['name','age','color'])
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    config = {
        'name' : st.column_config.TextColumn('Full Name (required)', width='large', required=True),
        'age' : st.column_config.NumberColumn('Age (years)', min_value=0, max_value=122),
        'color' : st.column_config.SelectboxColumn('Favorite Color', options=colors)
    }

    result = st.data_editor(df, column_config = config, num_rows='dynamic')

    if st.button('Get results'):
        st.write(result)


if __name__ == "__main__":

    create_table()
