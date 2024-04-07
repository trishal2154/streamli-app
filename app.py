import streamlit as st

picture=st.camera_input("Give an Expression")

if picture is not None:
  st.image(picture)
