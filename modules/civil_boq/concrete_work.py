import pandas as pd
from modules.civil_boq.create_concrete_df import create_df

def concrete_work(st):
    concrete_expander =  st.expander("Concrete Work", expanded= False, icon=":material/currency_rupee_circle:")
    if concrete_expander:
            concrete_from = concrete_expander.form(key="concrete_from")
            cement_grade = ["M20", "M25", "M40", "M50"]
            cement_grade_choide = concrete_from.selectbox("Concrete Grade", cement_grade, )
            concrete_Items = ["Footing", "Column", "Beam", "Wall Footing", "Floor Slab", "Stairs"]
            concrete_expander_container = concrete_from.container(border=True)    
            Footing, Column, Beam, Wall_Footing  = concrete_expander_container.columns(4)    
            Floor_Slab, Stairs, future1, future2 = concrete_expander_container.columns(4)   
            # with Footing:        
                # selected_Footing_count = st.number_input("Footing",  min_value=0, max_value=100,)
            selected_Footing_count = Footing.number_input("Footing",  min_value=0, max_value=100,)    
            with Column:        
                selected_Column_count = st.number_input("Column",  min_value=0, max_value=100,)
            with Beam:        
                selected_Beam_count = st.number_input("Beam",  min_value=0, max_value=100,)
            with Wall_Footing:        
                selected_Wall_Footing_count = st.number_input("Wall Footing",  min_value=0, max_value=25,)
            with Floor_Slab:        
                selected_Floor_Slab_count = st.number_input("Floor Slab",  min_value=0, max_value=25,)
            with Stairs:        
                selected_Stairs_count = st.number_input("Stairs",  min_value=0, max_value=25,)
            def display_header_row():
                cancrete_size_lable_container = concrete_from.container(border=True)
                item_column, length_column, width_column, height_column = cancrete_size_lable_container.columns(4)
                item_column.write("Item")
                length_column.write("Length")
                width_column.write("Width")
                height_column.write("Height")
            concrete_from.form_submit_button(label="Update")
            

            footing_df = pd.DataFrame()
            column_df = pd.DataFrame()
            beam_df = pd.DataFrame()
            wall_footing_df = pd.DataFrame()
            floor_slab_df = pd.DataFrame()
            stairs_df = pd.DataFrame()
            concrete_work_df = pd.DataFrame()


            if selected_Footing_count > 0:
                    footing_df = create_df(df_name="concrete_work_df",item="Footing", count=selected_Footing_count)                
            if selected_Column_count > 0:
                    column_df = create_df(df_name="concrete_work_df",item="Column", count=selected_Column_count)                
            if selected_Beam_count > 0:
                    beam_df = create_df(df_name="concrete_work_df",item="Beam", count=selected_Beam_count)
            if selected_Wall_Footing_count > 0:
                    wall_footing_df = create_df(df_name="concrete_work_df",item="Wall Footing", count=selected_Wall_Footing_count)
            if selected_Floor_Slab_count > 0:
                    floor_slab_df = create_df(df_name="concrete_work_df",item="Floor Slab", count=selected_Floor_Slab_count)
            if selected_Stairs_count > 0:
                    stairs_df = create_df(df_name="concrete_work_df",item="Stairs", count=selected_Stairs_count)

            def store_edited_df():  
                st.session_state["concrete_work_df"] = concrete_work_df     
                # concrete_from.write(st.session_state)
                    

            if selected_Footing_count | selected_Column_count | selected_Beam_count | selected_Wall_Footing_count | selected_Floor_Slab_count | selected_Stairs_count > 0:
                #     display_header_row()
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
                        required=False,            ),                           
                },)
                    concrete_from.form_submit_button(label="Save")
                    store_edited_df()
