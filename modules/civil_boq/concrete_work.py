
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
            with Footing:        
                selected_Footing_count = st.number_input("Footing",  min_value=0, max_value=25,)
            with Column:        
                selected_Column_count = st.number_input("Column",  min_value=0, max_value=25,)
            with Beam:        
                selected_Beam_count = st.number_input("Beam",  min_value=0, max_value=25,)
            with Wall_Footing:        
                selected_Wall_Footing_count = st.number_input("Wall_Footing",  min_value=0, max_value=25,)
            with Floor_Slab:        
                selected_Floor_Slab_count = st.number_input("Floor_Slab",  min_value=0, max_value=25,)
            with Stairs:        
                selected_Stairs_count = st.number_input("Stairs",  min_value=0, max_value=25,)
            concrete_from.form_submit_button(label="Save")
            def display_input_row(item, index):
                    concrete_length, concrete_width, concrete_height = concrete_from.columns(3)
                    concrete_length.number_input(f'{index+1} {item} Length(Feet)', min_value=1.0)
                    concrete_width.number_input(f'{index+1} {item} Width(Feet)', min_value=1.0)
                    concrete_height.number_input(f'{index+1} {item} Height(Feet)', min_value=1.0)

            if selected_Footing_count > 0:
                    for i in range(selected_Footing_count):
                            display_input_row("Footing",i)
            if selected_Column_count > 0:
                    for i in range(selected_Column_count):
                            display_input_row("Column",i)
            if selected_Beam_count > 0:
                    for i in range(selected_Beam_count):
                            display_input_row("Beam",i)
            if selected_Wall_Footing_count > 0:
                    for i in range(selected_Wall_Footing_count):
                            display_input_row("Wall_Footing",i)
            if selected_Floor_Slab_count > 0:
                    for i in range(selected_Floor_Slab_count):
                            display_input_row("Floor_Slab",i)
            if selected_Stairs_count > 0:
                    for i in range(selected_Stairs_count):
                            display_input_row("Stairs",i)
            def display_concrete_save_button():
                    concrete_expander.button(label="Save", key="concrete_final_save_btn")
            if selected_Footing_count | selected_Column_count | selected_Beam_count | selected_Wall_Footing_count | selected_Floor_Slab_count | selected_Stairs_count > 0:
                    display_concrete_save_button()
