import streamlit as st
import pandas as pd

def plumbing_work():
    plumbing_work_expander =  st.expander("Plumbing Work", expanded= False, icon=":material/star:")
    if plumbing_work_expander:
        # plumbing_work_expander.markdown("##### Enter tiles area in square feet")
        plumbing_work_form = plumbing_work_expander.form(key="plumbing_work_form")
        tiles_work_form_container = plumbing_work_form.container(border=True)  

        items_list = ["selected_sink", "selected_faucet","selected_wash_basin","selected_shower_head","selected_bath_tub","selected_toilet_commode","selected_towel_bars","selected_taps","selected_water_tank","selected_geyser", "selected_purifier", "selected_fountain", "selected_pool","plumbing_work_cost"]

        def store_values():
                values_list = [st.session_state.selected_sink,st.session_state.selected_faucet,st.session_state.selected_wash_basin,st.session_state.selected_shower_head,st.session_state.selected_bath_tub,st.session_state.selected_toilet_commode,st.session_state.selected_towel_bars,st.session_state.selected_taps,st.session_state.selected_water_tank, st.session_state.selected_geyser, st.session_state.selected_purifier, st.session_state.selected_fountain, st.session_state.selected_pool,st.session_state.plumbing_work_cost]
                plumbing_widgets_df = pd.DataFrame({"Item": items_list,
                                  "Value": values_list,
                                  })
                plumbing_widgets_df.set_index("Item", inplace=True)
                st.session_state.plumbing_widgets_df = plumbing_widgets_df

        def load_values(items_list):
                for item in items_list:
                     st.session_state[item] = st.session_state.plumbing_widgets_df.loc[item]["Value"]

        if "plumbing_widgets_df" in st.session_state:
                load_values(items_list)   

        col1, col2, col3, col4, col5, col6 = plumbing_work_form.columns(6)

        selected_sink = col1.number_input("Sink", min_value=0, max_value=10000, step=1, key="selected_sink")
        selected_faucet = col2.number_input("Faucet", min_value=0, max_value=10000, step=1, key="selected_faucet")
        selected_wash_basin = col3.number_input("Wash Basin", min_value=0, max_value=10000, step=1, key="selected_wash_basin")
        selected_shower_head = col4.number_input("Shower Heads", min_value=0, max_value=10000, step=1, key="selected_shower_head")
        selected_bath_tub = col5.number_input("Bath Tub", min_value=0, max_value=10000, step=1, key="selected_bath_tub")                
        selected_toilet_commode = col6.number_input("Toilet Commode", min_value=0, max_value=10000, step=1, key="selected_toilet_commode")
        selected_towel_bars = col1.number_input("Towel Bar/Ring", min_value=0, max_value=10000, step=1, key="selected_towel_bars")                        
        selected_taps = col2.number_input("Taps", min_value=0, max_value=10000, step=1, key="selected_taps")
        selected_water_tank = col3.number_input("Water Tank", min_value=0, max_value=10000, step=1, key="selected_water_tank")
        selected_geyser = col4.number_input("Geyser", min_value=0, max_value=10000, step=1, key="selected_geyser")
        selected_purifier = col5.number_input("Water Purifier", min_value=0, max_value=10000, step=1, key="selected_purifier")    
        selected_fountain  = col6.number_input("Water Fountain", min_value=0, max_value=10000, step=1, key="selected_fountain")  
        selected_pool  = col1.number_input("Swimming Pool", min_value=0, max_value=10000, step=1, key="selected_pool")         
        col1.write("")
        plumbing_work_cost = plumbing_work_form.number_input("Total Cost of Plumbing work including meterial and labour", min_value=0, max_value=10000000, step=1000, key="plumbing_work_cost")
        # plumbing_work_form.form_submit_button(label="Update", on_click=store_values)


        # store_edited_df()
        if plumbing_work_form.form_submit_button(label="Save"):
            store_values()
            st.toast("Done!", icon="👍")        