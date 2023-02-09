from loops import fib_from_text
import streamlit as st


text_input = st.text_input('Input text')


result = fib_from_text(text_input)

st.write(result)
