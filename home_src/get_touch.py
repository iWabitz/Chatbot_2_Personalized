import streamlit as st
from streamlit_extras.stylable_container import stylable_container


def get_touch():
    with stylable_container(
            key="get_in_touch",
            css_styles="""
                        {
                            border: 5px solid rgba(49, 51, 63, 0.2);
                            border-radius: 0.5rem;
                            border-color: gray;
                            padding-left: 25px;
                        }
                        """,
    ):
        st.markdown(f'''<h2 style= "color: black;">{"Get In Touch 💬"}</h2>''', unsafe_allow_html=True)
        st.markdown(f'<span style="color:black"> Discord: outpvp</span>', unsafe_allow_html=True)
        st.markdown(f'<span style="color:black"> Email: shiqizhu321@gmail.com</span>', unsafe_allow_html=True)
