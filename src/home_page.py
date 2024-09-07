import streamlit as st
from streamlit_timeline import st_timeline

def home():
    st.title('Shawn AI 🤖')
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

    st.header("About Me")
    st.write("""I am a 13 year old coding enthusiast, my hobbies are soccer, coding, and playing video games.
I was born in the US and have two brothers (yes I am the middle child), and my favorite subject in school is PE.
I know three coding languages, which are Python, Java, and C++.
I am currently in a FTC robotics team with my older brother where we code Java.
We would go to outreaches to inspire the community to start coding or doing robotics.
""")
    items = [
        {"id": 1, "content": "2022-10-20", "start": "2022-10-20"},
        {"id": 2, "content": "2022-10-09", "start": "2022-10-09"},
        {"id": 3, "content": "2022-10-18", "start": "2022-10-18"},
        {"id": 4, "content": "2022-10-16", "start": "2022-10-16"},
        {"id": 5, "content": "2022-10-25", "start": "2022-10-25"},
        {"id": 6, "content": "2022-10-27", "start": "2022-10-27"},
    ]
    timeline = st_timeline(items, groups=[], options={}, height="300px")
    st.subheader("Selected item")
    st.write(timeline)
##    items = [
##    {"id": 1, "content": "Born in California", "start": "2011-7-20"},
##    {"id": 2, "content": "Started playing soccer", "start": "2016-5-20"},
##    {"id": 3, "content": "Got a little brother", "start": "2018-6-20"},
##    {"id": 4, "content": "Started Coding", "start": "2021-9-18"},
##    {"id": 5, "content": "Learning about AI", "start": "2024-8-15"},
##    ]
##
##    timeline = st_timeline(items, height="300px")
##    st.subheader("Selected item")
##    st.write(timeline)
