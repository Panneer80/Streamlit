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
                            item_use_list.append("Bed Room")     
                            item_type_list.append("UPVC")
                            item_spec_list.append("4' x 4'")  
                            item_price_list.append("2000")                
                        else:
                            sess_df = st.session_state[df_name]
                            if f"{item} {i+1}" in sess_df["Room"].keys():
                                item_use_list.append(sess_df["Room"][f"{item} {i+1}"])  
                            else:
                                  item_use_list.append("Bed Room")     
                            if f"{item} {i+1}" in sess_df["Type"].keys():
                                item_type_list.append(sess_df["Type"][f"{item} {i+1}"]) 
                            else:
                                item_type_list.append("UPVC")                 
                                                   
                            if f"{item} {i+1}" in sess_df["Size"].keys():
                                item_spec_list.append(sess_df["Size"][f"{item} {i+1}"])    
                            else:
                                item_spec_list.append("4' x 4'")      
                            if f"{item} {i+1}" in sess_df["Price"].keys():
                                item_price_list.append(sess_df["Price"][f"{item} {i+1}"]) 
                            else:
                                 item_price_list.append("2000")  
                          

                df = pd.DataFrame({"Item": item_header_list,
                                  "Room": item_use_list,
                                  "Type": item_type_list,
                                  "Size": item_spec_list,
                                  "Price": item_price_list
                                  })
                return df