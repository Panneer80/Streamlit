
import streamlit as st

from modules.civil_boq.calculations.masonary_calculator import masonary_calculator
from modules.civil_boq.page_elements.concrete_work import concrete_work
from modules.civil_boq.page_elements.doors_windows import door_window_work
from modules.civil_boq.page_elements.masonary_work import masonary_work
from modules.civil_boq.page_elements.price_setting import set_price
from modules.civil_boq.page_elements.tiles_work import tiles_work
from modules.civil_boq.page_elements.basic_details import basic_details
from modules.civil_boq.calculations.concrete_calculator import concrete_calculator

st.header("BOQ Generator")
# st.write(st.session_state)
st.divider()
basic_details()
set_price()
concrete_work()
masonary_work()
door_window_work()
tiles_work()

st.divider()
generate, print, clear, finalize = st.columns(4)
 
if st.button("Generate BOQ", type="primary", key="generate_btn_poq_page_end"):
    concrete_calculator()
    masonary_calculator()
    st.switch_page("modules/civil_boq/pages/print_page.py")

