import streamlit as st
from streamlit_timeline import st_timeline

def line_data():
    st.header("Timeline")
    items = [
        {"id": 1, "content": "Born in California", "start": "2011-7-20"},
        {"id": 2, "content": "Started playing soccer", "start": "2016-5-20"},
        {"id": 3, "content": "Got a little brother", "start": "2018-6-20"},
        {"id": 4, "content": "Started Coding", "start": "2021-9-18"},
        {"id": 5, "content": "Joined a Robotics Team", "start": "9/30/2021"},
        {"id": 6, "content": "Learning about AI", "start": "2024-8-15"},
    ]

    timeline = st_timeline(items, groups=[], options={}, height="150px")
    st.subheader("Selected item")
    st.write(timeline)