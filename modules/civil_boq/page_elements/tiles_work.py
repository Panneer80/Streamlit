import pandas as pd
import streamlit as st
from modules.civil_boq.page_elements.create_tiles_df import create_df



def tiles_work():
    tiles_work_expander =  st.expander("Tiles Work", expanded= False, icon=":material/currency_rupee_circle:")
    if tiles_work_expander:
        tiles_work_expander.markdown("##### Enter tiles area in square feet")
        tiles_work_form = tiles_work_expander.form(key="tiles_work_form")
        tiles_work_form_container = tiles_work_form.container(border=True)        


        items_list = ["selected_floor_tiles", "selected_wall_tiles","selected_exterior_tiles","selected_bathroom_tiles","selected_parking_tiles","selected_roof_tiles"]

        def store_values():
                values_list = [st.session_state.selected_floor_tiles,st.session_state.selected_wall_tiles,st.session_state.selected_exterior_tiles,st.session_state.selected_bathroom_tiles,st.session_state.selected_parking_tiles,st.session_state.selected_roof_tiles ]
                tiles_widgets_df = pd.DataFrame({"Item": items_list,
                                  "Value": values_list,
                                  })
                tiles_widgets_df.set_index("Item", inplace=True)
                st.session_state.tiles_widgets_df = tiles_widgets_df

        def load_values(items_list):
                for item in items_list:
                     st.session_state[item] = st.session_state.tiles_widgets_df.loc[item]["Value"]

        if "tiles_widgets_df" in st.session_state:
                load_values(items_list)   

        floor_tiles, wall_tiles, exterior_tiles, bathroom_tiles, parking_tiles, roof_tiles = tiles_work_form.columns(6)

        selected_floor_tiles = floor_tiles.number_input("Floor tiles (Sq.ft)", min_value=0, max_value=10000, step=100, key="selected_floor_tiles")
        selected_wall_tiles = wall_tiles.number_input("Wall tiles (Sq.ft)", min_value=0, max_value=10000, step=100, key="selected_wall_tiles")
        selected_exterior_tiles = exterior_tiles.number_input("Exterior tiles (Sq.ft)", min_value=0, max_value=10000, step=100, key="selected_exterior_tiles")
        selected_bathroom_tiles = bathroom_tiles.number_input("Bathroom tiles (Sq.ft)", min_value=0, max_value=10000, step=100, key="selected_bathroom_tiles")
        selected_parking_tiles = parking_tiles.number_input("Parking tiles (Sq.ft)", min_value=0, max_value=10000, step=100, key="selected_parking_tiles")                
        selected_roof_tiles = roof_tiles.number_input("Roof tiles (Sq.ft)", min_value=0, max_value=10000, step=100, key="selected_roof_tiles")                
        
        tiles_work_form.form_submit_button(label="Update", on_click=store_values)
        
        floor_df = create_df(df_name="tiles_work_df",item="Floor Tiles", count=selected_floor_tiles)        
        wall_df = create_df(df_name="tiles_work_df",item="Wall Tiles", count=selected_wall_tiles)        
        exterior_df = create_df(df_name="tiles_work_df",item="Exterior Tiles", count=selected_exterior_tiles)        
        bathrrom_df = create_df(df_name="tiles_work_df",item="Bathroom Tiles", count=selected_bathroom_tiles)        
        parking_df = create_df(df_name="tiles_work_df",item="Parking Tiles", count=selected_parking_tiles)
        roof_df = create_df(df_name="tiles_work_df",item="Roof Tiles", count=selected_roof_tiles)
  

        if selected_floor_tiles | selected_wall_tiles | selected_exterior_tiles | selected_bathroom_tiles | selected_parking_tiles | selected_roof_tiles > 0:
                final_df = pd.concat([floor_df,wall_df,exterior_df,bathrrom_df,parking_df,roof_df],ignore_index=True)
                final_df.set_index("Item",inplace=True)
                tiles_work_df = tiles_work_form.data_editor(final_df, use_container_width=True)

                # store_edited_df()
                if tiles_work_form.form_submit_button(label="Save"):
                        st.session_state["tiles_work_df"] = tiles_work_df 
                        st.toast("Done!", icon="👍")