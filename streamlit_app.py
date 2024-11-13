import streamlit as st

     
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
    local_css("modules/civil_boq/css/style.css")

    # with st.sidebar:
    #     st.logo(image="modules/civil_boq/images/wolf_1f43a.png")

    welcome_page = st.Page(
        "modules/civil_boq/pages/welcome_page.py",
        title="Home",
        icon=":material/home:",
        url_path="home",
        default=True
       
    )

    boq_generator = st.Page(
        "modules/civil_boq/pages/boq_page.py",
        title="Generate BOQ",
        icon=":material/task:",
        url_path="boq",
        default=False
       
    )

    your_boqs = st.Page(
        "modules/task_manager/task_manager.py",
        title="Your BOQ's",
        icon=":material/list:",
        url_path="saved", 
        default=False
    )

    about_me = st.Page(
        "modules/about_me/about_me.py",
        title="About Developer",
        icon=":material/person:",
        url_path="about_me", 
        default=False
    )

    feedback = st.Page(
        "modules/about_me/feedback.py",
        title="Give Feedback",
        icon=":material/feedback:",
        url_path="feedback", 
        default=False
    )
    
    print_pdf = st.Page(
        "modules/civil_boq/pages/print_page.py",
        title="Print/Download BOQ",
        icon=":material/print:",
        url_path="print", 
        default=False
    )

    formulas = st.Page(
        "modules/civil_boq/pages/formulas.py",
        title="Formulas",
        icon=":material/calculate:",
        url_path="formulas", 
        default=False
    )    

    sample_report = st.Page(
        "modules/civil_boq/pages/sample_report.py",
        title="Sample Report",
        icon=":material/summarize:",
        url_path="sample_report", 
        default=False
    )    
    page_dict = {}

    page_dict["BOQ Generator"] = [welcome_page,boq_generator,print_pdf,your_boqs,formulas, sample_report]
    page_dict["Contact Us"] = [about_me, feedback]
    # if ("generate_pressed" in st.session_state):
    # page_dict["BOQ Generator"] +=  [print_pdf ]
    pg = st.navigation(page_dict )
    pg.run()



if __name__ == '__main__':
    main()




