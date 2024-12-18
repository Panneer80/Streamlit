import streamlit as st
import pandas as pd

def set_price():
    price_expander = st.expander("Civil work price setting", expanded= False, icon=":material/star:")
    if price_expander:
            price_from = price_expander.form(key="price_form")
            price_col1, price_col2, price_col3 = price_from.columns(3)
            items_list = ["cement_price_per_bag", "aggregate_price_per_ton","steel_price_per_kg","msand_price_per_ton","labour_price_per_sqft","psand_price_per_ton","gravel_price_per_ton","brick_per_piece","jcb_work_per_hour"]

            def store_values(pop=True):
                values_list = [st.session_state.cement_price_per_bag,st.session_state.aggregate_price_per_ton,st.session_state.steel_price_per_kg,st.session_state.msand_price_per_ton,st.session_state.labour_price_per_sqft,st.session_state.psand_price_per_ton,st.session_state.gravel_price_per_ton,st.session_state.brick_per_piece,st.session_state.jcb_work_per_hour ]
                price_widgets_df = pd.DataFrame({"Item": items_list,
                                  "Value": values_list,
                                  })
                price_widgets_df.set_index("Item", inplace=True)
                st.session_state.price_widgets_df = price_widgets_df
                if pop:
                    st.toast("Done!", icon="👍")

            def load_values(items_list):
                for item in items_list:
                     st.session_state[item] = st.session_state.price_widgets_df.loc[item]["Value"]

            if "price_widgets_df" in st.session_state:
                load_values(items_list)      

            with price_col1:
                cement_price_per_bag = st.number_input("Cement Price / Bag",min_value=300, max_value=2000,step=50, key="cement_price_per_bag")
                aggregate_price_per_ton = st.number_input("Aggregate / Ton", min_value=1000, max_value=100000, step=500, key="aggregate_price_per_ton")
                brick_per_piece = st.number_input("Brick / Piece", min_value=5, max_value=100, step=1, key="brick_per_piece")                
            with price_col2:    
                msand_price_per_ton = st.number_input("M Sand / Ton", min_value=1000, max_value=100000, step=500, key="msand_price_per_ton")
                steel_price_per_kg = st.number_input("Steel / kg", min_value=50, max_value=1000, step=10, key="steel_price_per_kg")
                labour_price_per_sqft = st.number_input("Labour / Sqft", min_value=100, max_value=5000, step=50, key="labour_price_per_sqft")  
            with price_col3:    
                psand_price_per_ton = st.number_input("P Sand / Ton", min_value=1000, max_value=100000, step=500, key="psand_price_per_ton")
                gravel_price_per_ton = st.number_input("Gravel / Ton", min_value=1000, max_value=100000, step=500, key="gravel_price_per_ton")
                jcb_work_per_hour = st.number_input("JCB Earth work / Hour", min_value=1000, max_value=100000, step=500, key="jcb_work_per_hour")
            store_values(False)
            price_from.form_submit_button(label="Set Price", on_click=store_values, type="primary")