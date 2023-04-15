import streamlit as st
import pyttsx3


class textToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)

    def save_file(self, text, filename):
        self.engine.save_to_file(text, filename)


tts = textToSpeech()


st.title("Text to Speech Converter")

text = st.text_input("Please enter a text to convert")

if st.button("Convert"):
    tts.save_file(text, 'converted.mp3')
    try:
        with open("converted.mp3", 'rb') as audio:
            audio_bytes = audio.read()
        st.audio(audio_bytes, format='audio/mp3')
    except FileNotFoundError:
        st.error("File 'converted.mp3' not found.")
    except Exception as e:
        st.error("An error occurred: {}".format(e))
