import openai
import streamlit as st
import os

api_key = st.secrets.get('OPENAI_API_KEY') or os.environ.get('OPENAI_API_KEY')
client = openai.OpenAI(api_key=api_key)

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://cdn.prod.website-files.com/669add4b1b89b71c0262fede/66a8cc36299ff0a55a524ae1_65e8bacedc46733515f87c04_hypo3.jpeg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

st.write(response.choices[0].message.content)