import streamlit as st
from scripts.read_file import read_file_contents

FILE = "txt/citation.md"

st.title("Citation")
st.markdown(read_file_contents(FILE))
