import streamlit as st
import pandas as pd

#Working with Text
def basics_text():
    # st.text("Hello this is a simple text")
    # name = "Panneer"
    # st.text("My name is {}".format(name))
    # #header
    # st.header("This is a header")
    # #subheader
    # st.subheader("this is a subheader")
    # #title
    # st.title("this is a title")
    # # markdown
    # st.markdown("## This is a markdown")

    # #display colored text / Bootstraps Alert
    # st.success("Successful")
    # st.warning("Warning")
    # st.info("This is info")
    # st.error("this is an error")
    # st.exception("this is an exception")

    # #super function
    # st.write("## this is a text")
    # st.write( 1+2)
    # st.write(dir(st))
    # #help info
    # st.help(range)

    #display data
    df = pd.read_csv("C:\\work\\Streamlit_Code\\LearnStreamlit\\Module01\\iris.csv")
    # print top 5 rows
    # st.write(df.head())
    # Scrollable/expandable/downloadable df
    # st.dataframe(df, 700,500)
    # adding color style from Pandas
    # st.dataframe(df.style.highlight_max(axis=0))
    # display it as static table
    # st.table(df)

    #display json
    st.json({'key':'value'})

    #display code
    my_code = """
    def sayhello():
    print("Hellow Streamlit Lovers")
    """
    st.code(my_code, language='python')