import streamlit as st

st.subheader("WORK IN PROGRESS!")
# import pandas as pd
# from sqlalchemy.sql import text
# import json

# st.text("Task List")
# file = open("modules/task_manager/task_data.json", 'r')
# list_data = json.load(file)
# selected_coloums = ['id','title','assigned to']

# #st.dataframe(list_data[selected_coloums].set_index('id'))

# conn = st.connection('tasks_db', type='sql')

# # Insert some data with conn.session.
# with conn.session as s:
#     s.execute(text("CREATE TABLE IF NOT EXISTS task_main (id INTEGER, Title TEXT, Description TEXT, Assigned_To TEXT, Status TEXT);"))
#     #s.execute('DELETE FROM pet_owners;')
#     #task_data = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
#     for k in list_data:
#         s.execute(
#             text('INSERT INTO task_main (Title, Description,Assigned_To,Status ) VALUES (:title, :description, :assignedto, :status);'),
#             params=dict(title=k['title'], description=k['description'], assignedto=k['assigned to'], status='new')
#         )
#     s.commit()

# # Query and display the data you inserted
# task_main_df = conn.query('select * from task_main')
# st.dataframe(task_main_df)
