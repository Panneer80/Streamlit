import streamlit as st
import pandas as pd        

def create_windows_df(df_name, item="Door", count=1, ):
                item_header_list = []
                item_use_list = []
                item_type_list = []
                item_spec_list = []
                item_price_list = []
                for i in range(count):
                        item_header_list.append(f"{item} {i+1}")
                        if df_name not in st.session_state:
                            item_use_list.append("Main Door")     
                            item_type_list.append("Steel")
                            item_spec_list.append("4' x 7'")  
                            item_price_list.append("20000")                
                        else:
                            sess_df = st.session_state[df_name]
                            if f"{item} {i+1}" in sess_df["Useage"].keys():
                                item_use_list.append(sess_df["Useage"][f"{item} {i+1}"])  
                            else:
                                  item_use_list.append("Main Door")     
                            if f"{item} {i+1}" in sess_df["Type"].keys():
                                item_type_list.append(sess_df["Type"][f"{item} {i+1}"]) 
                            else:
                                item_type_list.append("Steel")                 
                                                   
                            if f"{item} {i+1}" in sess_df["Size"].keys():
                                item_spec_list.append(sess_df["Size"][f"{item} {i+1}"])    
                            else:
                                item_spec_list.append("4' x 7'")      
                            if f"{item} {i+1}" in sess_df["Price"].keys():
                                item_price_list.append(sess_df["Price"][f"{item} {i+1}"]) 
                            else:
                                 item_price_list.append("20000")  
                          

                df = pd.DataFrame({"Item": item_header_list,
                                  "Useage": item_use_list,
                                  "Type": item_type_list,
                                  "Size": item_spec_list,
                                  "Price": item_price_list
                                  })
                return df