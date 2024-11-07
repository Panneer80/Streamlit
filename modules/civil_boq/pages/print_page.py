import streamlit as st
import pandas as pd

# st.write(st.session_state)



if ("basic_details_df" in st.session_state) & ("concrete_widgets_df" in st.session_state):
    jcb_cost = (st.session_state.price_widgets_df.loc["jcb_work_per_hour"].iloc[0])  * ( st.session_state.concrete_widgets_df.loc["selected_Footing_count"].iloc[0]  / 2)
    gravel_cost  =(st.session_state.price_widgets_df.loc["gravel_price_per_ton"].iloc[0])  * ( st.session_state.concrete_widgets_df.loc["selected_Gravel_Qty"].iloc[0] )
    site_prep_cost = round(jcb_cost + gravel_cost)
    concrete_work_cost = st.session_state.concreate_costs["concrete_cement_cost"] + st.session_state.concreate_costs["concrete_sand_cost"] + st.session_state.concreate_costs["concrete_aggregate_cost"] + st.session_state.concreate_costs["concrete_steal_cost"]
    masonary_work_cost = round(st.session_state.masonary_costs["masonary_bricks_cost"] + st.session_state.masonary_costs["masonary_cement_cost"] + st.session_state.masonary_costs["masonary_sand_cost"])
    labour_cost = st.session_state.basic_details_df.loc["builtup_area"].iloc[0]  * ( st.session_state.price_widgets_df.loc["labour_price_per_sqft"].iloc[0]) 
    if "door_work_df" in st.session_state:
        windows_doors_cost = round((st.session_state.door_work_df["Price"].astype(float)).sum())
    else: 
        windows_doors_cost = 0
    flooring_cost = st.session_state.total_tiles_cost
    if "painting_widgets_df" in st.session_state:
        painting_cost = st.session_state.painting_widgets_df.loc["painting_work_cost"].iloc[0]
    else: 
        painting_cost = 0
    if "plumbing_widgets_df" in st.session_state:
        plumbing_cost = st.session_state.plumbing_widgets_df.loc["plumbing_work_cost"].iloc[0]
    else:
        plumbing_cost = 0
    if "electrical_widgets_df" in st.session_state:
        electrical_cost = st.session_state.electrical_widgets_df.loc["electrical_work_cost"].iloc[0]
    else:
        electrical_cost = 0
        
    grand_total = (site_prep_cost + concrete_work_cost + masonary_work_cost + windows_doors_cost + flooring_cost + painting_cost + plumbing_cost + electrical_cost + labour_cost)
    total_cement_cost = st.session_state.concreate_costs["concrete_cement_cost"] + st.session_state.masonary_costs["masonary_cement_cost"]
    total_sand_cost = st.session_state.concreate_costs["concrete_sand_cost"] + st.session_state.masonary_costs["masonary_sand_cost"]
    steal_df = st.session_state.concreate_qtys["steel_df"]
    if "weight(KG)" in steal_df.keys():
        steal_df_mask = steal_df["weight(KG)"] > 0
        final_steal_df = steal_df[steal_df_mask].to_html()
    else:
        final_steal_df = steal_df.to_html()
    if "tiles_work_df" in st.session_state:
        tiles_df = st.session_state.tiles_work_df
        tiles_mask = tiles_df["Area"] > 0
        final_tiles_df = tiles_df[tiles_mask].to_html(index_names=False)         
    else:
         final_tiles_df = pd.DataFrame().to_html()    
    if 'electrical_widgets_df' in st.session_state:     
        elec_df = st.session_state.electrical_widgets_df.iloc[:9,:].to_html(index_names=False, bold_rows=False)  
    else:
        elec_df = pd.DataFrame().to_html()       
    if 'plumbing_widgets_df' in st.session_state:     
        plumb_df = st.session_state.plumbing_widgets_df.iloc[:13,:].to_html(index_names=False, bold_rows=False)  
    else:
        plumb_df = pd.DataFrame().to_html()    
    if 'door_work_df' in st.session_state:     
        door_df = st.session_state.door_work_df.to_html(index_names=False)  
    else:
        door_df = pd.DataFrame().to_html()   

    if 'concrete_work_df' in st.session_state:     
        concrete_spec = st.session_state.concrete_work_df.to_html(index_names=False)  
    else:
        concrete_spec = pd.DataFrame().to_html()   

    if 'masonary_work_df' in st.session_state:     
        masonary_spec = st.session_state.masonary_work_df.to_html(index_names=False)  
    else:
        masonary_spec = pd.DataFrame().to_html()   

    st.html(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>BOQ Report</title>
        <style>
            table {{
                width: 80%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }}
            table, th, td {{
                border: 1px solid #ccc;
            }}
            th, td {{
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f4f4f4;
            }}
        </style>
    </head>
    <body> 
          
            
        <h2>Bill Of Quantities</h2>
         <table id="basic_data">
            <tbody>
                <tr>
                    <td>Prepared By</td>
                    <td>{st.session_state.basic_details_df.loc["prepared_by"]["Value"]}</td>
                </tr>
                <tr>
                    <td>Project Type</td>
                    <td>{st.session_state.basic_details_df.loc["project_type"]["Value"]}</td>
                </tr>
                <tr>
                    <td>Builtup Area</td>
                    <td>{st.session_state.basic_details_df.loc["builtup_area"]["Value"]}</td>
                </tr>
                <tr>
                    <td>Project Location</td>
                    <td>{st.session_state.basic_details_df.loc["project_location"]["Value"]}</td>
                </tr>
                <tr>
                    <td>Date</td>
                    <td>{st.session_state.basic_details_df.loc["prapared_date"]["Value"]}</td>
                </tr>

            </tbody>
        </table>        



        <h2>Summary of Costs</h2>
        <table>
            <thead>
                <tr>
                    <th>Description</th>
                    <th>Total Cost (INR)</th>                    
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Site Preparation</td>
                    <td>{site_prep_cost}</td>
                </tr>
                <tr>
                    <td>Concrete Works</td>
                    <td>{concrete_work_cost}</td>
                </tr>
                <tr>
                    <td>Masonry and Plastering</td>
                    <td>{ masonary_work_cost }</td>
                </tr>
                <tr>
                    <td>Windows & Doors</td>
                    <td>{windows_doors_cost}</td>
                </tr>                
                <tr>
                    <td>Flooring and Tiling</td>
                    <td>{flooring_cost}</td>
                </tr>
                <tr>
                    <td>Painting and Finishing</td>
                    <td>{painting_cost}</td>
                </tr>
                <tr>
                    <td>Plumbing and Sanitary Works</td>
                    <td>{plumbing_cost}</td>
                </tr>
                <tr>
                    <td>Electrical Works</td>
                    <td>{electrical_cost}</td>
                </tr>
                <tr>
                    <td>Civil labour cost</td>
                    <td>{labour_cost}</td>
                </tr>                
                <tr>
                    <td><h3>Grand Total</h3></td>
                    <td><h3>{grand_total}</h3></td>
                </tr>
            </tbody>
        </table>

               <h5>Summary of Quantities</h5>
        <table>
            <thead>
                <tr>
                    <th>Masonary & Concrete</th>
                    <th>Total Quantity</th>
                    <th>Cost</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Cement Bags</strong></td>
                    <td>{round((st.session_state.concreate_qtys["total_c_bags"] + st.session_state.masonary_qtys["cement"]))} Bags</td>
                    <td>{round(total_cement_cost)}</td>
                </tr>
                <tr>
                    <td><strong>Sand</strong></td>
                    <td>{round((st.session_state.concreate_qtys["total_sand_ton"] + st.session_state.masonary_qtys["sand"]))} Ton</td>
                    <td>{round(total_sand_cost)}</td>
                </tr>
                <tr>
                    <td><strong>Aggregate</strong></td>
                    <td>{ round(st.session_state.concreate_qtys["total_aggre_ton"]) } Ton</td>
                    <td>{round(st.session_state.concreate_costs["concrete_aggregate_cost"]) }</td>
                </tr>
                <tr>
                    <td><strong>Steel</strong></td>
                    <td>{final_steal_df}</td>
                    <td>{ round(st.session_state.concreate_costs["concrete_steal_cost"])}</td>                    
                </tr>                
                <tr>
                    <td><strong>Bricks</strong></td>
                    <td>{round(st.session_state.masonary_qtys["bricks"])}</td>
                    <td>{round(st.session_state.masonary_costs["masonary_bricks_cost"])}</td>
                </tr>
                <tr>
                    <td><strong>Gravel</strong></td>
                    <td>{round(( st.session_state.concrete_widgets_df.loc["selected_Gravel_Qty"].iloc[0] ))} Ton</td>
                    <td>{round(gravel_cost)}</td>
                </tr>                
            </tbody>
        </table>


        <h5>Tiles & Flooring</h5>


        {final_tiles_df}
        <h5>Doors and Windows</h5>
        {door_df} 

        <h5>Concrete Work Specifications</h5>  
        {concrete_spec}
        <h5>Masonary and Plastering Work Specifications</h5>  
        {masonary_spec}
        <h5>Electrical Quantities</h5>
        {elec_df}
        <h5>Plumbing Quantities</h5>
        {plumb_df}
        <h3>Notes:</h3>

        <ul>
            <li>All rates include labor, material, and equipment costs.</li>
            <li>Quantities are based on estimated measurements; actual quantities may vary.</li>
            <li>Prices are subject to change based on material cost fluctuations and project site conditions.</li>
        </ul>
    </body>
    </html>


            """)

else:
    st.subheader("Your report is not yet ready. ")
    st.write("Click the below button to complte the details.")
    if st.button("Generate Now!", type="primary", key="generate_btn_page_start"):
        st.switch_page("modules/civil_boq/pages/boq_page.py")