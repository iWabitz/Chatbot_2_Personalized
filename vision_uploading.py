import base64
import openai
import streamlit as st
import os
from io import StringIO

api_key = st.secrets.get('OPENAI_API_KEY') or os.environ.get('OPENAI_API_KEY')
client = openai.OpenAI(api_key=api_key)


def file_handle():
    uploaded_files = st.file_uploader(
        "Choose a CSV file", accept_multiple_files=True
    )

    for uploaded_file in uploaded_files:
        st.write("filename:", uploaded_file.name)
        return uploaded_file.name
# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


def assistant_response(path):
    # Path to your image
    image_path = f"./images/{path}"

    # Getting the base64 string
    base64_image = encode_image(image_path)

    response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "What is in this image?",
            },
            {
              "type": "image_url",
              "image_url": {
                "url":  f"data:image/jpeg;base64,{base64_image}"
              },
            },
          ],
        }
      ],
    )

    st.write(response.choices[0].message.content)

def main():
    handle_path = file_handle()
    assistant_response(handle_path)

if __name__ == "__main__":
    main()