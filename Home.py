import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=400)

with col2:
    st.title("Abdulrasheed Shittu")
    content = """ 
     Hi,I am Abdulrasheed, a seasoned IT professional with over 8 years of experience in IT infrastructure and software
     development. My expertise spans designing, implementing, and managing robust IT systems, as well as developing 
     innovative software solutions.
     With a strong passion for technology, I stay up-to-date with industry trends and advancements. 
     Throughout my career, I have successfully delivered numerous projects, leveraging my technical skills to drive business
     growth and improvement..
     """
    st.info(content)

content2 = """ 
Below you can find some of the apps I have built in python. Feel free to contact me. 
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

