import streamlit as st

# from modules.civil_boq.plastering_work import plastering_work
from modules.civil_boq.tiles_work import tiles_work
from modules.civil_boq.doors_windows import door_window_work
from modules.civil_boq.masonary_work import masonary_work
from modules.civil_boq.price_setting import set_price
from modules.civil_boq.concrete_work import concrete_work

st.set_page_config(page_title="Civil BOQ", 
                   page_icon="🐺",
                   initial_sidebar_state='auto',
                layout='wide'
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


    welcome_page = st.Page(
        "modules/civil_boq/welcome_page.py",
        title="Home",
        icon=":material/task:",
        url_path="home",
        default=True
       
    )

    boq_generator = st.Page(
        "modules/civil_boq/boq_page.py",
        title="Generate BOQ",
        icon=":material/task:",
        url_path="boq",
        default=False
       
    )

    your_boqs = st.Page(
        "modules/task_manager/task_manager.py",
        title="Your BOQ's",
        icon=":material/person_add:",
        url_path="saved", 
        default=False
    )

    about_me = st.Page(
        "modules/about_me/about_me.py",
        title="About me",
        icon=":material/person_add:",
        url_path="about_me", 
        default=False
    )

    page_dict = {}

    page_dict["BOQ Generator"] = [welcome_page,boq_generator, your_boqs]
    page_dict["Developer"] = [about_me]
    pg = st.navigation(page_dict )
    pg.run()



if __name__ == '__main__':
    main()




