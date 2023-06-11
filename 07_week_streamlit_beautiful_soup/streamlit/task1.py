import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "id":[1,2,3,4,5],
    "name":['Qasim','Hamza',"Ali","Rashid","Konain"]
})

st.write("My First Streamlit Application")
st.write(df)