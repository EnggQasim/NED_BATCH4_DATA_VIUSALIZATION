import numpy as np
import pandas as pd
import streamlit as st

df = pd.DataFrame({
    "first column": [1,2,3,4],
    "second colum": [10,20,30,40]
})

option = st.selectbox(
    "Which number do you like best?",
    df['first column']
)

st.write("You have selected:",option)


add_slider = st.sidebar.slider(
    "Select a range of values",
    0.0, 100.00 , (25.0, 75.0)
)

st.write(add_slider)