import streamlit as st
import pandas as pd

def electrical_work():
    electrical_work_expander =  st.expander("Electrical Work", expanded= False, icon=":material/star:")
    if electrical_work_expander:
        electrical_work_form = electrical_work_expander.form(key="electrical_work_form")
        col1, col2, col3, col4, col5, col6 = electrical_work_form.columns(6)
        items_list = ["Light Points", "Fan Points","AC Points","UPS Points","5A Sockets","16A Sockets","20A Sockets","CCTV Points","Solar Points","EV Points","electrical_work_cost"]
        
        def store_values(pop=True):
                values_list = [st.session_state["Light Points"], st.session_state["Fan Points"],st.session_state["AC Points"],st.session_state["UPS Points"],st.session_state["5A Sockets"],st.session_state["16A Sockets"],st.session_state["20A Sockets"],st.session_state["CCTV Points"],st.session_state["Solar Points"],st.session_state["EV Points"],st.session_state["electrical_work_cost"]]
                electrical_widgets_df = pd.DataFrame({"Item": items_list,
                                  "Quantity": values_list,
                                  })
                electrical_widgets_df.set_index("Item", inplace=True)
                st.session_state.electrical_widgets_df = electrical_widgets_df
                if pop:
                    st.toast("Done!", icon="👍")

        def load_values(items_list):
                for item in items_list:
                     st.session_state[item] = st.session_state.electrical_widgets_df.loc[item]["Quantity"]


        if "electrical_widgets_df" in st.session_state:
                load_values(items_list)  
 

        with col1:
                selected_light_points = st.number_input("Light Points", min_value=0, max_value=10000, step=1, key="Light Points")
                selected_20a_sockets = st.number_input("20A Sockets", min_value=0, max_value=10000, step=1, key="20A Sockets")
                st.write("")
        with col2:
                selected_fan_points = st.number_input("Fan Points", min_value=0, max_value=10000, step=1, key="Fan Points")
                selected_cctv_points = st.number_input("CCTV points", min_value=0, max_value=10000, step=1, key="CCTV Points")        
        with col3:
                selected_ac_points = st.number_input("AC Points", min_value=0, max_value=10000, step=1, key="AC Points")
                selected_solar_points = st.number_input("Solar Points", min_value=0, max_value=10000, step=1, key="Solar Points")
        with col4:
                selected_ups_points = st.number_input("UPS Points", min_value=0, max_value=10000, step=1, key="UPS Points")
                selected_ev_points = st.number_input("EV Charging Point", min_value=0, max_value=10000, step=1, key="EV Points")
        with col5:        
                selected_5a_sockets = st.number_input("5A Sockets", min_value=0, max_value=10000, step=1, key="5A Sockets")                
        with col6:
                selected_16a_sockets = st.number_input("16A Sockets", min_value=0, max_value=10000, step=1, key="16A Sockets")

        electrical_work_cost = electrical_work_form.number_input("Total Cost of Electrical work including meterial and labour", min_value=0, max_value=10000000, step=1000, key="electrical_work_cost")
        # electrical_work_form.form_submit_button(label="Update", on_click=store_values)

        store_values(False)
        electrical_work_form.form_submit_button(label="Save", on_click=store_values, type="primary")
   