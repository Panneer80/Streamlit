import pandas as pd

from modules.civil_boq.create_doors_df import create_doors_df
from modules.civil_boq.create_widows_df import create_windows_df


def door_window_work(st):
    door_window_expander =  st.expander("Doors & Windows", expanded= False, icon=":material/currency_rupee_circle:")
    if door_window_expander:
        door_window_form = door_window_expander.form(key="door_window_form")
        door_window_form_container = door_window_form.container(border=True)
        door_name_list = ["Main door","Toilet door", "Bedroom door", "Utility door", "Balcony door", "Head room door", "Pooja door", "other door"]
        door_type_list = ["PVC", "UPVC", "Wooden", "MDF", "Aluminium", "Glass", "Flush", "Steel"]
        add_doors, add_windows, future2, future3 = door_window_form.columns(4)
        selected_doors_count = add_doors.number_input("Add Doors", min_value=0, max_value=100)
        selected_windows_count = add_windows.number_input("Add Windows", min_value=0, max_value=100)
        door_window_form.form_submit_button(label="Update")

        door_work_df = pd.DataFrame()      
        window_work_df = pd.DataFrame()   
        def store_doors_edited_df():  
                st.session_state["door_work_df"] = door_work_df     
                # concrete_from.write(st.session_state)
        def store_windows_edited_df():  
                st.session_state["window_work_df"] = window_work_df   
                # concrete_from.write(st.session_state)
        if selected_doors_count > 0:
            for i in range(selected_doors_count):
                        # display_input_row("Wall",i)
                final_doors_df = create_doors_df(df_name="door_work_df", item="Door", count=selected_doors_count)
            final_doors_df.set_index("Item",inplace=True)
            door_work_df = door_window_form.data_editor(final_doors_df, use_container_width=True)
            # door_window_form.form_submit_button(label="Save ")
            store_doors_edited_df()        

        if selected_windows_count > 0:
            for i in range(selected_windows_count):
                        # display_input_row("Wall",i)
                final_windows_df = create_windows_df(df_name="window_work_df", item="Window", count=selected_windows_count)
            final_windows_df.set_index("Item",inplace=True)
            window_work_df = door_window_form.data_editor(final_windows_df, use_container_width=True)
            door_window_form.form_submit_button(label="Save ")
            store_windows_edited_df()   