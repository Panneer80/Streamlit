import streamlit as st

st.title("Hello World")

st.text_input("Movie title", "Life of Brian")
with st.sidebar:
    st.header("Side Heading")
    st.write("some random text")

