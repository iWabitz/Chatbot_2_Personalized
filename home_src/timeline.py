import streamlit as st
from streamlit_timeline import st_timeline
from streamlit_extras.stylable_container import stylable_container

def line_data():
    with stylable_container(
            key="timeline",
            css_styles="""
                        {
                            border: 5px solid rgba(49, 51, 63, 0.2);
                            border-radius: 0.5rem;
                            border-color: pink;
                        }
                        """,
    ):
        st.markdown(f'''<h2 style= "color: black;">{"Timeline"}</h2>''', unsafe_allow_html=True)


        items = [
            {"id": 1, "content": "Born in California", "start": "2011-7-20"},
            {"id": 2, "content": "Started playing soccer", "start": "2016-5-20"},
            {"id": 3, "content": "Got a little brother", "start": "2018-6-20"},
            {"id": 4, "content": "Started Coding", "start": "2021-9-18"},
            {"id": 5, "content": "Joined a Robotics Team", "start": "9/30/2021"},
            {"id": 6, "content": "Learning about AI", "start": "2024-8-15"},
        ]

        timeline = st_timeline(items, groups=[], options={}, height="150px")
        st.markdown(f'''<h3 style= "color: black;">{"Selected item️"}</h3>''', unsafe_allow_html=True)
        st.markdown(f'<span style="color:black"> {timeline}</span>', unsafe_allow_html=True)
