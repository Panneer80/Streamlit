import streamlit as st
import pandas as pd        

def create_df(df_name, item, count, ):
                item_header_list = []
                brick_size_list = []
                cement_ratio_list= []
                plastering_thickness_list = []
                item_length_feet_list = []
                item_length_inch_list = []
                item_height_feet_list = []
                item_height_inch_list = []
                for i in range(count):
                        item_header_list.append(f"{item} {i+1}")
                        if df_name not in st.session_state:
                            brick_size_list.append("9 x 4 x 3")
                            cement_ratio_list.append("1:4")
                            plastering_thickness_list.append("12 mm")
                            item_length_feet_list.append(1.0)     
                            item_length_inch_list.append(0.00)
                            item_height_feet_list.append(1.0)
                            item_height_inch_list.append(0.00)                       
                        else:
                            sess_df = st.session_state[df_name]
                            if f"{item} {i+1}" in sess_df["Brick size"].keys():
                                brick_size_list.append(sess_df["Brick size"][f"{item} {i+1}"])  
                            else:
                                  brick_size_list.append("9 x 4 x 3")   
                            if f"{item} {i+1}" in sess_df["Cement ratio"].keys():
                                cement_ratio_list.append(sess_df["Cement ratio"][f"{item} {i+1}"])  
                            else:
                                  cement_ratio_list.append("1:4")             
                            if f"{item} {i+1}" in sess_df["Plastering thickness"].keys():
                                plastering_thickness_list.append(sess_df["Plastering thickness"][f"{item} {i+1}"])  
                            else:
                                  plastering_thickness_list.append("12 mm")                                                                                       
                            if f"{item} {i+1}" in sess_df["Length feet"].keys():
                                item_length_feet_list.append(sess_df["Length feet"][f"{item} {i+1}"])  
                            else:
                                  item_length_feet_list.append(1.0)       
                            if f"{item} {i+1}" in sess_df["Length inch"].keys():
                                item_length_inch_list.append(sess_df["Length inch"][f"{item} {i+1}"]) 
                            else:
                                item_length_inch_list.append(0.00)                  
                            # if f"{item} {i+1}" in sess_df["Width feet"].keys():
                            #     item_width_feet_list.append(sess_df["Width feet"][f"{item} {i+1}"])  
                            # else:
                            #      item_width_feet_list.append(1.0)        
                            # if f"{item} {i+1}" in sess_df["Width inch"].keys():
                            #     item_width_inch_list.append(sess_df["Width inch"][f"{item} {i+1}"])   
                            # else:
                            #      item_width_inch_list.append(0.00)                                                      
                            if f"{item} {i+1}" in sess_df["Height feet"].keys():
                                item_height_feet_list.append(sess_df["Height feet"][f"{item} {i+1}"])    
                            else:
                                item_height_feet_list.append(1.0)      
                            if f"{item} {i+1}" in sess_df["Height inch"].keys():
                                item_height_inch_list.append(sess_df["Height inch"][f"{item} {i+1}"]) 
                            else:
                                 item_height_inch_list.append(0.00)  
                          

                df = pd.DataFrame({"Item": item_header_list,
                                   "Brick size": brick_size_list,
                                   "Cement ratio": cement_ratio_list,
                                   "Plastering thickness": plastering_thickness_list,
                                  "Length feet": item_length_feet_list,
                                  "Length inch": item_length_inch_list,
                                #   "Width feet": item_width_feet_list,
                                #   "Width inch": item_width_inch_list,
                                  "Height feet": item_height_feet_list,
                                  "Height inch": item_height_inch_list
                                  })
                return df