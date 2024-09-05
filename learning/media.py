import streamlit as st
from PIL import Image

#working with media
def media_t():
    # # #display image using pillow
    # img = Image.open("C:\\work\\Streamlit_Code\\LearnStreamlit\\Module01\\data\\image_01.jpg")
    # st.image(img, use_column_width=False, width=300)
    # # st.image(url)

    # # video
    # video_file = open("C:\\work\\Streamlit_Code\\LearnStreamlit\\Module01\\data\\secret_of_success.mp4", "rb").read()
    # st.video(video_file)

    #audio
    audio_file= open("C:\\work\Streamlit_Code\\LearnStreamlit\\Module01\\data\\song.mp3","rb")
    st.audio(audio_file.read())