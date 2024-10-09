    
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
                        selected_Walls_count = st.number_input("Wall(s)",  min_value=st.session_state["m_selected_walls_count"], max_value=25,)
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
            def display_plastering_save_button():
                    plastering_expander.button(label="Update", key="plastering_final_save_btn")
        #     st.write(st.session_state)
              
            if selected_Walls_count > 0:
                    for i in range(selected_Walls_count):
                                display_input_row("Wall",i)
                    display_plastering_save_button()