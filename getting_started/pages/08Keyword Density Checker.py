import streamlit as st
import re
import numpy as np

st.set_page_config(page_title="Keyword Density Checker")

st.markdown("<h1>Keyword Density Checker</h1>", unsafe_allow_html=True)

text = st.text_area("Paragraph")
words_dict = dict()

if text:
    # substitute special characters with empty string in text inputted
    sim_text = re.sub("[!@#$%^&*<>?:.,;]", "", text)
    words = sim_text.lower().split(" ")
    for word in words:
        if word.strip() in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

    count = list(words_dict.values())
    np_count = np.array(count)
    word_count = np_count.sum()

    keys = list(words_dict.keys())
    values = list(words_dict.values())
    col1, col2, col3 = st.columns(3)
    col1.markdown(f"<h3 style='text-align:center'>Keywords</h3>", unsafe_allow_html=True)
    col2.markdown(f"<h3 style='text-align:center'>Count</h3>", unsafe_allow_html=True)
    col3.markdown(f"<h3 style='text-align:center'>Percentage Density</h3>", unsafe_allow_html=True)
    for i in range(len(keys)):
        col1.markdown(f"<h5 style='text-align:center'>{keys[i]}</h5>", unsafe_allow_html=True)
        col2.markdown(f"<h5 style='text-align:center'>{values[i]}</h5>", unsafe_allow_html=True)
        col3.markdown(f"<h5 style='text-align:center'>{round((values[i] / word_count) * 100)}%</h5>",
                      unsafe_allow_html=True)

    st.markdown(f"<h5>Total words counted = {word_count}</h5>", unsafe_allow_html=True)
