import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.stylable_container import stylable_container

def introduction():
    st.markdown(f'''<h1 style="text-align:center;
                                    color: black;">{"Home 🏠"}</h1>''', unsafe_allow_html=True)
    colored_header(
        color_name="green-70",
        label="",
        description=""
    )
    with stylable_container(
            key="welcome_to_medical",
            css_styles="""
                            {
                                border: 5px solid rgba(49, 51, 63, 0.2);
                                border-radius: 0.5rem;
                                border-color: purple;
                                padding-left: 25px;
                            }
                            """,
    ):
        st.markdown(f'<span style="color:black"> Welcome to Medical AI! Today, you\'ll learn how AI is changing the medical world.</span>', unsafe_allow_html=True)
        st.markdown(f'''<span style="color:black"> **Medical AI** means using :blue-background[computers and machines] to help doctors figure out what’s wrong
                with patients and how to treat them. It can analyze a lot of information really fast, which helps doctors make better
                 decisions.</span>''',unsafe_allow_html=True)
        st.markdown('''<ul style="color:black">
            <li>  <b>Faster Diagnoses</b>: AI helps doctors find out what's wrong with patients more quickly. </li>
            <li> <b>Better Research</b>: AI speeds up the process of discovering new medicines. </li>
            <li> <b>Patient Care</b>: AI helps doctors keep track of patients and make sure they get the right care. </li>
            <li> <b>AI Chatbots</b>: Learn how chatbots (like the one you’ll use) can answer medical questions and give advice. </li>
            </ul>''', unsafe_allow_html=True)

        st.markdown(f'''<span style="color:black"> By the end of this, you'll know how AI is helping doctors and patients. 
                You’ll even get to ask your own questions to a medical AI chatbot!</span>''', unsafe_allow_html=True)