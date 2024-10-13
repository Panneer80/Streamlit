
import streamlit as st

from modules.civil_boq.concrete_work import concrete_work
from modules.civil_boq.doors_windows import door_window_work
from modules.civil_boq.masonary_work import masonary_work
from modules.civil_boq.price_setting import set_price
from modules.civil_boq.tiles_work import tiles_work

st.header("BOQ Generator")
st.markdown("##### Enter your data")
st.divider()
set_price(st)
concrete_work(st)
masonary_work(st)
door_window_work(st)
tiles_work(st)
    # plastering_work(st)
st.divider()
generate, print, clear, finalize = st.columns(4)
with finalize:
    st.button(label="Generate BOQ")
