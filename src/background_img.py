import streamlit as st
import base64
def add_bg_from_local(image_path, width= None, height = None):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    img_html = f'<img src = "data:image/png;base64,{encoded_string}"'
    if width:
        img_html += f' width = "{width}"'
    if height:
        img_html += f' height = "{height}"'
    img_html += ' style = "display: block; margin: auto; margin-left: 465px;">'
    st.markdown(img_html, unsafe_allow_html= True)