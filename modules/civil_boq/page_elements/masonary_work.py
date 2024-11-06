    
from modules.civil_boq.page_elements.create_masonary_df import create_df
import pandas as pd
import streamlit as st

def masonary_work():
    masonary_expander =  st.expander("Masonary Work & Plastering", expanded= False, icon=":material/star:")
    if masonary_expander:
            masonary_from = masonary_expander.form(key="masonary_from")
            masonary_expander_container = masonary_from.container(border=True)    
            brick_size_list = ["9 x 4 x 3", "9.1 x 4.3 x 2.8", "12 x 8 x 6"]
            wall_thickness_list = [4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
            plasteringSize = ["12 mm", "15 mm", "18 mm"]
            cement_ratio_list = ["1:5", "1:4", "1:3", "1:2"]
            def store_values():
                values = st.session_state.m_selected_walls_count
                masonary_widgets_df = pd.DataFrame({"Item": ["m_selected_walls_count"],
                                  "Value": [values],
                                  })
                masonary_widgets_df.set_index("Item", inplace=True)
                st.session_state.masonary_widgets_df = masonary_widgets_df

            def load_values():
                st.session_state["m_selected_walls_count"] = st.session_state.masonary_widgets_df.loc["m_selected_walls_count"]["Value"]

            if "masonary_widgets_df" in st.session_state:
                load_values()    


            Walls, futurem1, futurem2, futurem3  = masonary_expander_container.columns(4) 
            with Walls:        
                selected_Walls_count = st.number_input("Wall(s)",  min_value=0, max_value=25, key="m_selected_walls_count")

            masonary_from.form_submit_button(label="Update", on_click=store_values)


            if selected_Walls_count > 0:
                    for i in range(selected_Walls_count):
                            final_df = create_df(df_name="masonary_work_df", item="Wall", count=selected_Walls_count)
                    final_df.set_index("Item",inplace=True)
                    masonary_work_df = masonary_from.data_editor(final_df, use_container_width=True, column_config={
                    "Brick size": st.column_config.SelectboxColumn(
                        "Brick size",
                        help="select brick size",
                        width="medium",
                        options=brick_size_list,
                        required=True,
                        
                    ),
                    "Cement ratio": st.column_config.SelectboxColumn(
                        "Cement ratio",
                        help="select Cement ratio",
                        width="medium",
                        options=cement_ratio_list,
                        required=True,            ),      
                    "Plastering thickness": st.column_config.SelectboxColumn(
                        "Plastering thickness",
                        help="select Plastering thickness",
                        width="medium",
                        options=plasteringSize,
                        required=True,          ),      
                    "Wall thickness(inch)": st.column_config.SelectboxColumn(
                        "Wall thickness(inch)",
                        help="select wall thickness",
                        width="medium",
                        options=wall_thickness_list,
                        
                        required=True,          ),                          
                                                               
                    },)
                    if masonary_from.form_submit_button(label="Save "):
                        st.session_state["masonary_work_df"] = masonary_work_df 
                        st.toast("Done!", icon="👍")