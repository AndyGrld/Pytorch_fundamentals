import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image

st.set_page_config(page_title="my website", page_icon=':tada', layout='wide')

# loading assets
lottie_coding= 'https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json'
fashion_image = Image.open("../fashionDataset.png")
nums_image = Image.open("../random_nums.png")


# use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css('../style.css')


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


with st.container():
    st.subheader("Hi, I am Andy :wave")
    st.title("A data Scientist")
    st.write("I am passionate about python and machine learning")
    st.write("[Learn more >](www.google.com)")

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write('##')
        st.write(
            '''
            I am a student at the University of Mines and Technology in Tarkwa who:
            - is very passionate about machine learning and data science topics.
            - wants to learn data science and analysis to make an impact in society.
            - finding ways to automate our daily repetitive tasks.
            '''
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key='coding')
        st.write("Right column")

with st.container():
    st.write('---')
    st.header("My projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(fashion_image)
    with text_column:
        st.subheader("Learning Fields")
        st.write(
            '''
            - Web development (HTTP, CSS, JAVASCRIPT, FLASK, DJANGO, STREAMLIT)
            - Machine Learning (PYTHON)
            - Neural Network (PYTORCH)
            - Computer Vision (OPENCV)
            - Computer Graphics (A-FRAME)
            '''
        )
        st.markdown('[Watch video...](https://youtu.be/TXSQitGoINE)')
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(nums_image)
    with text_column:
        st.subheader("Public projects I have worked on")
        st.write(
            '''
            Here are some projects that I have worked on:
            - A loan management system
            - Handwritten digit recognizer using machine learning and neural networks
            - Fashion recognition using CNN implemented in pytorch
            - A human resource management system made with flask and basic HTML, CSS and javascript
            '''
        )
        st.markdown('[Github Account](github.AndyGrld)')
with st.container():
    st.write('---')
    st.header('Get in touch with me')
    st.write("##")
    contact_form = '''
    <form action="https://formsubmit.co/ansongandy04@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email address" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    '''
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
