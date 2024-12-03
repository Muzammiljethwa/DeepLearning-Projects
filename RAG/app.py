import streamlit as st
from llm_chain import ask_ai

st.title("Medical GPT: Medi 🤖|🩺")

def generate_response(input_text):
    st.info(ask_ai(input_text))

with st.form("my_form"):
    text = st.text_area("Enter text:", "What your duties as a doctor?")
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)