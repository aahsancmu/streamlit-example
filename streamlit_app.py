import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

from brain import get_me_an_answer

st.title("Ask Quantum about Terlipressin 👨‍⚕️ 💉")

question_input = st.text_input("Question:")

if question_input:
  answer = get_me_an_answer(question_input, st.secrets["OPENAI_API_KEY"])
  st.text_area("Answer:", answer)
