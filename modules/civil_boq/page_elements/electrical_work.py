import streamlit as st
import pandas as pd

def electrical_work():
    electrical_work_expander =  st.expander("Electrical Work", expanded= False, icon=":material/star:")
    if electrical_work_expander:
        # electrical_work_expander.markdown("##### Enter tiles area in square feet")
        electrical_work_form = electrical_work_expander.form(key="electrical_work_form")
        electrical_work_form_container = electrical_work_form.container(border=True)  

        items_list = ["selected_light_points", "selected_fan_points","selected_ac_points","selected_ups_points","selected_5a_sockets","selected_16a_sockets","selected_20a_sockets","selected_cctv_points","selected_solar_points","selected_ev_points","electrical_work_cost"]

        def store_values():
                values_list = [st.session_state.selected_light_points,st.session_state.selected_fan_points,st.session_state.selected_ac_points,st.session_state.selected_ups_points,st.session_state.selected_5a_sockets,st.session_state.selected_16a_sockets,st.session_state.selected_20a_sockets,st.session_state.selected_cctv_points,st.session_state.selected_solar_points, st.session_state.selected_ev_points, st.session_state.electrical_work_cost]
                electrical_widgets_df = pd.DataFrame({"Item": items_list,
                                  "Value": values_list,
                                  })
                electrical_widgets_df.set_index("Item", inplace=True)
                st.session_state.electrical_widgets_df = electrical_widgets_df

        def load_values(items_list):
                for item in items_list:
                     st.session_state[item] = st.session_state.electrical_widgets_df.loc[item]["Value"]

        if "electrical_widgets_df" in st.session_state:
                load_values(items_list)   

        col1, col2, col3, col4, col5, col6 = electrical_work_form.columns(6)

        selected_light_points = col1.number_input("Light Points", min_value=0, max_value=10000, step=1, key="selected_light_points")
        selected_fan_points = col2.number_input("Fan Points", min_value=0, max_value=10000, step=1, key="selected_fan_points")
        selected_ac_points = col3.number_input("AC Points", min_value=0, max_value=10000, step=1, key="selected_ac_points")
        selected_ups_points = col4.number_input("UPS Points", min_value=0, max_value=10000, step=1, key="selected_ups_points")
        selected_5a_sockets = col5.number_input("5A Sockets", min_value=0, max_value=10000, step=1, key="selected_5a_sockets")                
        selected_16a_sockets = col6.number_input("16A Sockets", min_value=0, max_value=10000, step=1, key="selected_16a_sockets")
        selected_20a_sockets = col1.number_input("20A Sockets", min_value=0, max_value=10000, step=1, key="selected_20a_sockets")                        
        selected_cctv_points = col2.number_input("CCTV points", min_value=0, max_value=10000, step=1, key="selected_cctv_points")
        selected_solar_points = col3.number_input("Solar Points", min_value=0, max_value=10000, step=1, key="selected_solar_points")
        selected_ev_points = col4.number_input("EV Charging Point", min_value=0, max_value=10000, step=1, key="selected_ev_points")
        col1.write("")
        electrical_work_cost = electrical_work_form.number_input("Total Cost of Electrical work including meterial and labour", min_value=0, max_value=10000000, step=1000, key="electrical_work_cost")
        # electrical_work_form.form_submit_button(label="Update", on_click=store_values)


        # store_edited_df()
        if electrical_work_form.form_submit_button(label="Save"):
            store_values()
            st.toast("Done!", icon="👍")        