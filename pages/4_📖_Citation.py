import streamlit as st
from scripts.read_file import read_file_contents

FILE = (
    "https://raw.githubusercontent.com/pythonhealthdatascience/"
    + "stars-streamlit-example/main/txt/citation.md"
)

st.title("Citation")
st.markdown(read_file_contents(FILE))
