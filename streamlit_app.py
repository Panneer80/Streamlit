import streamlit as st

from modules.civil_boq.plastering_work import plastering_work
from modules.civil_boq.masonary_work import masonary_work
from modules.civil_boq.price_setting import set_price
from modules.civil_boq.concrete_work import concrete_work

st.set_page_config(page_title="Civil BOQ", 
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


    @st.cache_data
    def local_css(file_name):
        with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("modules/civil_boq/style.css")
    st.subheader("Bill Of Quantity (BOQ) | Data entry")
    set_price(st)
    concrete_work(st)
    masonary_work(st)
    plastering_work(st)

    # civil_boq = st.Page(
    #     "modules/civil_boq/landing.py",
    #     title="Data Entry",
    #     icon=":material/task:",
    #     url_path="boq",
    #     default=True
       
    # )

    # task_manager = st.Page(
    #     "modules/task_manager/task_manager.py",
    #     title="Task Manager",
    #     icon=":material/task:",
    #     url_path="home"
       
    # )

    # profile = st.Page(
    #     "modules/about_me/about_me.py",
    #     title="Profile",
    #     icon=":material/person_add:",
    #     url_path="admin", 
    #     default=False
    # )

    # # st.logo("modules/about_me/Photo_Panneer.jpg")
    # page_dict = {}

    # page_dict["Civil BOQ"] = [civil_boq]
    # #page_dict["About Me"] = [profile]
    # pg = st.navigation(page_dict )
    # pg.run()



if __name__ == '__main__':
    main()




