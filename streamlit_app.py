# import core
import streamlit as st

#import dependent packages
from learning import basics, widgets_tut, media, plotting, file_process,file_download

st.set_page_config(page_title="Developer: Panneer Selvam R", 
                   page_icon="🐺",
                   initial_sidebar_state='auto',
                layout='centered'
                   )

def main():
    if "role" not in st.session_state:
        st.session_state.role = None

    ROLES = [None, "user", "admin"]


    def login():

        st.header("Log in")
        role = st.selectbox("Choose your role", ROLES)

        if st.button("Log in"):
            st.session_state.role = role
            st.rerun()


    def logout():
        st.session_state.role = None
        st.rerun()


    role = st.session_state.role

    logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

    task_manager = st.Page(
        "modules/task_manager/task_manager.py",
        title="Task Manager",
        icon=":material/task:",
        url_path="home"
       
    )

    profile = st.Page(
        "modules/about_me/about_me.py",
        title="Profile",
        icon=":material/person_add:",
        url_path="admin", 
        default=True
    )

    # st.logo("modules/about_me/Photo_Panneer.jpg")
    page_dict = {}
    page_dict["About Me"] = [profile]
    page_dict["My Apps"] = [task_manager]
    pg = st.navigation(page_dict )
    pg.run()

if __name__ == '__main__':
    main()




