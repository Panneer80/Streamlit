import streamlit as st
import pandas as pd

def column_steal_calc():
    concreate_df = st.session_state.concrete_work_df
    column_df = concreate_df.loc[concreate_df.index.str.startswith('Column')]
    column_rod_weight = {
    "rod_8_mm": 0,
    "rod_10_mm": 0,
    "rod_12_mm": 0,
    "rod_16_mm": 0, 
    "rod_20_mm": 0, 
    "rod_25_mm": 0
    }

    for index, seris in column_df.iterrows():
        rod_size_list = seris["Rod size"].replace(' mm','').split(' & ')    
        # print(rod_size_list)
        rod_quantity_list = seris["Rod count"].split(' + ')    
        rod_height_feet = seris["Height feet"]
        rod_height_inch_to_feet = seris["Height inch"]   / 12
        rod_height = rod_height_feet + rod_height_inch_to_feet
        ring_length = (seris["Length feet"] + (seris["Length inch"] / 12) + seris["Width feet"] + (seris["Width inch"] / 12) ) * 2
        ring_size = str(seris["Ring size"]).replace(' mm','')
        num_of_rings = rod_height / 0.5
        total_ring_length = ring_length * num_of_rings  
        s1 = rod_size_list[0]
        q1 = rod_quantity_list[0]                                            
        weight = ((int(s1)*int(s1)) /162.28) * (( rod_height / 3.281 ) * int(q1))
        column_rod_weight[f"rod_{s1}_mm"] += weight
        if len(rod_size_list) > 1:
            s2 = rod_size_list[1]
            if len(rod_quantity_list) > 1: 
                q2 = rod_quantity_list[1] 
            else:
                q2 = q1                                           
            weight = ((int(s2)*int(s2)) /162.28) * (( rod_height / 3.281 ) * int(q2))
            column_rod_weight[f"rod_{s2}_mm"] += weight
        if len(ring_size) > 0:
            weight = ((int(ring_size)*int(ring_size)) /162.28) * (( total_ring_length / 3.281 ) * 1)
            column_rod_weight[f"rod_{ring_size}_mm"] += weight
  
    coloum_rod_keys = column_rod_weight.keys()
    coloum_rod_values = column_rod_weight.values()
    coulum_steel_data = {
    "size": coloum_rod_keys,
    "weight": coloum_rod_values
    }
    column_steel_df = pd.DataFrame(data=coulum_steel_data)
    return column_steel_df

def other_steal_calc():
    concreate_df = st.session_state.concrete_work_df
    other_df = concreate_df.loc[~concreate_df.index.str.startswith('Column')]
    others_rod_weight = {
    "rod_8_mm": 0,
    "rod_10_mm": 0,
    "rod_12_mm": 0,
    "rod_16_mm": 0, 
    "rod_20_mm": 0, 
    "rod_25_mm": 0
    }

    for index, seris in other_df.iterrows():
        rod_size_list = seris["Rod size"].replace(' mm','').split(' & ')    
        # print(rod_size_list)
        rod_quantity_list = seris["Rod count"].split(' + ')    
        rod_height_feet = seris["Length feet"]
        rod_height_inch_to_feet = seris["Length inch"]   / 12
        rod_height = rod_height_feet + rod_height_inch_to_feet
        # print(rod_height)
        ring_length = (seris["Length feet"] + (seris["Length inch"] / 12) + seris["Width feet"] + (seris["Width inch"] / 12) ) * 2
        # print(ring_length)
        ring_size = str(seris["Ring size"]).replace(' mm','')
        num_of_rings = rod_height / 0.5
        total_ring_length = ring_length * num_of_rings  
        s1 = rod_size_list[0]
        q1 = rod_quantity_list[0]                                            
        weight = ((int(s1)*int(s1)) /162.28) * (( rod_height / 3.281 ) * int(q1))
        # print(f"size:{s1}:length:{rod_height}:quantity:{q1}: weight: {weight}")
        others_rod_weight[f"rod_{s1}_mm"] += weight
        if len(rod_size_list) > 1:
            s2 = rod_size_list[1]
            if len(rod_quantity_list) > 1: 
                q2 = rod_quantity_list[1] 
            else:
                q2 = q1                                           
            weight = ((int(s2)*int(s2)) /162.28) * (( rod_height / 3.281 ) * int(q2))
            others_rod_weight[f"rod_{s2}_mm"] += weight
        if len(ring_size) > 0 :
            weight = ((int(ring_size)*int(ring_size)) /162.28) * (( total_ring_length / 3.281 ) * 1)
            others_rod_weight[f"rod_{ring_size}_mm"] += weight
    other_rod_keys = others_rod_weight.keys()
    other_rod_values = others_rod_weight.values()
    other_steel_data = {
    "size": other_rod_keys,
    "weight": other_rod_values
    }
    other_steel_df = pd.DataFrame(data=other_steel_data)
    return  other_steel_df

def steel_calculator():
    if "concrete_work_df" in st.session_state:
        column_steel_df = column_steal_calc()
        other_steel_df = other_steal_calc()
        final_steal_weight_df = column_steel_df + other_steel_df
        return final_steal_weight_df

def concrete_wet_volume(df):
    #find total length, width, height
    length_feet = df["Length feet"].sum()
    width_feet = df["Width feet"].sum()
    height_feet = df["Height feet"].sum()
    length_inch = df["Length inch"].sum()
    width_inch = df["Width inch"].sum()
    height_inch = df["Height inch"].sum()
    length_inch_to_feet = ( length_inch ) /12
    width_inch_to_feet = (width_inch ) / 12
    height_inch_to_feet = (height_inch) / 12
    total_length = length_feet + length_inch_to_feet
    total_width = width_feet + width_inch_to_feet
    total_height = height_feet + height_inch_to_feet
    #find concreate dry volume (l x w x h)
    concrete_volume = total_length * total_width * total_height
    # convert cubic feet to cubic meter
    concrete_volume_in_m3 = concrete_volume / 35.315
    # find wet volume (Wet volume of mix is 52.4 % higher than dry volume)
    wet_volume = concrete_volume_in_m3 + (concrete_volume_in_m3 * (52.4 /100))
    return wet_volume

def amount_of_cement(wet_volume, cement, sand, aggregate):
    cement_ratio = cement
    sum_of_ratio = cement + sand + aggregate
    cement_volume = (cement_ratio / sum_of_ratio) * wet_volume
    cement_bags_num = cement_volume / 0.035
    return cement_bags_num

def amount_of_sand(wet_volume, cement, sand, aggregate):
    sand_ratio = sand
    sum_of_ratio = cement + sand + aggregate
    sand_volume = (sand_ratio / sum_of_ratio) * wet_volume
    sand_in_kg = sand_volume * 1550
    sand_in_ton = sand_in_kg / 1000
    return sand_in_ton

def amount_of_aggregate(wet_volume, cement, sand, aggregate):
    aggregate_ratio = aggregate
    sum_of_ratio = cement + sand + aggregate
    aggregate_volume = (aggregate_ratio / sum_of_ratio) * wet_volume
    aggegate_in_kg = aggregate_volume * 1350
    aggregate_in_ton = aggegate_in_kg / 1000
    return aggregate_in_ton

def concrete_calculator():
    total_c_bags, total_sand_ton, total_aggre_ton = 0, 0, 0
    m20_c_bags,m20_sand_ton,m20_aggre_ton = 0, 0, 0
    m25_c_bags,m25_sand_ton,m25_aggre_ton = 0, 0, 0
    if "concrete_work_df" in st.session_state:
        # print(st.session_state.concrete_work_df)
        concreate_df = st.session_state.concrete_work_df
        m20_mask = concreate_df["Grade"] == "M20"
        m25_mask = concreate_df["Grade"] == "M25"        
        m20_concrete_df = concreate_df[m20_mask]
        m20_wet_volume = concrete_wet_volume(m20_concrete_df)        
        m20_c_bags = amount_of_cement(wet_volume=m20_wet_volume, cement=1, sand=1.5, aggregate=3)        
        m20_sand_ton = amount_of_sand(wet_volume=m20_wet_volume, cement=1, sand=1.5, aggregate=3)  
        m20_aggre_ton = amount_of_aggregate(wet_volume=m20_wet_volume, cement=1, sand=1.5, aggregate=3)              
        m25_concrete_df = concreate_df[m25_mask]   
        if m25_concrete_df.shape[0] != 0:   
            m25_wet_volume = concrete_wet_volume(m25_concrete_df)
            m25_c_bags = amount_of_cement(wet_volume=m25_wet_volume, cement=1, sand=1, aggregate=2)
            m25_sand_ton = amount_of_sand(wet_volume=m25_wet_volume, cement=1, sand=1, aggregate=2)
            m25_aggre_ton = amount_of_aggregate(wet_volume=m25_wet_volume, cement=1, sand=1, aggregate=2)                     
        total_c_bags = float(m20_c_bags + m25_c_bags)
        total_sand_ton = float(m20_sand_ton + m25_sand_ton)
        total_aggre_ton = float(m20_aggre_ton + m25_aggre_ton  )
        steel_df = steel_calculator()
    st.session_state.concreate_qtys = [total_c_bags,total_sand_ton, total_aggre_ton, steel_df] 


        
