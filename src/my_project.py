import streamlit as st

def project():
    st.markdown(f'<h1 style="text-align:center;">{"Projects 🚧"}</h1>', unsafe_allow_html=True)

    st.write("Here are some links to see what I have done")
    st.link_button("GitHub", "https://github.com/iWabitz")
    st.link_button("Current :heart: Game", "https://www.minecraft.net/en-us")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write('')
    with col2:
        st.markdown(
            """
        <iframe  
          src="https://stanleyportfolio.streamlit.app?embed=true"
          style="height: 500px; width: = 500px;"
        ></iframe>    """,
            unsafe_allow_html=True
        )
    with col3:
        st.write('')