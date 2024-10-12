import streamlit as st
from streamlit_extras.stylable_container import stylable_container


def about_me():
    with stylable_container(
            key="my_hobbies_are_soccer",
            css_styles="""
                {
                    border: 5px solid rgba(49, 51, 63, 0.2);
                    border-radius: 0.5rem;
                    border-color: violet;
                    
                    padding-right: 400px;

                }
                """,
    ):
        st.markdown(f'''<h2 style= "color: black;">{"About Me"}</h2>''', unsafe_allow_html=True)
        st.markdown('''<span style="color:black"> I am a 13 year old coding enthusiast, my hobbies are soccer, coding, and playing video games.
        I was born in the US and have two brothers (yes I am the middle child), and my favorite subject in school is PE.
        I know three coding languages, which are Python, Java, and C++.
        I am currently in a FTC robotics team with my older brother where we code Java.
        We would go to outreaches to inspire the community to start coding or doing robotics.</span>''', unsafe_allow_html=True)