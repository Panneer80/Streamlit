
import streamlit as st

from modules.civil_boq.page_elements.concrete_work import concrete_work
from modules.civil_boq.page_elements.doors_windows import door_window_work
from modules.civil_boq.page_elements.masonary_work import masonary_work
from modules.civil_boq.page_elements.price_setting import set_price
from modules.civil_boq.page_elements.tiles_work import tiles_work
st.write(st.session_state)
st.header("BOQ Generator")
st.markdown("##### Enter your data")
st.divider()
set_price()
concrete_work(st)
masonary_work(st)
door_window_work(st)
tiles_work(st)

st.divider()
generate, print, clear, finalize = st.columns(4)
 
if st.button("Generate BOQ", type="primary", key="generate_btn_poq_page_end"):
    st.switch_page("modules/civil_boq/print_page.py")

