import streamlit as st
import pandas as pd

st.text("Task List")
list_data = pd.read_json("modules/task_manager/task_data.json")
selected_coloums = ['id','title','assigned to']

st.dataframe(list_data[selected_coloums].set_index('id'))