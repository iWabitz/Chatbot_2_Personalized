import streamlit as st

st.title("My Map")

# Display an embedded Google Map
st.markdown(
    """
<iframe
  src="https://stanleyportfolio.streamlit.app?embed=true"
  style="height: 450px; width: 100%;"
></iframe>    """,
    unsafe_allow_html=True
)