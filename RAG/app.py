import streamlit as st
from llm_chain import ask_ai

st.title("Medical GPT: Medi 🤖|🩺")

llm_name = st.radio(
    "Choose your Model",
    ["4o", "4o-mini"],
)

def generate_response(input_text):
    st.info(ask_ai(
                query=input_text,
                model_name=llm_name
            )
        )

with st.form("my_form"):
    text = st.text_area("Enter text:", "What your duties as a doctor?")
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)