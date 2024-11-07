
import streamlit as st

from modules.civil_boq.calculations.masonary_calculator import masonary_calculator
from modules.civil_boq.calculations.tiles_calculator import tiles_cost_calculator
from modules.civil_boq.page_elements.concrete_work import concrete_work
from modules.civil_boq.page_elements.doors_windows import door_window_work
from modules.civil_boq.page_elements.electrical_work import electrical_work
from modules.civil_boq.page_elements.masonary_work import masonary_work
from modules.civil_boq.page_elements.other_work import other_work
from modules.civil_boq.page_elements.painting_work import painting_work
from modules.civil_boq.page_elements.plumbing_work import plumbing_work
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
electrical_work()
plumbing_work()
painting_work()
other_work()

st.divider()
generate, print, clear, finalize = st.columns(4)


if st.button("Generate BOQ", type="primary", key="generate_btn_poq_page_end"):
    concrete_calculator()
    masonary_calculator()  
    tiles_cost_calculator()
    # st.session_state.concrete_work_df.to_csv("C:\\work\\Streamlit_Code\\Streamlit\\test.csv")
    st.switch_page("modules/civil_boq/pages/print_page.py")


