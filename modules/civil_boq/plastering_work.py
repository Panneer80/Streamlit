import pandas as pd

from modules.civil_boq.create_df import create_df
def plastering_work(st):
    plastering_expander =  st.expander("Plastering Work", expanded= False, icon=":material/currency_rupee_circle:")
    if plastering_expander:
            plastering_from = plastering_expander.form(key="plastering_from")
            plastering_cement_ratio, futurep1, futurep2, futurep3  = plastering_from.columns(4)

            cement_ratio_list = ["1:4", "1:3", "1:2"]

            plastering_expander_container = plastering_from.container(border=True)    

            plastering_cement_ratio, Walls, futurem1, futurem2  = plastering_expander_container.columns(4)    
            with plastering_cement_ratio:
                cement_ratio = plastering_cement_ratio.selectbox("Cement - Sand Ratio", cement_ratio_list, )
            with Walls:        
                if st.session_state["m_selected_walls_count"] > 0:
                        selected_Walls_count = st.number_input("Wall(s)",  min_value=0, max_value=25,)
                else:
                        selected_Walls_count = st.number_input("Wall(s)",  min_value=0, max_value=25,)
            plastering_from.form_submit_button(label="Update")

            def display_input_row(item, index):
                    length,  height = plastering_from.columns(2)
                    if f"{index+1}_{item}_length" in st.session_state:
                        length.number_input(f'{index+1} {item} Length(Feet)', min_value=st.session_state[f"{index+1}_{item}_length"])
                    else:
                         length.number_input(f'{index+1} {item} Length(Feet)', min_value=0.0)
                #     if   f"{index+1}_{item}_width" in st.session_state:
                #         width.number_input(f'{index+1} {item} Thickness/Width(Feet)', min_value=st.session_state[f"{index+1}_{item}_width"])
                #     else: 
                #         width.number_input(f'{index+1} {item} Thickness/Width(Feet)', min_value=0.0)
                    if   f"{index+1}_{item}_height" in st.session_state:
                        height.number_input(f'{index+1} {item} Height(Feet)', min_value=st.session_state[f"{index+1}_{item}_height"])
                    else:
                          height.number_input(f'{index+1} {item} Height(Feet)', min_value=0.0)

            plastering_work_df = pd.DataFrame()
            def store_edited_df():  
                st.session_state["plastering_work_df"] = plastering_work_df     
                # concrete_from.write(st.session_state)

            if selected_Walls_count > 0:
                    for i in range(selected_Walls_count):
                        # display_input_row("Wall",i)
                            final_df = create_df(df_name="plastering_work_df", item="Wall", count=selected_Walls_count)
                    # if "masonary_work_df" in st.session_state:
                    #     masonary_df = st.session_state["masonary_work_df"]
                    #     print(masonary_df)
                    final_df.set_index("Item",inplace=True)
                    # final_df = final_df[["Length feet", "Length inch", "Height feet", "Height inch"]]
                    plastering_work_df = plastering_from.data_editor(final_df, use_container_width=True, disabled=["Width feet","Width inch"])
                    plastering_from.form_submit_button(label="Save ")
                    store_edited_df()



                    

