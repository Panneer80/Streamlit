import streamlit as st
import pandas as pd

def basic_details():
    container = st.expander(label="Basic Details", expanded=True, icon=":material/star:")
    basic_form = container.form("basic_info")
    col1, col2, col3= basic_form.columns(3)
    items_list = ["prepared_by","project_location","project_type","prapared_date","builtup_area"]

    def store_values():
        df = pd.DataFrame({"Item":items_list,
                           "Value":[st.session_state.prepared_by, st.session_state.project_location, st.session_state.project_type, st.session_state.prapared_date, st.session_state.builtup_area]})
        df.set_index("Item", inplace=True)
        st.session_state.basic_details_df = df
        st.toast("Done!", icon="👍")

    def load_values(items_list):
        for item in items_list:
            st.session_state[item] = st.session_state.basic_details_df.loc[item]["Value"]

    if "basic_details_df" in st.session_state:
        load_values(items_list)   

    with col1:
        st.text_input( "Prapared By",  key="prepared_by") 
        st.text_input( "Project Location",  key="project_location")
    with col2:
        st.selectbox( "Project Type", ["Residential Building", "Commercial Building"], key="project_type")
        
        st.date_input( "Date", key="prapared_date") 
    with col3:
        st.number_input(label="Builtup Area (Sq.ft)",  min_value=100, max_value=100000, step=100, key="builtup_area")

    basic_form.form_submit_button(label="Save", on_click=store_values)

    