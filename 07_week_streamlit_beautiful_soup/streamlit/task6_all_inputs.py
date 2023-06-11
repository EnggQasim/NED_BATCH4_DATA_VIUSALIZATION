import streamlit as st
import pandas as pd

# st.text('Fixed width text')
# st.markdown('_Markdown_') # see *
# st.latex(r''' e^{i\pi} + 1 = 0 ''')
# st.write('Most objects') # df, err, func, keras!
# st.write(['st', 'is <', 3]) # see *
# st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')


df = pd.DataFrame({
    "id":[1,2,3,4,5],
    "name":['Qasim','Hamza',"Ali","Rashid","Konain"]
})

st.dataframe(df)

a = st.sidebar.radio('Select one:', [1, 2])
st.write(a)