import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=450)

with col2:
    st.title("Abdulrasheed Shittu")
    content = """ 
     Hi, I am a seasoned IT professional with over 8 years of experience in IT infrastructure and software development. 
     My expertise spans designing, implementing, and managing robust IT systems, as well as developing innovative 
     software solutions. With a strong passion for technology, I stay up-to-date with industry trends and advancements. 
     Throughout my career, I have successfully delivered numerous projects, leveraging my technical skills to drive business
      growth and improvement..
     """
    st.info(content)

