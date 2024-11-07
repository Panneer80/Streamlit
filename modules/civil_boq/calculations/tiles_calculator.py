import streamlit as st
import pandas as pd

def tiles_cost_calculator():
    if "tiles_work_df" in st.session_state:
        df = st.session_state.tiles_work_df
        df["total_price"] = df["Area"] * df["Price per Sq.ft"]
        st.session_state.total_tiles_cost = df["total_price"].sum()
    else:
        st.session_state.total_tiles_cost = 0
