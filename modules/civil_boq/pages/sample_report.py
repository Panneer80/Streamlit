import streamlit as st
st.error("This is a sample report. DO NOT PRINT IT.")
st.html("""
<!DOCTYPE html>
    <html lang="en">
    <head>

        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>BOQ Report</title>
        <style>
         div[aria-label="dialog"]>button[aria-label="Close"] {
                display: none;
            }
            table {
                width: 80%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }
            table, th, td {
                border: 1px solid #ccc;
            }
            th, td {
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f4f4f4;
            }
        

        </style>
    </head>
    <body> 
        <h2>Bill Of Quantities</h2>
         <table id="basic_data">
            <tbody>
                <tr>
                    <td>Prepared By</td>
                    <td>ABC Builders</td>
                </tr>
                <tr>
                    <td>Project Type</td>
                    <td>Residential Building</td>
                </tr>
                <tr>
                    <td>Builtup Area</td>
                    <td>1000</td>
                </tr>
                <tr>
                    <td>Project Location</td>
                    <td>Coimbatore</td>
                </tr>
                <tr>
                    <td>Date</td>
                    <td>2024-11-11</td>
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
                    <td>1000</td>
                </tr>
                <tr>
                    <td>Concrete Works</td>
                    <td>34251</td>
                </tr>
                <tr>
                    <td>Masonry and Plastering</td>
                    <td>85584</td>
                </tr>
                <tr>
                    <td>Windows & Doors</td>
                    <td>8000</td>
                </tr>                
                <tr>
                    <td>Flooring and Tiling</td>
                    <td>37400</td>
                </tr>
                <tr>
                    <td>Painting and Finishing</td>
                    <td>250000</td>
                </tr>
                <tr>
                    <td>Plumbing and Sanitary Works</td>
                    <td>200000</td>
                </tr>
                <tr>
                    <td>Electrical Works</td>
                    <td>200000</td>
                </tr>
                <tr>
                    <td>Civil labour cost</td>
                    <td>450000</td>
                </tr>     
                <tr>
                    <td>Other Cost (drawing, consulting, etc)</td>
                    <td>425000</td>
                </tr>                             
                <tr>
                    <td><h3>Grand Total</h3></td>
                    <td><h3>1691235</h3></td>
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
                    <td>30.23 Bags</td>
                    <td>12092</td>
                </tr>
                <tr>
                    <td><strong>Sand</strong></td>
                    <td>5.45 Ton</td>
                    <td>54500</td>
                </tr>
                <tr>
                    <td><strong>Aggregate</strong></td>
                    <td>1.06 Ton</td>
                    <td>10600</td>
                </tr>
                <tr>
                    <td><strong>Steel</strong></td>
                    <td><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>weight(KG)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>rod_12_mm</th>
      <td>48.50</td>
    </tr>
    <tr>
      <th>rod_16_mm</th>
      <td>108.34</td>
    </tr>
    <tr>
      <th>rod_20_mm</th>
      <td>51.09</td>
    </tr>
  </tbody>
</table></td>
                    <td>14555</td>                    
                </tr>                
                <tr>
                    <td><strong>Bricks</strong></td>
                    <td>3121</td>
                    <td>28088</td>
                </tr>
                <tr>
                    <td><strong>Gravel</strong></td>
                    <td>0 Ton</td>
                    <td>0</td>
                </tr>                
            </tbody>
        </table>


        <h5>Tiles & Flooring</h5>


        <table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area</th>
      <th>Price per Sq.ft</th>
      <th>total_price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Floor Tiles</th>
      <td>300</td>
      <td>58</td>
      <td>17400</td>
    </tr>
    <tr>
      <th>Wall Tiles</th>
      <td>100</td>
      <td>60</td>
      <td>6000</td>
    </tr>
    <tr>
      <th>Exterior Tiles</th>
      <td>100</td>
      <td>50</td>
      <td>5000</td>
    </tr>
    <tr>
      <th>Bathroom Tiles</th>
      <td>50</td>
      <td>60</td>
      <td>3000</td>
    </tr>
    <tr>
      <th>Parking Tiles</th>
      <td>100</td>
      <td>60</td>
      <td>6000</td>
    </tr>
  </tbody>
</table>
        <h5>Doors and Windows</h5>
        <table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Room</th>
      <th>Type</th>
      <th>Size</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Door 1</th>
      <td>Living Room</td>
      <td>Wooden</td>
      <td>4' x 7'</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>Door 2</th>
      <td>Toilet</td>
      <td>UPVC</td>
      <td>3' x 7'</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>Window 1</th>
      <td>Kitchen</td>
      <td>UPVC</td>
      <td>4' x 4'</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>Window 2</th>
      <td>Bed Room</td>
      <td>UPVC</td>
      <td>4' x 4'</td>
      <td>2000</td>
    </tr>
  </tbody>
</table> 

        <h5>Concrete Work Specifications</h5>  
        <table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Description</th>
      <th>Grade</th>
      <th>Length feet</th>
      <th>Length inch</th>
      <th>Width feet</th>
      <th>Width inch</th>
      <th>Height feet</th>
      <th>Height inch</th>
      <th>Rod size</th>
      <th>Rod count</th>
      <th>Ring size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Footing 1</th>
      <td></td>
      <td>M20</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>12 mm &amp; 16 mm</td>
      <td>4</td>
      <td></td>
    </tr>
    <tr>
      <th>Footing 2</th>
      <td></td>
      <td>M20</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>16 mm &amp; 20 mm</td>
      <td>2 + 4</td>
      <td></td>
    </tr>
    <tr>
      <th>Column 1</th>
      <td></td>
      <td>M20</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>10.0</td>
      <td>0.0</td>
      <td>16 mm &amp; 20 mm</td>
      <td>4 + 6</td>
      <td>12 mm</td>
    </tr>
    <tr>
      <th>Column 2</th>
      <td></td>
      <td>M20</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>11.0</td>
      <td>5.0</td>
      <td>16 mm</td>
      <td>8</td>
      <td>12 mm</td>
    </tr>
    <tr>
      <th>Beam 1</th>
      <td></td>
      <td>M20</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>16 mm</td>
      <td>8</td>
      <td></td>
    </tr>
    <tr>
      <th>Beam 2</th>
      <td></td>
      <td>M20</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>16 mm</td>
      <td>10</td>
      <td></td>
    </tr>
    <tr>
      <th>Floor Slab 1</th>
      <td></td>
      <td>M20</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>16 mm</td>
      <td>60</td>
      <td></td>
    </tr>
    <tr>
      <th>Stairs 1</th>
      <td></td>
      <td>M20</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>16 mm</td>
      <td>4</td>
      <td></td>
    </tr>
  </tbody>
</table>
        <h5>Masonary and Plastering Work Specifications</h5>  
        <table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Wall Length feet</th>
      <th>Wall Length inch</th>
      <th>Wall Height feet</th>
      <th>Wall Height inch</th>
      <th>Wall thickness(inch)</th>
      <th>Brick size</th>
      <th>Cement ratio</th>
      <th>Plastering thickness</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Wall 1</th>
      <td>10.0</td>
      <td>0.0</td>
      <td>11.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>9 x 4 x 3</td>
      <td>1:4</td>
      <td>12 mm</td>
    </tr>
    <tr>
      <th>Wall 2</th>
      <td>8.0</td>
      <td>0.0</td>
      <td>11.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>9 x 4 x 3</td>
      <td>1:4</td>
      <td>12 mm</td>
    </tr>
    <tr>
      <th>Wall 3</th>
      <td>7.0</td>
      <td>0.0</td>
      <td>11.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>9 x 4 x 3</td>
      <td>1:4</td>
      <td>12 mm</td>
    </tr>
    <tr>
      <th>Wall 4</th>
      <td>10.0</td>
      <td>0.0</td>
      <td>11.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>9 x 4 x 3</td>
      <td>1:4</td>
      <td>12 mm</td>
    </tr>
    <tr>
      <th>Wall 5</th>
      <td>5.0</td>
      <td>0.0</td>
      <td>11.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>9 x 4 x 3</td>
      <td>1:4</td>
      <td>12 mm</td>
    </tr>
    <tr>
      <th>Wall 6</th>
      <td>6.0</td>
      <td>0.0</td>
      <td>11.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>9 x 4 x 3</td>
      <td>1:4</td>
      <td>12 mm</td>
    </tr>
  </tbody>
</table>
        <h5>Electrical Quantities</h5>
        <table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Light Points</td>
      <td>9</td>
    </tr>
    <tr>
      <td>Fan Points</td>
      <td>4</td>
    </tr>
    <tr>
      <td>AC Points</td>
      <td>1</td>
    </tr>
    <tr>
      <td>UPS Points</td>
      <td>1</td>
    </tr>
    <tr>
      <td>5A Sockets</td>
      <td>7</td>
    </tr>
    <tr>
      <td>16A Sockets</td>
      <td>5</td>
    </tr>
    <tr>
      <td>20A Sockets</td>
      <td>1</td>
    </tr>
    <tr>
      <td>CCTV Points</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Solar Points</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
        <h5>Plumbing Quantities</h5>
        <table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Sink</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Faucet</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Wash Basin</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Shower Head</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Bath Tub</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Toilet Commode</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Towel Bars</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Taps</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Water Tank</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Geyser</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Water Purifier</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Fountain</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Swimming Pool</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
        <h5>Painting Quantities</h5>
        <table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Exteriror Paint</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Interior Paint</td>
      <td>30</td>
    </tr>
    <tr>
      <td>Wall Putty</td>
      <td>10</td>
    </tr>
    <tr>
      <td>Wall Primer</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Enamal Paint</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Wood Warnish</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
        <h5>Other Costs</h5>
        <table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Description</th>
      <th>Cost</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Drawing</th>
      <td>Description</td>
      <td>10000</td>
    </tr>
    <tr>
      <th>Consultation</th>
      <td>Description</td>
      <td>100000</td>
    </tr>
    <tr>
      <th>Paper Work</th>
      <td>Description</td>
      <td>15000</td>
    </tr>
    <tr>
      <th>Builder Charges</th>
      <td>Description</td>
      <td>300000</td>
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

st.error("This is a sample report. DO NOT PRINT IT.")