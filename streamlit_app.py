# import core
import streamlit as st

#import dependent packages
from learning import basics, widgets_tut, media, plotting, file_process,file_download

st.set_page_config(page_title="Developer: Panneer Selvam R 🛠️", 
                   page_icon="🐺",
                   initial_sidebar_state='auto',
                layout='centered'
                   )

def main():
    # basics.basics_text()
    # widgets_tut.widget_t()
    # media.media_t()
    #plotting.charts_t()
    #file_process.file_manager()
    # file_download.main()
    # st.title("Welcome!")

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
        "modules/about_me.py",
        title="Profile",
        icon=":material/person_add:",
        url_path="admin", 
        default=True
    )

    # st.logo("🐺")
    page_dict = {}
    page_dict["About Me"] = [profile]
    page_dict["My Apps"] = [task_manager]

    # page_dict = {}
    # if st.session_state.role in ["admin"]:
    #     page_dict["Admin"] = [admin]
    # if st.session_state.role in ["user"]:
    #     page_dict["Home"] = [home]

    pg = st.navigation(page_dict )
    # if len(page_dict) > 0:
    #     pg = st.navigation(page_dict | {"Log out": [logout_page]}  )
    # else:
    #     pg = st.navigation([st.Page(login)])
        

    pg.run()

if __name__ == '__main__':
    main()




