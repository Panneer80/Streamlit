import streamlit as st
from modules.civil_boq.price_setting import set_price


st.subheader("Bill Of Quantity (BOQ) | Data entry")

set_price(st)

