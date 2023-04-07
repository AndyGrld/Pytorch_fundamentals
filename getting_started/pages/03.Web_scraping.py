import streamlit as st
import requests
import webbrowser
from bs4 import BeautifulSoup

st.set_page_config(page_title="Unsplash webscraper", page_icon=":globe_with_meridians")

st.markdown("<h1>Web Scraper</h1>", unsafe_allow_html=True)

with st.form("Search"):
    keyword = st.text_input("Enter your keyword")
    search = st.form_submit_button("Submit")
placeholder = st.empty()
if keyword:
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup = BeautifulSoup(page.content, features="lxml")
    rows = soup.find_all("div", class_="ripi6")
    col1, col2 = placeholder.columns(2)
    for j, row in enumerate(rows):
        figures = row.find_all('figure')
        for i in range(2):
            img = figures[i].find("img", class_="tB6UZ a5VGX")
            list = img['srcset'].split("?")
            anchor = figures[i].find("a", class_="rEAWd")
            print(anchor["href"])
            if i==0:
                col1.image(list[0])
                btn = col1.button("Download", key=str(j)+str(i))
                if btn:
                    webbrowser.open_new_tab(f"https://unsplash.com{anchor['href']}")
            else:
                col2.image(list[0])
                btn = col2.button("Download", key=str(j)+str(i))
                if btn:
                    webbrowser.open_new_tab(f"https://unsplash.com{anchor['href']}")
