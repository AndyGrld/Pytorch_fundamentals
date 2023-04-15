from PIL import Image
import streamlit as st
from PIL.ImageFilter import BLUR, SMOOTH, EMBOSS, DETAIL

st.markdown("<h1>Image Editor</h1>", unsafe_allow_html=True)
st.markdown("---")

image = st.file_uploader("Upload your image", type=["jpg", "png", "jpeg", "jfif"])
size = st.empty()
mode = st.empty()
format_ = st.empty()
info = st.empty()

if image:
    image = Image.open(image)
    info.markdown(f"<h2>Information</h2>", unsafe_allow_html=True)
    size.markdown(f"<h6>{image.size}</h6>", unsafe_allow_html=True)
    mode.markdown(f"<h6>{image.mode}</h6>", unsafe_allow_html=True)
    format_.markdown(f"<h6>{image.format}</h6>", unsafe_allow_html=True)

    st.markdown(f"<h6>Resizing</h6>", unsafe_allow_html=True)
    width = st.number_input("Width", value = image.width)
    height = st.number_input("Height", value = image.height)

    st.markdown(f"<h6>Rotation</h6>", unsafe_allow_html=True)
    degree = st.number_input("Degree")

    st.markdown(f"<h6>Filters</h6>", unsafe_allow_html=True)
    filters = st.selectbox("Filters", options=("None", "Blur", "Detail", "Emboss", "Smooth"))

    btn = st.button("Submit")
    if btn:
        edited = image.resize((width, height)).rotate(degree)
        if filters != "None":
            if filters == "Blur":
                filtered = edited.filter(BLUR)
            elif filters == "Detail":
                filtered = edited.filter(DETAIL)
            elif filters == "Smooth":
                filtered = edited.filter(SMOOTH)
            else:
                filtered = edited.filter(EMBOSS)
        else:
            filtered = edited

        st.image(filtered)
