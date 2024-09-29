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

    civil_boq = st.Page(
        "modules/civil_boq/landing.py",
        title="Data Entry",
        icon=":material/task:",
        url_path="boq",
        default=True
       
    )

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
        default=False
    )

    # st.logo("modules/about_me/Photo_Panneer.jpg")
    page_dict = {}

    page_dict["Civil BOQ"] = [civil_boq, task_manager]
    page_dict["About Me"] = [profile]
    pg = st.navigation(page_dict )
    pg.run()

if __name__ == '__main__':
    main()




