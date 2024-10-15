import streamlit as st
import pandas as pd        

def create_df(df_name, item="Floor Tiles", count=1, ):
                item_header_list = []
                item_area_list = []
                item_price_list = []


                item_header_list.append(f"{item}")
                if df_name not in st.session_state:
                            item_area_list.append(count)     
                            item_price_list.append(60)
                else:
                    sess_df = st.session_state[df_name]
                    if f"{item}" in sess_df["Area"].keys():
                        item_area_list.append(sess_df["Area"][f"{item}"])  
                    else:
                        item_area_list.append(count)       
                    if f"{item}" in sess_df["Price per Sq.ft"].keys():
                        item_price_list.append(sess_df["Price per Sq.ft"][f"{item}"]) 
                    else:
                        item_price_list.append(60)                  
                                                                                                            

                df = pd.DataFrame({"Item": item_header_list,
                                  "Area": item_area_list,
                                  "Price per Sq.ft": item_price_list,

                                  })
                return df