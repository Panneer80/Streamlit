import streamlit as st
# from modules.civil_boq.calculations.concrete_calculator import concrete_calculator
# from modules.civil_boq.calculations.concrete_calculator import steel_calculator
# st.button(label="Calculate", on_click=steel_calculator)
st.write(st.session_state)
if "basic_details_df" in st.session_state:

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

        <table>
            <thead>
                <tr>
                    <th>Item No.</th>
                    <th>Description of Work</th>
                    <th>Unit</th>
                    <th>Quantity</th>
                    <th>Unit Rate (INR)</th>
                    <th>Total Cost (INR)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>1.0</strong></td>
                    <td><strong>Site Preparation</strong></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <td>1.1</td>
                    <td>JCB Clearing and Excavation work</td>
                    <td>Hours</td>
                    <td>6</td>
                    <td>1000</td>
                    <td>6000</td>
                </tr>
                <tr>
                    <td>1.2</td>
                    <td>Gravel Sand</td>
                    <td>Ton</td>
                    <td>6</td>
                    <td>5000</td>
                    <td>30000</td>
                </tr>                
                <tr>
                    <td><strong>2.0</strong></td>
                    <td><strong>Concrete Work</strong></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <td>2.1</td>
                    <td>Cement</td>
                    <td>Bags</td>
                    <td>15</td>
                    <td>400</td>
                    <td>6000</td>
                </tr>
                <tr>
                    <td>2.2</td>
                    <td>Sand</td>
                    <td>Ton</td>
                    <td>30</td>
                    <td>120.00</td>
                    <td>3,600.00</td>
                </tr>
                <tr>
                    <td>2.3</td>
                    <td>Aggregate</td>
                    <td>Ton</td>
                    <td>80</td>
                    <td>20.00</td>
                    <td>1,600.00</td>
                </tr>
                <tr>
                    <td>2.3</td>
                    <td>Steel</td>
                    <td>Ton</td>
                    <td>80</td>
                    <td>20.00</td>
                    <td>1,600.00</td>
                </tr>                
                <tr>
                    <td><strong>3.0</strong></td>
                    <td><strong>Masonry and Plastering</strong></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <td>3.1</td>
                    <td>Bricks</td>
                    <td>cu.m</td>
                    <td>40</td>
                    <td>55.00</td>
                    <td>2,200.00</td>
                </tr>
                <tr>
                    <td>3.2</td>
                    <td>Cement</td>
                    <td>sq.m</td>
                    <td>100</td>
                    <td>5.00</td>
                    <td>500.00</td>
                </tr>
                <tr>
                    <td>3.3</td>
                    <td>Sand</td>
                    <td>sq.m</td>
                    <td>80</td>
                    <td>6.00</td>
                    <td>480.00</td>
                </tr>
                <tr>
                    <td><strong>4.0</strong></td>
                    <td><strong>Flooring and Tiling</strong></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <td>4.1</td>
                    <td>Ceramic Floor Tiles (300x300mm)</td>
                    <td>sq.m</td>
                    <td>60</td>
                    <td>15.00</td>
                    <td>900.00</td>
                </tr>
                <tr>
                    <td>4.2</td>
                    <td>Skirting (100mm high)</td>
                    <td>m</td>
                    <td>50</td>
                    <td>2.50</td>
                    <td>125.00</td>
                </tr>
                <tr>
                    <td><strong>5.0</strong></td>
                    <td><strong>Painting and Finishing</strong></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <td>5.1</td>
                    <td>Interior Emulsion Paint (3 coats)</td>
                    <td>sq.m</td>
                    <td>120</td>
                    <td>4.00</td>
                    <td>480.00</td>
                </tr>
                <tr>
                    <td>5.2</td>
                    <td>Exterior Weatherproof Paint (2 coats)</td>
                    <td>sq.m</td>
                    <td>80</td>
                    <td>5.00</td>
                    <td>400.00</td>
                </tr>
                <tr>
                    <td><strong>6.0</strong></td>
                    <td><strong>Plumbing and Sanitary Works</strong></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <td>6.1</td>
                    <td>Installation of Water Supply Pipes (PVC)</td>
                    <td>m</td>
                    <td>30</td>
                    <td>7.00</td>
                    <td>210.00</td>
                </tr>
                <tr>
                    <td>6.2</td>
                    <td>Installation of Sanitary Fixtures</td>
                    <td>unit</td>
                    <td>4</td>
                    <td>50.00</td>
                    <td>200.00</td>
                </tr>
                <tr>
                    <td><strong>7.0</strong></td>
                    <td><strong>Electrical Works</strong></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <td>7.1</td>
                    <td>Wiring for Light Points</td>
                    <td>point</td>
                    <td>20</td>
                    <td>8.00</td>
                    <td>160.00</td>
                </tr>
                <tr>
                    <td>7.2</td>
                    <td>Installation of Switches and Sockets</td>
                    <td>unit</td>
                    <td>10</td>
                    <td>12.00</td>
                    <td>120.00</td>
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
                    <td>900.00</td>
                </tr>
                <tr>
                    <td>Concrete Works</td>
                    <td>6,325.00</td>
                </tr>
                <tr>
                    <td>Masonry and Plastering</td>
                    <td>3,180.00</td>
                </tr>
                <tr>
                    <td>Flooring and Tiling</td>
                    <td>1,025.00</td>
                </tr>
                <tr>
                    <td>Painting and Finishing</td>
                    <td>880.00</td>
                </tr>
                <tr>
                    <td>Plumbing and Sanitary Works</td>
                    <td>410.00</td>
                </tr>
                <tr>
                    <td>Electrical Works</td>
                    <td>280.00</td>
                </tr>
                <tr>
                    <td><strong>Grand Total</strong></td>
                    <td><strong>13,000.00</strong></td>
                </tr>
            </tbody>
        </table>

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