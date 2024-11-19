import streamlit as st
import pandas as pd
from spire.doc import *
from spire.doc.common import *
import time
import os
from modules.civil_boq.utils.send_report import send_boq_report


#   

if ("basic_details_df" in st.session_state) & ("concrete_widgets_df" in st.session_state) & ("concreate_costs" in st.session_state):
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

    if "saved_other_work_df"  in st.session_state:
        other_cost_df = st.session_state.saved_other_work_df
        other_cost_df_mask = other_cost_df["Cost"] > 0
        other_cost  = other_cost_df[other_cost_df_mask]["Cost"].sum()
        other_cost_df_html  = other_cost_df[other_cost_df_mask].to_html(index_names=False)    

    else:
        other_cost = 0
        other_cost_df_html = pd.DataFrame().to_html()   
        
    grand_total = (site_prep_cost + concrete_work_cost + masonary_work_cost + windows_doors_cost + flooring_cost + painting_cost + plumbing_cost + electrical_cost + labour_cost + other_cost)
    
    # donut chart variables
    # dchart_labels = ["site_prep_cost","concrete_work_cost","masonary_work_cost","windows_doors_cost","flooring_cost","painting_cost","plumbing_cost","electrical_cost","labour_cost","other_cost"]
    # dchart_values = [site_prep_cost, concrete_work_cost, masonary_work_cost, windows_doors_cost, flooring_cost, painting_cost, plumbing_cost, electrical_cost, labour_cost, other_cost]

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

    if 'painting_widgets_df' in st.session_state:     
        paint_df = st.session_state.painting_widgets_df.iloc[:6,:].to_html(index_names=False, bold_rows=False)  
    else:
        paint_df = pd.DataFrame().to_html()           

    if 'concrete_work_df' in st.session_state:     
        concrete_spec = st.session_state.concrete_work_df.to_html(index_names=False)  
    else:
        concrete_spec = pd.DataFrame().to_html()   

    if 'masonary_work_df' in st.session_state:     
        masonary_spec = st.session_state.masonary_work_df.to_html(index_names=False)  
    else:
        masonary_spec = pd.DataFrame().to_html()   

    @st.dialog("Download your BOQ")
    def docDownload():
        timestr = time.strftime("%d%m%Y-%H%M%S")
        if "boq_file_name" not in st.session_state:
            st.session_state.boq_file_name = f"temp_downloads/{timestr}.docx"
        col1, col2 = st.columns(2)
        # Create a Document object
        document = Document()
        # Add a section to the document
        section = document.AddSection()

        # Set the page margins to 72 points (72 points = 1 inch)
        section.PageSetup.Margins.All = 72

        # Add a paragraph to the section
        paragraph = section.AddParagraph()

        # Add the HTML string to the paragraph
        paragraph.AppendHTML(boq_html)

        # Save the result document to a DOCX file
        document.SaveToFile(st.session_state.boq_file_name, FileFormat.Docx2016)
        # Or save the result document to a DOC file
        # document.SaveToFile("HtmlStringToDoc.doc", FileFormat.Doc)
        document.Close()    
        # href = f"""
        # <a style="border-radius: 8px;color:black;background-color: #E2C27B;padding: 8px 25px;text-align: center;text-decoration: none;display: inline-block;" href="{st.session_state.boq_file_name}" download="{st.session_state.boq_file_name}">Download DOCX File</a>
        # """
        # col1.markdown(href, unsafe_allow_html=True) 
        
        with open(st.session_state.boq_file_name, 'rb') as f:
            col1.download_button('Download as word file', f, file_name=st.session_state.boq_file_name)   
        st.divider()   
        st.text(""" 
                If you like to support me, 
                scan the UPI QR code below. 
                Every contribution, big or small, 
                helps me cover maintenance costs.""")

        st.image("modules/about_me/images/My_QR_Code.jpeg", width=300)
              
        if col2.button("Close", type="primary"):
            os.remove(st.session_state.boq_file_name)
            del st.session_state.boq_file_name
            send_boq_report(boq_html)
            st.rerun()

    boq_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>

        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>BOQ Report</title>
        <style>
         div[aria-label="dialog"]>button[aria-label="Close"] {{
                display: none;
            }}
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
          
            
        <h3>Building Cost and Quantities Report</h3>
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
                    <td>Other Cost (drawing, consulting, etc)</td>
                    <td>{other_cost}</td>
                </tr>                             
                <tr>
                    <td><h3>Grand Total</h3></td>
                    <td><h3>{grand_total}</h3></td>
                </tr>
            </tbody>
        </table>

        

<p style="page-break-after: always;">&nbsp;</p>
<p style="page-break-before: always;">&nbsp;</p>
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
                    <td>{round((st.session_state.concreate_qtys["total_c_bags"] + st.session_state.masonary_qtys["cement"]),2)} Bags</td>
                    <td>{round(total_cement_cost)}</td>
                </tr>
                <tr>
                    <td><strong>Sand</strong></td>
                    <td>{round((st.session_state.concreate_qtys["total_sand_ton"] + st.session_state.masonary_qtys["sand"]),2)} Ton</td>
                    <td>{round(total_sand_cost)}</td>
                </tr>
                <tr>
                    <td><strong>Aggregate</strong></td>
                    <td>{ round(st.session_state.concreate_qtys["total_aggre_ton"],2) } Ton</td>
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
                    <td>{round(( st.session_state.concrete_widgets_df.loc["selected_Gravel_Qty"].iloc[0] ),2)} Ton</td>
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
        <h5>Painting Quantities</h5>
        {paint_df}
        <h5>Other Costs</h5>
        {other_cost_df_html}        
        <h3>Notes:</h3>

        <ul>
            <li>All rates include labor, material, and equipment costs.</li>
            <li>Quantities are based on estimated measurements; actual quantities may vary.</li>
            <li>Prices are subject to change based on material cost fluctuations and project site conditions.</li>
        </ul>

    

    </body>
    </html>"""
    
    if st.button("Download",type="primary", key="boq_download_btn_top"):
        docDownload()
    # with open("C:\\work\\Streamlit_Code\\Streamlit\\modules\\civil_boq\\text.html", "w") as text_file:
    #         text_file.write(boq_html)     
    st.html(boq_html)      
    
    if st.button("Download",type="primary"):
        docDownload()

else:
    st.subheader("Your report is not yet ready. ")
    st.write("Click the below button to complte the details.")
    if st.button("Generate Now!", type="primary", key="generate_btn_page_start"):
        st.switch_page("modules/civil_boq/pages/boq_page.py")
    