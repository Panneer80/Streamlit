# import core
import streamlit as st
import os
from PIL import Image
import pandas as pd
import docx2txt # process pdfs
from PyPDF2 import PdfReader
# import pdfplumber

@st.cache_data
def load_image(image_file):
    img = Image.open(image_file)
    return img

def read_pdf(file):
    pdfReader = PdfReader(file)
    count = len(pdfReader.pages)
    all_page_text = ""
    for i in range(count):
        page = pdfReader.pages[i]
        all_page_text += page.extract_text()
    return all_page_text

def file_manager():
    st.text("File Manager")

    menu=["Home", "Dataset","Document Files","About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        image_file=st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
        if image_file is not None:
            #to see details
            # st.write(type(image_file))
            # st.write(dir(image_file))
            file_details = {
                "file name": image_file.name,
                "file type": image_file.type,
                "file size":image_file.size
            }
            st.write(file_details)
            st.image(load_image(image_file))
            #saving file to tempDir
            with open(os.path.join("tempDir",image_file.name), "wb") as f:
                f.write(image_file.getbuffer())
            st.success("File Saved")
# upload multiple files
    elif choice == "Dataset":
        st.subheader("Dataset")
        data_file = st.file_uploader("Upload CSV",type=["csv"], accept_multiple_files=True)
        if data_file is not None:
            for file in data_file:
                file_details = {
                    "file name": file.name,
                    "file type": file.type,
                    "file size":file.size
                }
                st.write(file_details)
                df = pd.read_csv(file)
                st.dataframe(df)

    elif choice == "Document Files":
        st.subheader("Document Files")
        docx_file = st.file_uploader("Upload Document", type=["pdf","docx","txt"])
        if st.button("Process"):
            if docx_file is not None:
                file_type = docx_file.type
                st.write(file_type)
                if file_type == "text/plain":
                    #read as bytes
                    # raw_text = docx_file.read()
                    # st.write(raw_text) # works but in bytes
                    #read as string (decode bytest to string)
                    raw_text = str(docx_file.read(),"utf-8")
                    st.write(raw_text) #works
                    st.text(raw_text) # works fine with formatting
                elif file_type == "application/pdf":
                    # try:
                    #     with pdfplumber.open(docx_file) as pdf:
                    #         pages = pdf.pages[1]
                    #         st.write(pages.extract_text())
                    # except:
                    #     st.write("None")
                    raw_text = read_pdf(docx_file)
                    st.write(raw_text)
                else:
                    raw_text = docx2txt.process(docx_file)
                    st.write(raw_text) # works file with alingment
                    st.text(raw_text) # works
    elif choice == "About":
        st.subheader("About")