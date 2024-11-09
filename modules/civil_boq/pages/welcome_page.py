import streamlit as st


st.header("Welcome to BOQ Generator")
st.markdown("##### Your Fast-Track Solution to Accurate Construction Estimates")
if st.button("Generate Now!", type="primary", key="generate_btn_page_start"):
    st.switch_page("modules/civil_boq/pages/boq_page.py")

st.html(
"""
    <section>
        <h2>What is a BOQ?</h2>
        <p>A Bill of Quantities (BOQ) is a comprehensive document that lists all the materials, labor, and other costs required for a construction project. It breaks down every element, from building materials like concrete and steel to the finishing touches like paint and fixtures. A well-prepared BOQ helps to:</p>
        <ul>
            <li><strong>Accurately Estimate Costs:</strong> Know exactly how much your project will cost before starting.</li>
            <li><strong>Streamline Procurement:</strong> Make ordering materials simpler and more organized.</li>
            <li><strong>Minimize Wastage:</strong> Avoid over-purchasing materials by estimating quantities precisely.</li>
            <li><strong>Improve Project Planning:</strong> Ensure all aspects of the project are accounted for in terms of materials and labor.</li>
        </ul>
    </section>

""")
# st.html("""
#     <h2>Watch Our Tutorial on BOQ Generation</h2>
#     <p>Learn more about how to create a Bill of Quantities quickly and accurately by watching our tutorial video below:</p>
# """) 

# VIDEO_URL = "https://youtu.be/M4xtXdg_ibU"
# container, _, _  = st.columns(3)
# container.video(data=VIDEO_URL)

st.html("""
    <section>
        <h2>Why Use BOQ Generator?</h2>
        <p>Creating a BOQ manually can be time-consuming, complex, and prone to errors. With our BOQ Generator, you can:</p>
        <ul>
            <li><strong>Quickly Generate Detailed BOQs:</strong> Our tool allows you to enter project details and specifications, then automatically calculates material quantities and costs based on standard rates.</li>
            <li><strong>Customize Your Estimates:</strong> Adjust quantities, add items, or modify unit costs to reflect the specifics of your project.</li>
            <li><strong>Download Professional BOQ Documents:</strong> Export your completed BOQ as a PDF or Excel file for easy sharing with clients, contractors, or suppliers.</li>
            <li><strong>Save Time and Effort:</strong> Skip the tedious manual calculations and let our automated tool do the work for you.</li>
        </ul>
    </section>

    <section>
        <h2>How Does It Work?</h2>
        <ol>
            <li><strong>Enter Project Details:</strong> Provide basic project information, such as the type of construction, area dimensions, and specifications.</li>
            <li><strong>Select Materials and Work Items:</strong> Choose from a wide range of pre-defined materials and construction tasks commonly used in the industry.</li>
            <li><strong>Get Instant Estimates:</strong> Our algorithm calculates quantities and costs based on standard industry data, giving you a BOQ ready for review.</li>
            <li><strong>Download or Share Your BOQ:</strong> Download the BOQ in PDF or Excel format, or share it directly with your team or client.</li>
        </ol>
    </section> 
    """
)

if st.button("Generate Now!", type="primary", key="generate_btn_page_end"):
    st.switch_page("modules/civil_boq/pages/boq_page.py")