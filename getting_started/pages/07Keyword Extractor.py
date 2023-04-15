import streamlit as st
from bs4 import BeautifulSoup
import requests

st.set_page_config(page_title="Youtube keyword extractor")

st.markdown("<h1>Youtube keyword extractor</h1>", unsafe_allow_html=True)

url = st.text_input("Enter the url of the video")

if url:
    page = requests.get(url)
    print(page.status_code)

    soup = BeautifulSoup(page.content, 'lxml')
    tit = soup.find("title")
    meta_tag = soup.select("meta[name='keywords']")
    keywords = meta_tag[0]['content']
    st.markdown(f"<h4 style='color: #101820'>{tit.text}</h4>", unsafe_allow_html=True)
    st.markdown()
    st.title("Tags")
    st.markdown(f"<h5 style='color: #101820'>{keywords}</h5>", unsafe_allow_html=True)