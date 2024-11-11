import streamlit as st
import pandas as pd

def plumbing_work():
    plumbing_work_expander =  st.expander("Plumbing Work", expanded= False, icon=":material/star:")
    if plumbing_work_expander:
        # plumbing_work_expander.markdown("##### Enter tiles area in square feet")
        plumbing_work_form = plumbing_work_expander.form(key="plumbing_work_form")
        tiles_work_form_container = plumbing_work_form.container(border=True)  

        items_list = ["Sink", "Faucet","Wash Basin","Shower Head","Bath Tub","Toilet Commode","Towel Bars","Taps","Water Tank","Geyser", "Water Purifier", "Fountain", "Swimming Pool","plumbing_work_cost"]

        def store_values(pop=True):
                values_list = [st.session_state["Sink"], st.session_state["Faucet"],st.session_state["Wash Basin"],st.session_state["Shower Head"],st.session_state["Bath Tub"],st.session_state["Toilet Commode"],st.session_state["Towel Bars"],st.session_state["Taps"],st.session_state["Water Tank"],st.session_state["Geyser"], st.session_state["Water Purifier"], st.session_state["Fountain"], st.session_state["Swimming Pool"],st.session_state["plumbing_work_cost"]]
                plumbing_widgets_df = pd.DataFrame({"Item": items_list,
                                  "Quantity": values_list,
                                  })
                plumbing_widgets_df.set_index("Item", inplace=True)
                st.session_state.plumbing_widgets_df = plumbing_widgets_df
                if pop:
                    st.toast("Done!", icon="👍")
        def load_values(items_list):
                for item in items_list:
                     st.session_state[item] = st.session_state.plumbing_widgets_df.loc[item]["Quantity"]

        if "plumbing_widgets_df" in st.session_state:
                load_values(items_list)   

        col1, col2, col3, col4, col5, col6 = plumbing_work_form.columns(6)

        selected_sink = col1.number_input("Sink", min_value=0, max_value=10000, step=1, key="Sink")
        selected_faucet = col2.number_input("Faucet", min_value=0, max_value=10000, step=1, key="Faucet")
        selected_wash_basin = col3.number_input("Wash Basin", min_value=0, max_value=10000, step=1, key="Wash Basin")
        selected_shower_head = col4.number_input("Shower Heads", min_value=0, max_value=10000, step=1, key="Shower Head")
        selected_bath_tub = col5.number_input("Bath Tub", min_value=0, max_value=10000, step=1, key="Bath Tub")                
        selected_toilet_commode = col6.number_input("Toilet Commode", min_value=0, max_value=10000, step=1, key="Toilet Commode")
        selected_towel_bars = col1.number_input("Towel Bar/Ring", min_value=0, max_value=10000, step=1, key="Towel Bars")                        
        selected_taps = col2.number_input("Taps", min_value=0, max_value=10000, step=1, key="Taps")
        selected_water_tank = col3.number_input("Water Tank", min_value=0, max_value=10000, step=1, key="Water Tank")
        selected_geyser = col4.number_input("Geyser", min_value=0, max_value=10000, step=1, key="Geyser")
        selected_purifier = col5.number_input("Water Purifier", min_value=0, max_value=10000, step=1, key="Water Purifier")    
        selected_fountain  = col6.number_input("Water Fountain", min_value=0, max_value=10000, step=1, key="Fountain")  
        selected_pool  = col1.number_input("Swimming Pool", min_value=0, max_value=10000, step=1, key="Swimming Pool")         
        col1.write("")
        plumbing_work_cost = plumbing_work_form.number_input("Total Cost of Plumbing work including meterial and labour", min_value=0, max_value=10000000, step=1000, key="plumbing_work_cost")
        # plumbing_work_form.form_submit_button(label="Update", on_click=store_values)


        # store_edited_df()
        store_values(False)
        plumbing_work_form.form_submit_button(label="Save",  on_click=store_values, type="primary")
 