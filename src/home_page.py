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
    
    st.header("Timeline")
    items = [
    {"id": 1, "content": "Born in California", "start": "2011-7-20"},
    {"id": 2, "content": "Started playing soccer", "start": "2016-5-20"},
    {"id": 3, "content": "Got a little brother", "start": "2018-6-20"},
    {"id": 4, "content": "Started Coding", "start": "2021-9-18"},
    {"id": 5, "content": "Learning about AI", "start": "2024-8-15"},
    ]

    timeline = st_timeline(items, groups=[], options={}, height="150px")
    st.subheader("Selected item")
    st.write(timeline)
    
    st.title("Skills")
    st.write("There are many skills you need to know to be able to code an AI chatbot using streamlit")
    
    with st.expander("Python Programming"):
        st.write('''
        Proficiency in Python, as Streamlit is a Python-based framework.
        Experience with data structures, control flow, and basic algorithms.
        ''')
        st.image("data:image/jpeg;base64,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")
    with st.expander("API Interaction"):
        st.write('''
            Ability to work with APIs and use the chatbot to integrate with external services.
        ''')
        st.image("https://cdn.prod.website-files.com/5dd827bbc07b1656e06b16d8/649c41b13040c07f7437d79d_Depositphotos_417720198_L%20(1).jpg")
    with st.expander("Git and Version Control"):
        st.write('''
            Basic understanding of Git for version control and collaboration.
        ''')
        st.image("data:image/png;base64,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")
    with st.expander("Debugging Skills"):
        st.write('''
            Ability to troubleshoot and debug errors that may arise during development.
        ''')
        st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fillustrations%2Funtangling&psig=AOvVaw38F-QIQ4R1qGY1uGDPMjxZ&ust=1726014108886000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCNCQs-WNt4gDFQAAAAAdAAAAABAE")
        
    st.title("Technologies")
    st.write("These technologies can give you an environment to code and be more efficient.")
    with st.expander("Streamlit"):
        st.write('''
            Knowledge of Streamlit library for building web applications quickly.
            Understanding the Streamlit API for creating forms, buttons, text inputs, etc.
        ''')
        st.image("data:image/png;base64,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")
        
    with st.expander("Environment Management"):
        st.write('''
            Using tools like virtual environments for package management.
        ''')
    
        
    st.header("Services")
    
    
    
    
    st.header("Get In Touch")
    st.write("Discord: OutPvP")
    st.write("Email: shiqizhu321@gmail.com")
    
