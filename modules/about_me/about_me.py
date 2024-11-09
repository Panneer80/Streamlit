import streamlit as st
st.text("This website is developed and maintained by:")
st.divider()
st.markdown("##### Panneer Selvam R")

st.markdown("###### Senior Python Developer & Automation Architect")

st.text("""
        A seasoned Python developer with extensive experience in automation, microservices, 
        and system integration. Proficient in designing and implementing scalable solutions 
        using Python, Streamlit, SQLAlchemy, Flask, FastAPI, and Docker. Expertise in 
        developing REST APIs, automating tasks with tools like Ansible, and working with 
        various databases including MSSQL, PostgreSQL, and MySQL. Successfully completed 
        over 70 task automations, providing technical leadership in complex projects.""")
st.divider()
st.markdown("###### Support me")
st.text(""" 
        If you find my content valuable and would like to support me, you can make a donation by scanning the QR code below. 
        Every contribution, big or small, helps me cover hosting, maintenance, and development costs.""")

st.image("modules/about_me/images/My_QR_Code.jpeg", width=400)
st.divider()
st.markdown("###### Thank You!")
# st.markdown("###### Check my projects:")
# st.page_link(label='Task Manager',page='modules/task_manager/task_manager.py',icon=":material/task:")   