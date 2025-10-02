import streamlit as st
import locale
from utils import get_entity
locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")
st.set_page_config(
    page_title="X5",
    layout="wide",
    page_icon=":search",
    initial_sidebar_state="collapsed",
)

st.title("Введите запрос")
input = st.text_input("Введите запрос")
if input:
    st.write(get_entity(input))
