import streamlit as st
from scripts.read_file import read_file_contents
from scripts.setup import page_config

# Set page config
page_config()

FILE = "txt/citation.md"

st.title("Citation")
st.markdown(read_file_contents(FILE))
