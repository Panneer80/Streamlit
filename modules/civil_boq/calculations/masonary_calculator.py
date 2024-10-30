import streamlit as st
import pandas as pd

def masonary_calculator():
    if "masonary_work_df" in st.session_state:
        print("Hi")
        df = st.session_state.masonary_work_df
        df.to_csv("C:\\work\\Streamlit_Code\\Streamlit\\test.csv")