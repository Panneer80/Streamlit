import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
#working with charts

def charts_t():
    st.title("Plotting in Streamlit with Plotly")
    df = pd.read_csv("C:\\work\\Streamlit_Code\\LearnStreamlit\\Module01\\data\\prog_languages_data.csv")
    st.dataframe(df)

    fig = px.pie(df, values='Sum', names='lang', title='Plotting languages')
    st.plotly_chart(fig)

    fig2 = px.bar(df, x='lang', y='Sum')
    st.plotly_chart(fig2)