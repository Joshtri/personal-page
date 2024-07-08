import streamlit as st

# Set page configuration    
st.set_page_config(page_title="Joshtri Web Page", page_icon=":tada", layout="wide")

# Header section with image
with st.container():
    st.subheader("Hi, I am Yostri")
    col1, col2 = st.columns([3, 1])

    with col1:
        st.title("I'm a student at UNC")
        st.write("I believe technology has the potential to change the world for the better, and I'm excited to be a part of it.")
        st.write("[You can check my GitHub 👈](https://github.com/Joshtri)")

    with col2:
        st.image("profile.jpg", width=200, caption="Profile Image")

# About Me section
with st.container():
    st.write("---")
    st.header("What I Do")
    st.write("##")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write(
            """
            - 🌟 I am an IT student and a full-stack developer freelancer.
            - 💻 I love programming and working on innovative projects.
            - 🌍 I'm interested in developing systems that have a positive impact on society.
            """
        )
    
    with col2:
        st.image("https://media.giphy.com/media/H7f5ZGjvKXBaLbBigO/giphy.gif", width=200)

# Image section
# with st.container():
#     st.write("---")
#     st.header("Gallery")
#     st.write("##")

#     col1, col2, col3 = st.columns(3)

#     with col1:
#         st.image("https://via.placeholder.com/150", caption="Project 1")

#     with col2:
#         st.image("https://via.placeholder.com/150", caption="Project 2")

#     with col3:
#         st.image("https://via.placeholder.com/150", caption="Project 3")
