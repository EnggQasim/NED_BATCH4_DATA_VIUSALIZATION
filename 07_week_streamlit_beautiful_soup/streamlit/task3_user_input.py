import streamlit as st

st.text_input("Your Name", key="name")

st.write(st.session_state.name)