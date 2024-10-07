
def set_price(st):
    price_expander = st.expander("Your Price setting", expanded= True, icon=":material/currency_rupee_circle:")
    if price_expander:
            price_from = price_expander.form(key="price_form")
            price_col1, price_col2, price_col3 = price_from.columns(3)
            with price_col1:
                cement_price_per_bag = st.number_input("Cement Price / Bag", value=400, key="cement_price_per_bag")
                aggregate_price_per_ton = st.number_input("20mm Aggregate / Ton", value=14000)
                steel_price_per_kg = st.number_input("Steel / kg", value=70)
            with price_col2:    
                msand_price_per_ton = st.number_input("M Sand / Ton", value=12000)
                labour_price_per_sqft = st.number_input("Labour / Sqft", value=400)
            with price_col3:    
                psand_price_per_ton = st.number_input("P Sand / Ton", value=10000)
                gravel_price_per_ton = st.number_input("Gravel / Ton", value=10000)
            price_from.form_submit_button(label="Save")