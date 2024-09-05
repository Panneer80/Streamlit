import streamlit as st

#working with Widgets

def widget_t():
    # #Buttons
    # name = "Panneer"
    # if st.button("Submit", key='button01'):
    #     st.write("Hello {} !!".format(name.upper()))
    # if st.button("Submit", key='button02'):
    #     st.write("Hello {} !!".format(name.lower()))        
    # # radio button
    # status = st.radio("Select one", (10, 20, 30))
    # if status == 30:
    #     st.error("Critical")
    # elif status == 20:
    #     st.warning("Warning")
    # else:
    #     st.info("Ok")
    # #checkbox
    # if st.checkbox("available"):
    #     st.text("OK")
    #Expander
    # expand = st.expander("Expand", icon=":material/info:")
    # if expand.checkbox("accept"):
    #     expand.info("Accepted Terms and conditions")
        
    # # select/ multiple
    # my_lang = ["python", "java", "C#", "Js"]
    # choide = st.selectbox("Language", my_lang, )

    # st.multiselect("Select",my_lang)

    # # slider int/fload/dates
    # age = st.slider("Age", 1,100)

    # #slider any data type
    # clor = st.select_slider("Chose color", options=["red", "green", "blue", "pink"])
    st.text_input("Username",placeholder="Full Name", max_chars=30, )
    st.text_input("Password", type='password')

    #Text Area
    message = st.text_area("Enter Message", height=200)
    st.write(message)
    # Number
    st.number_input("Enter Number", 1,25,)
    #date input
    myappointment = st.date_input("Select Date")

    #time input
    st.time_input("Time")

    #color picker
    st.color_picker("Color")