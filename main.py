import os
import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]
model = "text-davinci-003"

st.write("# Explain Like I'm 5")
input_str = st.text_input("What do you want to know?", key="input")

if not input_str.endswith("?"):
    input_str += "?"

if st.button("Submit"):
    input_str = "Could you explain this to a five year old " + input_str
    response = openai.Completion.create(engine=model, prompt=input_str, max_tokens=1024, temperature=0.5)
    response_str = response['choices'][0]['text']
    st.success(response_str)
