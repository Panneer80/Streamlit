import streamlit as st
import pandas as pd

def masonary_calculator():
    if "masonary_work_df" in st.session_state:
        df = st.session_state.masonary_work_df
        df.fillna(0, inplace=True)
        # df.to_csv("C:\\work\\Streamlit_Code\\Streamlit\\test.csv")
        # iterate all rows
        masonary_cement_bags = []
        masonary_bricks = []
        masonary_sand = []

        for index, row in df.iterrows():
            wall_length_feet = row["Wall Length feet"]
            wall_length_inch = row["Wall Length inch"]
            wall_length_inch_to_feet = wall_length_inch / 12
            total_wall_length_feet = wall_length_feet + wall_length_inch_to_feet
            total_wall_length_meter = total_wall_length_feet / 3.281

            wall_height_feet = row["Wall Height feet"]
            wall_height_inch = row["Wall Height inch"]
            wall_height_inch_to_feet = wall_height_inch / 12
            total_wall_height_feet = wall_height_feet + wall_height_inch_to_feet
            total_wall_height_meter = total_wall_height_feet / 3.281

            brick_size = row["Brick size"].split(' x ')
            brick_length = int(brick_size[0]) / 39.37
            brick_width = int(brick_size[1]) / 39.37
            brick_height = int(brick_size[2]) / 39.37
            wall_thickness = row["Wall thickness(inch)"] / 39.37

            # Volume of brick masonary = wall_length(m) x wall_Height(m) x wall_thickness(m)
            brick_masonary_volume = total_wall_length_meter * total_wall_height_meter * wall_thickness
            #brick volume with mortar in meter
            brick_volume_with_mortar = (brick_length + 0.01) * (brick_width + 0.01) * (brick_height + 0.01)
            # number of bricks required = Volume of brick masonary / brick_volume_with_mortar
            number_of_bricks = brick_masonary_volume / brick_volume_with_mortar



            actual_volume_of_bricks_mortar = number_of_bricks * (brick_length * brick_width * brick_height )
            quantity_of_mortar = brick_masonary_volume - actual_volume_of_bricks_mortar
            quantity_of_mortar = quantity_of_mortar + (quantity_of_mortar * (15/100)) 
            quantity_of_mortar = quantity_of_mortar + (quantity_of_mortar * (25/100)) 

            cement_ratio = row["Cement ratio"].split(':')[0]
            sand_ratio = row["Cement ratio"].split(':')[1]    
            sum_of_ratio = int(cement_ratio) + int(sand_ratio)

            amount_of_cement = (int(cement_ratio)/int(sum_of_ratio)) * quantity_of_mortar
            num_of_cement_bags = amount_of_cement / 0.035


            amount_of_sand = (int(sand_ratio)/int(sum_of_ratio)) * quantity_of_mortar
            sand_in_kg = amount_of_sand * 1500
            sand_in_ton = sand_in_kg / 1000
            masonary_bricks.append(number_of_bricks)
            masonary_cement_bags.append(num_of_cement_bags)
            masonary_sand.append(sand_in_ton)
            # print(number_of_bricks)
            # print(num_of_cement_bags)
            # print(sand_in_kg)

            plaster_area = total_wall_length_feet * total_wall_height_feet
            plaster_area_sqmtr = plaster_area / 10.764   
            # print(plaster_area)
            # print(plaster_area_sqmtr)
            volume_of_plaster_mortar = plaster_area_sqmtr * (int(row["Plastering thickness"].replace(' mm', '')) / 1000)
            # print(volume_of_plaster_mortar)
            # Add 30% to fill up join & Cover surface
            volume_of_plaster_mortar = volume_of_plaster_mortar + (volume_of_plaster_mortar * (15/100)) 
        
            #  Increases by 25% of the total dry volume
            volume_of_plaster_mortar = volume_of_plaster_mortar + (volume_of_plaster_mortar * (25/100)) 
            # print(volume_of_plaster_mortar)       

            cement_bags_for_plastering = ((volume_of_plaster_mortar * int(cement_ratio)) / int(sum_of_ratio)) / 0.035
            # print(cement_bags_for_plastering)

            sand_for_plastering = (((volume_of_plaster_mortar * int(sand_ratio)) / int(sum_of_ratio)) * 1550) / 1000
            # print(sand_for_plastering)

            masonary_cement_bags.append(cement_bags_for_plastering * 2)
            masonary_sand.append(sand_for_plastering * 2)
        bricks = (round(sum(masonary_bricks),2))
        cement = (round(sum(masonary_cement_bags),2))
        sand = (round(sum(masonary_sand),2))
        st.session_state.masonary_qtys = { "bricks":bricks, "cement":cement, "sand":sand }
        masonary_cement_cost = cement * (st.session_state.price_widgets_df.loc["cement_price_per_bag"].iloc[0])
        masonary_sand_cost = sand * (st.session_state.price_widgets_df.loc["msand_price_per_ton"].iloc[0])
        masonary_bricks_cost = bricks * (st.session_state.price_widgets_df.loc["brick_per_piece"].iloc[0])
        
        st.session_state.masonary_costs = {"masonary_bricks_cost": masonary_bricks_cost,
                                        "masonary_cement_cost": masonary_cement_cost,
                                        "masonary_sand_cost": masonary_sand_cost
                                        }
    else:
        st.session_state.masonary_qtys = { "bricks":0, "cement":0, "sand":0 }
        st.session_state.masonary_costs = {"masonary_bricks_cost": 0,
                                        "masonary_cement_cost": 0,
                                        "masonary_sand_cost": 0
                                        }