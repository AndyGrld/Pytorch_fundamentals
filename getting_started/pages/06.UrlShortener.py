import streamlit as st
import pyshorteners as pyst
import pyperclip


def copying(url):
    pyperclip.copy(url)


shortener = pyst.Shortener()

st.markdown("<h1>URL SHORTENER</h1>", unsafe_allow_html=True)
st.markdown("---")

form = st.form("name")
url = form.text_input("Enter url")
btn = form.form_submit_button("Shorten")

short = st.empty()

if btn:
    short_url = shortener.tinyurl.short(url)
    short.markdown(f"<h6>Shortened Url</h6>", unsafe_allow_html=True)
    short.markdown(f"<h6>{short_url}</h6>", unsafe_allow_html=True)
    st.button("Copy", on_click=copying(short_url))
