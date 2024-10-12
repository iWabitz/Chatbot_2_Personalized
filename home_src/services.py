import streamlit as st

def serv():
    st.markdown(f'''<h2 style= "color: black;">{"Services 📝"}</h2>''', unsafe_allow_html=True)
    tabs_1, tabs_2, tabs_3 = st.tabs(["Teach Coding Workshops 🛠️", "Train Soccer ⚽", "Robot Assistance 🤖"])
    with tabs_1:
        st.markdown(f'''<h2 style= "color: black;">{"Teach Coding Workshops 🛠️"}</h2>''', unsafe_allow_html=True)
        st.markdown(
            f'''<span style="color:black"> In my robotics team, I go to many events where improved my public speaking. I taught people how to drive our robot and spoke loudly and clearly when showcasing our bot to judges.
        I have also taught coding workshops during FTC Kickoffs, where I taught new teams how to code block code.</span>''',
            unsafe_allow_html=True)

    with tabs_2:

        st.markdown(f'''<h2 style= "color: black;">{"Train Soccer ⚽"}</h2>''', unsafe_allow_html=True)
        st.markdown(
            f'''<span style="color:black"> I love playing soccer outside, but having another person to practice with makes it so much better. I can coach smaller kids with their passing skills, dribbling skills,
        and shooting skills. I have experience in this because my little brother loves playing soccer and wants to improve, so I practice with him everyday outside.</span>''',
            unsafe_allow_html=True)
    with tabs_3:

        st.markdown(f'''<h2 style= "color: black;">{"Robot Assistance 🤖"}</h2>''', unsafe_allow_html=True)
        st.markdown(
            f'''<span style="color:black"> I could give ideas on how to improve robots, and mechanisms they should use to make their scoring more accurate. For example, they could use sensors such as cameras to detect where
        they need to go and position their robot more accurately if their game uses april tags.</span>''',
            unsafe_allow_html=True)
        st.write("""""")