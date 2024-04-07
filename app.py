import streamlit as st
import cv2
from PIL import Image

picture=st.camera_input("Give an Expression")

if picture is not None:
  picture=Image.open(picture)
  print(picture)
