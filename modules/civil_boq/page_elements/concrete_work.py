import pandas as pd
import streamlit as st
from modules.civil_boq.page_elements.create_concrete_df import create_df

def concrete_work():
    concrete_expander =  st.expander("Concrete Work", expanded= False, icon=":material/currency_rupee_circle:")
    if concrete_expander:
            concrete_from = concrete_expander.form(key="concrete_widget_from")
            items_list = ["selected_Footing_count", "selected_Column_count","selected_Beam_count","selected_Wall_Footing_count","selected_Floor_Slab_count","selected_Stairs_count"]      
            concrete_grade = ["M20", "M25"]
            def store_values():
                values_list = [st.session_state.selected_Footing_count,st.session_state.selected_Column_count,st.session_state.selected_Beam_count,st.session_state.selected_Wall_Footing_count,st.session_state.selected_Floor_Slab_count,st.session_state.selected_Stairs_count ]
                concrete_widgets_df = pd.DataFrame({"Item": items_list,
                                  "Value": values_list,
                                  })
                concrete_widgets_df.set_index("Item", inplace=True)
                st.session_state.concrete_widgets_df = concrete_widgets_df


            def load_widget_values(items_list):
                for item in items_list:
                     st.session_state[item] = st.session_state.concrete_widgets_df.loc[item]["Value"]

            def store_edited_df():  
                st.session_state.concrete_work_df = concrete_work_df 
 

            if "concrete_widgets_df" in st.session_state:
                load_widget_values(items_list)  
           
            Footing, Column, Beam, Wall_Footing  = concrete_from.columns(4)    
            Floor_Slab, Stairs, future1, future2 = concrete_from.columns(4) 

            selected_Footing_count = Footing.number_input("Footing",  min_value=0, max_value=100,key="selected_Footing_count")     
            selected_Column_count = Column.number_input("Column",  min_value=0, max_value=100, key="selected_Column_count")  
            selected_Beam_count = Beam.number_input("Beam",  min_value=0, max_value=100,key="selected_Beam_count")     
            selected_Wall_Footing_count = Wall_Footing.number_input("Wall Footing",  min_value=0, max_value=25,key="selected_Wall_Footing_count")  
            selected_Floor_Slab_count = Floor_Slab.number_input("Floor Slab",  min_value=0, max_value=25,key="selected_Floor_Slab_count")  
            selected_Stairs_count = Stairs.number_input("Stairs",  min_value=0, max_value=25,key="selected_Stairs_count")
            
            concrete_from.form_submit_button(label="Update",on_click=store_values)
            
            footing_df = create_df(df_name="concrete_work_df",item="Footing", count=selected_Footing_count)                
            column_df = create_df(df_name="concrete_work_df",item="Column", count=selected_Column_count)                
            beam_df = create_df(df_name="concrete_work_df",item="Beam", count=selected_Beam_count)
            wall_footing_df = create_df(df_name="concrete_work_df",item="Wall Footing", count=selected_Wall_Footing_count)
            floor_slab_df = create_df(df_name="concrete_work_df",item="Floor Slab", count=selected_Floor_Slab_count)
            stairs_df = create_df(df_name="concrete_work_df",item="Stairs", count=selected_Stairs_count)                  

            if selected_Footing_count | selected_Column_count | selected_Beam_count | selected_Wall_Footing_count | selected_Floor_Slab_count | selected_Stairs_count > 0:
                    final_df = pd.concat([footing_df,column_df,beam_df,wall_footing_df,floor_slab_df,stairs_df],ignore_index=True)
                    final_df.set_index("Item",inplace=True)
                    concrete_work_df = concrete_from.data_editor(final_df, use_container_width=True, column_config={
                    "Rod size": st.column_config.SelectboxColumn(
                        "Rod size",
                        help="select rod size",
                        width="medium",
                        options=[ "10 mm","12 mm","16 mm","20 mm", "25 mm", "35 mm", "10 mm & 12 mm", "12 mm & 16 mm", "16 mm & 20 mm", "20 mm & 25 mm"],
                        required=True,
                        
                    ),
                    "Rod count": st.column_config.SelectboxColumn(
                        "Rod count",
                        help="select rod count",
                        width="medium",
                        options=[ "4","6","8", "10","12","14","18","20","2 + 4", "4 + 4", "4 + 6", "5 + 5","6 + 6", "8 + 8", "9 + 9", "10 + 10"],
                        required=True,            ),      
                    "Ring size": st.column_config.SelectboxColumn(
                        "Ring size (optional)",
                        help="select rod size",
                        width="medium",
                        options=[ "6 mm","8 mm", "10 mm","12 mm",],
                        required=False,          ),      
                    "Grade": st.column_config.SelectboxColumn(
                        "Grade",
                        help="select grade",
                        width="medium",
                        options= concrete_grade,
                        required=False,          ),                                                  
                    },)
                    # st.session_state.concrete_work_df = concrete_work_df

                    if concrete_from.form_submit_button(label="Save"):
                        store_edited_df()
                        st.toast("Done!", icon="👍")

