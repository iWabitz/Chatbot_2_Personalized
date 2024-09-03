import streamlit as st
def home():
    st.title('Shawn AI 🤖')
    st.write("You will be learning about Medical AI Chat Interface")
    st.write("At the end, you could learn and ask questions about Medicine to an AI Chatbot!")
    st.write("First, let's choose a color for the background!")
    color = st.color_picker("Choose A Color", "#00f900")
    st.write("The current color is", color)
    st.write("Great Choice!")
    st.markdown(f"""
        <style>
        .stForm {
                background-color: {color};
        }
        </style>
    """, unsafe_allow_html=True)
