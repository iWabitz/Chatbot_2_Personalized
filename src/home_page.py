import streamlit as st
from home_src.about_me import about_me
from home_src.timeline import line_data
from home_src.skills_technology import skills_technology
from home_src.get_touch import get_touch
from home_src.intro import introduction

st.set_page_config(layout="wide")



def home():


############################################################################## Introduction
    introduction()
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

