import streamlit as st
import pandas as pd



def other_work():
    other_work_expander = st.expander("Other cost (optional)", icon=":material/star:")
    if other_work_expander:
        other_work_container = other_work_expander.form("other_work_df_form")
       

        if "saved_other_work_df" not in st.session_state:        
            items_list = ["Drawing","Consultation","Paper Work","Builder Charges","Enter here","Enter here","Enter here"]
            values_list = ["Description","Description","Description","Description","Description","Description","Description"]
            cost_list = [0,0,0,0,0,0,0]    
            other_work_df = pd.DataFrame({"Item Name": items_list,
                                        "Description": values_list,
                                        "Cost": cost_list
                                        })
            other_work_df.set_index("Item Name", inplace=True)

            edited_other_work_df = other_work_container.data_editor(other_work_df, use_container_width=True) 
        else:
            edited_other_work_df = other_work_container.data_editor(st.session_state.saved_other_work_df, use_container_width=True)
        if other_work_container.form_submit_button(label="Save", type="primary"):
            st.session_state.saved_other_work_df = edited_other_work_df
