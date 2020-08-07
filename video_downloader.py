from flask import Flask
import streamlit as st
from pytube import YouTube
import os

st.title("Video Downloader")

# st.markdown("Select Download Location")
# file_path = st.text_input("Enter File Download Location")
# st.markdown(file_path + str(type(file_path)))
# download_path = os.path(file_path)
#

select = st.selectbox("Select Download mode :", ["Select", "Single Video", "Entire Playlist"])
if select == "Single Video":
    video_url = str(st.text_input("Enter the video link"))
    if video_url:
        try:
            yt = YouTube(video_url)
            yt.streams.first().download()
        except:
            st.markdown("Exception occured while downloading")
        else:
            st.markdown("Download completed.. 😊")
elif select == "Entire Playlist":
    st.markdown("Coming soon")