import streamlit as st
import pandas as pd

df = pd.DataFrame({"lat":[24.852430624379622,24.87633000425782],
                   "lon":[66.98888977240608, 67.02116211296422]})

st.map(df)