import pandas as pd
import streamlit as st
from modules.civil_boq.page_elements.create_doors_df import create_doors_df
from modules.civil_boq.page_elements.create_widows_df import create_windows_df


def door_window_work():
    door_window_expander =  st.expander("Doors & Windows", expanded= False, icon=":material/currency_rupee_circle:")
    if door_window_expander:
        door_window_form = door_window_expander.form(key="door_window_form")
        door_window_form_container = door_window_form.container(border=True)
        door_name_list = ["Main door","Kitchen door","Study room","Toilet door", "Bedroom door", "Utility door", "Balcony door", "Head room door", "Pooja door", "Other"]
        door_type_list = ["PVC", "UPVC", "Wooden", "MDF", "Aluminium", "Glass", "Flush", "Steel"]
        rooms_list = ["Living Room","Bed Room","Kitchen","Dining","Toilet","Balcony","Study Room","Utility Room", "Theatre Room", "Head Room", "Other"]
        add_doors, add_windows, future2, future3 = door_window_form.columns(4)

        items_list = ["selected_doors_count", "selected_windows_count"]

        def store_values():
            values_list = [st.session_state.selected_doors_count,st.session_state.selected_windows_count]
            doors_widgets_df = pd.DataFrame({"Item": items_list,
                                "Value": values_list,
                                  })
            doors_widgets_df.set_index("Item", inplace=True)
            st.session_state.doors_widgets_df = doors_widgets_df


        def load_values(items_list):
            for item in items_list:
                st.session_state[item] = st.session_state.doors_widgets_df.loc[item]["Value"]

        if "doors_widgets_df" in st.session_state:
            load_values(items_list)   



        selected_doors_count = add_doors.number_input("Add Doors", min_value=0, max_value=100, key="selected_doors_count")
        selected_windows_count = add_windows.number_input("Add Windows", min_value=0, max_value=100, key="selected_windows_count" )
        door_window_form.form_submit_button(label="Update", on_click=store_values)

        def store_doors_edited_df():  
                st.session_state["door_work_df"] = door_work_df     

        if selected_doors_count | selected_windows_count > 0:
            final_doors_df = create_windows_df(df_name="door_work_df", item="Door", count=selected_doors_count)
            final_windows_df = create_windows_df(df_name="window_work_df", item="Window", count=selected_windows_count)
            final_df = pd.concat([final_doors_df,final_windows_df])
            final_df.set_index("Item",inplace=True)
            door_work_df = door_window_form.data_editor(final_df, use_container_width=True, column_config={
                        "Room": st.column_config.SelectboxColumn(
                            "Room",
                            help="select Room",
                            width="medium",
                            options=rooms_list,
                            required=True,
                            
                        ),
                        "Type": st.column_config.SelectboxColumn(
                            "Type",
                            help="select meterial",
                            width="medium",
                            options=door_type_list,
                            required=True,            ),      
                        
                    },)
            if door_window_form.form_submit_button(label="Save "):
                store_doors_edited_df()        
                st.toast("Done!", icon="👍")
  