import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("modules/civil_boq/style.css")

st.subheader("Bill Of Quantity (BOQ) | Data entry")

#Expander
price_expander = st.expander("Your Price setting", expanded= True, icon=":material/currency_rupee_circle:")
if price_expander:
    price_col1, price_col2, price_col3 = price_expander.columns(3)
    with price_col1:
            st.number_input("Cement Price / Bag", value=400)
            st.number_input("20mm Aggregate / Ton", value=14000)
            st.number_input("Steel / kg", value=70)
    with price_col2:    
            st.number_input("M Sand / Ton", value=12000)
            st.number_input("Labour / Sqft", value=400)
    with price_col3:    
            st.number_input("P Sand / Ton", value=10000)
            st.number_input("Gravel / Ton", value=10000)


concrete_expander =  st.expander("Concrete Work", expanded= False, icon=":material/currency_rupee_circle:")
if concrete_expander:
    cement_grade = ["M20", "M25", "M40", "M50"]
    cement_grade_choide = concrete_expander.selectbox("Concrete Grade", cement_grade, )
    concrete_Items = ["Footing", "Column", "Beam", "Wall Footing", "Floor Slab", "Stairs"]
    concrete_expander_container = concrete_expander.container(border=True)    
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
    def display_input_row(item, index):
        concrete_length, concrete_width, concrete_height = concrete_expander.columns(3)
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


masonary_expander =  st.expander("Masonary Work", expanded= False, icon=":material/currency_rupee_circle:")
if masonary_expander:
        brick_length, masonary_cement_ratio = masonary_expander.columns(2)

        brick_size_list = ["9 x 4 x 3", "9.1 x 4.3 x 2.8", "12 x 8 x 6"]
        brick_size = brick_length.selectbox("Brick Size(Inches)", brick_size_list, )

        cement_ratio_list = ["1:4", "1:3", "1:2"]
        cement_ratio = masonary_cement_ratio.selectbox("Cement - Sand Ratio", cement_ratio_list, )
        masonary_expander_container = masonary_expander.container(border=True)    
        Walls, futurem1, futurem2, futurem3  = masonary_expander_container.columns(4)    
 
        with Walls:        
            selected_Walls_count = st.number_input("Wall(s)",  min_value=0, max_value=25,)
        
        def display_input_row(item, index):
                length, width, height = masonary_expander.columns(3)
                length.number_input(f'{index+1} {item} Length(Feet)', min_value=0.0)
                width.number_input(f'{index+1} {item} Thickness/Width(Feet)', min_value=0.0)
                height.number_input(f'{index+1} {item} Height(Feet)', min_value=0.0)

        if selected_Walls_count > 0:
                for i in range(selected_Walls_count):
                        display_input_row("Wall",i)