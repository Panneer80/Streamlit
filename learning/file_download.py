import streamlit as st
import streamlit.components as stc
import base64
import time
import pandas as pd

timestr = time.strftime("%d%m%Y-%H%M%S")

def text_downloader(raw_text):
    b64 = base64.b64encode(raw_text.encode()).decode()
    new_filename = "new_text_file_{}_.txt".format(timestr)
    st.markdown("#### Download File ###")
    href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">click here!!</a>'
    st.markdown(href, unsafe_allow_html=True)
def csv_downloader(data):
    csvfile = data.to_csv()
    b64 = base64.b64encode(csvfile.encode()).decode()
    new_filename = "new_csv_file_{}_.csv".format(timestr)
    st.markdown("#### Download File ###")
    href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">click here!!</a>'
    st.markdown(href, unsafe_allow_html=True)

def main():
    menu = ["Home","CSV","About"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        my_text = st.text_area("Your Message")
        if st.button("Save"):
            st.write(my_text)
            text_downloader(my_text)
    elif choice == "CSV":
        df = pd.read_csv("C:\\Users\\PanneerSelvamR\\Desktop\\234_3711795.csv")
        st.dataframe(df)
        csv_downloader(df)
    else:
        st.subheader("About")

if __name__ == '__main__':
    main()