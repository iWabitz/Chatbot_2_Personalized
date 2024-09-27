

import streamlit as st
from home_src.about_me import about_me
from home_src.timeline import line_data
from home_src.skills_technology import skills_technology
from home_src.get_touch import get_touch
from streamlit_extras.colored_header import colored_header

st.set_page_config(layout="wide")


def home():
    st.title('Home 🏠')
    colored_header(
        label="",
        description="",
        color_name="green-70"
    )
    st.write("Welcome to Shawn AI! Today, you'll learn how AI is changing the medical world.")

    st.write("""
        Medical AI means using computers and machines to help doctors figure out what’s wrong with patients and how to treat them. 
        It can analyze a lot of information really fast, which helps doctors make better decisions.
    """)
    
    st.write("""
    - Faster Diagnoses: AI helps doctors find out what's wrong with patients more quickly.
    - Better Research: AI speeds up the process of discovering new medicines.
    - Patient Care: AI helps doctors keep track of patients and make sure they get the right care.
    - AI Chatbots: Learn how chatbots (like the one you’ll use) can answer medical questions and give advice.
    """)
    
    st.write("""
        By the end of this, you'll know how AI is helping doctors and patients. 
        You’ll even get to ask your own questions to a medical AI chatbot!
    """)
############################################################################## About Me
    about_me()    
############################################################################## Timeline
    line_data()
############################################################################## Skills & Technologies
    skills_technology()
############################################################################## Services
    st.header("Services")
    
    

############################################################################## Get In Touch
    get_touch()
############################################################################## END

