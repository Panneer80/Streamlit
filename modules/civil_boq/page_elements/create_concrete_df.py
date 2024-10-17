import streamlit as st
import pandas as pd        

def create_df(df_name, item="Footing", count=1, ):
                item_header_list = []
                item_description_list = []
                item_Grade_list = []
                item_length_feet_list = []
                item_length_inch_list = []
                item_width_feet_list = []
                item_width_inch_list = []
                item_height_feet_list = []
                item_height_inch_list = []
                item_rod_size_list = []
                item_rod_count_list = []
                item_ring_size = []
                for i in range(count):
                        item_header_list.append(f"{item} {i+1}")
                        if df_name not in st.session_state:
                            item_description_list.append("")
                            item_Grade_list.append("M20")
                            item_length_feet_list.append(1.0)     
                            item_length_inch_list.append(0.00)
                            item_width_feet_list.append(1.0)
                            item_width_inch_list.append(0.00)
                            item_height_feet_list.append(1.0)
                            item_height_inch_list.append(0.00)   
                            item_rod_size_list.append("16 mm")
                            item_rod_count_list.append("4")
                            item_ring_size.append("")
                        else:
                            sess_df = st.session_state[df_name]
                            if f"{item} {i+1}" in sess_df["Description"].keys():
                                item_description_list.append(sess_df["Description"][f"{item} {i+1}"])  
                            else:
                                  item_description_list.append("") 
                            if f"{item} {i+1}" in sess_df["Grade"].keys():
                                item_Grade_list.append(sess_df["Grade"][f"{item} {i+1}"])  
                            else:
                                  item_Grade_list.append("M20")                             
                            if f"{item} {i+1}" in sess_df["Length feet"].keys():
                                item_length_feet_list.append(sess_df["Length feet"][f"{item} {i+1}"])  
                            else:
                                  item_length_feet_list.append(1.0)       
                            if f"{item} {i+1}" in sess_df["Length inch"].keys():
                                item_length_inch_list.append(sess_df["Length inch"][f"{item} {i+1}"]) 
                            else:
                                item_length_inch_list.append(0.00)                  
                            if f"{item} {i+1}" in sess_df["Width feet"].keys():
                                item_width_feet_list.append(sess_df["Width feet"][f"{item} {i+1}"])  
                            else:
                                 item_width_feet_list.append(1.0)        
                            if f"{item} {i+1}" in sess_df["Width inch"].keys():
                                item_width_inch_list.append(sess_df["Width inch"][f"{item} {i+1}"])   
                            else:
                                 item_width_inch_list.append(0.00)                                                      
                            if f"{item} {i+1}" in sess_df["Height feet"].keys():
                                item_height_feet_list.append(sess_df["Height feet"][f"{item} {i+1}"])    
                            else:
                                item_height_feet_list.append(1.0)      
                            if f"{item} {i+1}" in sess_df["Height inch"].keys():
                                item_height_inch_list.append(sess_df["Height inch"][f"{item} {i+1}"]) 
                            else:
                                 item_height_inch_list.append(0.00)  
                            if f"{item} {i+1}" in sess_df["Rod size"].keys():
                                item_rod_size_list.append(sess_df["Rod size"][f"{item} {i+1}"]) 
                            else:
                                 item_rod_size_list.append("16 mm")     
                            if f"{item} {i+1}" in sess_df["Rod count"].keys():
                                item_rod_count_list.append(sess_df["Rod count"][f"{item} {i+1}"]) 
                            else:
                                 item_rod_count_list.append("4")       
                            if f"{item} {i+1}" in sess_df["Ring size"].keys():
                                item_ring_size.append(sess_df["Ring size"][f"{item} {i+1}"]) 
                            else:
                                 item_ring_size.append("")                                                                                 

                df = pd.DataFrame({"Item": item_header_list,
                                  "Description": item_description_list,
                                  "Grade": item_Grade_list,                                   
                                  "Length feet": item_length_feet_list,
                                  "Length inch": item_length_inch_list,
                                  "Width feet": item_width_feet_list,
                                  "Width inch": item_width_inch_list,
                                  "Height feet": item_height_feet_list,
                                  "Height inch": item_height_inch_list,
                                  "Rod size":item_rod_size_list,
                                  "Rod count":item_rod_count_list,
                                  "Ring size": item_ring_size
                                  })
                return df