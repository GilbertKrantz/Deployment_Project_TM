import streamlit as st
import pandas as pd
import numpy as np

from Google_T5 import textHandler

def main():
    st.title("Scientific Text Summarizer")
    st.subheader("This app uses the T5 model to summarize scientific text")

    text = st.text_area("Enter the text you want to summarize:")
    max_length = text.count(' ') + 1

    if st.button("Summarize"):
        text_handler = textHandler(max_length=max_length)
        summary = text_handler.summarize(text)
        st.write(summary)
        
    st.write("This app was created by Gilbert Krantz. You can find the code on [GitHub]")
    
if __name__ == "__main__":
    main()