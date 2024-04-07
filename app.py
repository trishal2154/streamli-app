import streamlit as st
import cv2

picture=st.camera_input("Give an Expression")

if picture is not None:
  cv2.imshow(picture)
