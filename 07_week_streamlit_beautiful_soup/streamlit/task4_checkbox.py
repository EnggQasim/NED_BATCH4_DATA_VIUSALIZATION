import numpy as np
import pandas as pd
import streamlit as st

if st.checkbox("Show table"):
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns = ['a','b','c']
    )
    st.table(chart_data)