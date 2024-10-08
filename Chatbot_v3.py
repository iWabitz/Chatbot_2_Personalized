import streamlit as st
import openai
import time
import os
from src.home_page import home
from src.my_project import project
import base64
from old.chat_time import generate_time
from src.background_img import add_bg_from_local

st.set_page_config(layout="wide")



ASSISTANT_ID='asst_YnUwM7GQ78sRQuzEfmOd8miQ'
THREAD_ID='thread_JaFFQGg5kdg7ddtLMsQXzK5l'

api_key = st.secrets.get('OPENAI_API_KEY') or os.environ.get('OPENAI_API_KEY')

if not api_key:
    st.error('OPENAI API Key was not found :(')
    st.stop()

client = openai.OpenAI(api_key=api_key)

# Main Chat Interface 

if 'messages' not in st.session_state:
    st.session_state.messages = []
    
def get_assistant_response(assistant_id, thread_id, user_input):
    try:
        current_time = str(generate_time())
        # Add the user's message to the thread
        client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=current_time+user_input
        )
        run = client.beta.threads.runs.create(
                thread_id=thread_id,
                assistant_id=assistant_id
        )

        # wait for the run to complete
        while True:
            run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id = run.id)

            if run_status.status == 'completed':
                break
            time.sleep(1)

        # Retrieve the Assistant's message
        messages = client.beta.threads.messages.list(thread_id=thread_id)

        return messages.data[0].content[0].text.value
    except Exception as e:
        st.error(f"Error getting assistant response: {str(e)}")
        return "I\m sorry but that did not work :("
    
def display_chatbot():
    st.markdown(f'<h1 style="text-align:center;">{"Medical AI 🏥"}</h1>', unsafe_allow_html=True)
    add_bg_from_local('./images/heartbeat.png', width = 400, height = 400)
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask me anything!")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = get_assistant_response(
                ASSISTANT_ID,
                THREAD_ID,  
                prompt
            )
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

def main():
    
    with st.sidebar:
        st.title("Medical Industry AI Integration")
    sections = ['Home', 'Chatbot', 'Projects']
    selected_section = st.sidebar.radio('Navigation', sections)
    if selected_section == 'Home':
        home()
    elif selected_section == 'Chatbot':
        display_chatbot()
    elif selected_section == 'Projects':
        project()

if __name__ == "__main__":
    main()














    
