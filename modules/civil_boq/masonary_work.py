    
def masonary_work(st):
    masonary_expander =  st.expander("Masonary Work", expanded= False, icon=":material/currency_rupee_circle:")
    if masonary_expander:
            masonary_from = masonary_expander.form(key="masonary_from")
            brick_length, masonary_cement_ratio = masonary_from.columns(2)

            brick_size_list = ["9 x 4 x 3", "9.1 x 4.3 x 2.8", "12 x 8 x 6"]
            brick_size = brick_length.selectbox("Brick Size(Inches)", brick_size_list, )

            cement_ratio_list = ["1:4", "1:3", "1:2"]
            cement_ratio = masonary_cement_ratio.selectbox("Cement - Sand Ratio", cement_ratio_list, )
            masonary_expander_container = masonary_from.container(border=True)    

            Walls, futurem1, futurem2, futurem3  = masonary_expander_container.columns(4)    
    
            with Walls:        
                selected_Walls_count = st.number_input("Wall(s)",  min_value=0, max_value=25, key="m_selected_walls_count")
            masonary_from.form_submit_button(label="Update")
            def display_input_row(item, index):
                    length, width, height = masonary_from.columns(3)
                    length.number_input(f'{index+1} {item} Length(Feet)', min_value=0.0, key=f'{index+1}_{item}_length')
                    width.number_input(f'{index+1} {item} Thickness/Width(Feet)', min_value=0.0, key=f'{index+1}_{item}_width')
                    height.number_input(f'{index+1} {item} Height(Feet)', min_value=0.0, key=f'{index+1}_{item}_height')

            def display_masonary_save_button():
                #     masonary_expander.button(label="Save", key="masonary_final_save_btn")
                    masonary_from.form_submit_button(label="Update ")
            if selected_Walls_count > 0:
                    for i in range(selected_Walls_count):
                            display_input_row("Wall",i)
                    display_masonary_save_button()