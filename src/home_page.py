import streamlit as st
from home_src.about_me import about_me
from home_src.timeline import line_data
from home_src.skills_technology import skills_technology
from home_src.get_touch import get_touch
from home_src.intro import introduction
from home_src.services import serv
import base64

def add_bg_from_local():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(https://media.discordapp.net/attachments/840396747729928214/1291910566394331166/sky.jpg?ex=6701d0f9&is=67007f79&hm=1ef1e3bb00d0efe71f15fd59c6f7913216fb97301e67f002f26292aa4c1e6931&=&format=webp&width=906&height=602);
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )



def home():


    add_bg_from_local()


############################################################################## Introduction
    introduction()
############################################################################## About Me
    about_me()    
############################################################################## Timeline
    line_data()
############################################################################## Skills & Technologies
    skills_technology()
############################################################################## Services
    serv()
############################################################################## Get In Touch
    get_touch()
############################################################################## END

