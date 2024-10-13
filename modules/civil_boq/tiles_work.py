import pandas as pd

from modules.civil_boq.create_tiles_df import create_df



def tiles_work(st):
    tiles_work_expander =  st.expander("Tiles Work", expanded= False, icon=":material/currency_rupee_circle:")
    if tiles_work_expander:
        tiles_work_expander.markdown("##### Enter tiles area in square feet")
        tiles_work_form = tiles_work_expander.form(key="tiles_work_form")
        tiles_work_form_container = tiles_work_form.container(border=True)        
        floor_tiles, wall_tiles, exterior_tiles, bathroom_tiles, parking_tiles = tiles_work_form_container.columns(5)
        selected_floor_tiles = floor_tiles.number_input("Floor tiles (Sq.ft)", min_value=0, max_value=10000)
        selected_wall_tiles = wall_tiles.number_input("Wall tiles (Sq.ft)", min_value=0, max_value=10000)
        selected_exterior_tiles = exterior_tiles.number_input("Exterior tiles (Sq.ft)", min_value=0, max_value=10000)
        selected_bathroom_tiles = bathroom_tiles.number_input("Bathroom tiles (Sq.ft)", min_value=0, max_value=10000)
        selected_parking_tiles = parking_tiles.number_input("Parking tiles (Sq.ft)", min_value=0, max_value=10000)                
        tiles_work_form_container.form_submit_button(label="Update")


        tiles_work_df = pd.DataFrame()  
        floor_df = pd.DataFrame()
        wall_df = pd.DataFrame()
        exterior_df = pd.DataFrame()
        bathrrom_df = pd.DataFrame()
        parking_df = pd.DataFrame() 


        if selected_floor_tiles > 0:
                floor_df = create_df(df_name="tiles_work_df",item="Floor Tiles", count=selected_floor_tiles)                
        if selected_wall_tiles > 0:
                wall_df = create_df(df_name="tiles_work_df",item="Wall Tiles", count=selected_wall_tiles)                
        if selected_exterior_tiles > 0:
                exterior_df = create_df(df_name="tiles_work_df",item="Exterior Tiles", count=selected_exterior_tiles)
        if selected_bathroom_tiles > 0:
                bathrrom_df = create_df(df_name="tiles_work_df",item="Bathroom Tiles", count=selected_bathroom_tiles)
        if selected_parking_tiles > 0:
                parking_df = create_df(df_name="tiles_work_df",item="Parking Tiles", count=selected_parking_tiles)

        def store_edited_df():  
            st.session_state["tiles_work_df"] = tiles_work_df     

        if selected_floor_tiles | selected_wall_tiles | selected_exterior_tiles | selected_bathroom_tiles | selected_parking_tiles > 0:
                #     display_header_row()
                    final_df = pd.concat([floor_df,wall_df,exterior_df,bathrrom_df,parking_df],ignore_index=True)
                    final_df.set_index("Item",inplace=True)
                    tiles_work_df = tiles_work_form.data_editor(final_df, use_container_width=True)
                    tiles_work_form.form_submit_button(label="Save")
                    store_edited_df()