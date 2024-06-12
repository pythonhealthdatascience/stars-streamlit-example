'''
Change log page

A list of changes to each version of the app
'''

import streamlit as st
from scripts.read_file import read_file_contents

FILE = (
    "https://raw.githubusercontent.com/pythonhealthdatascience/"
    + "stars-streamlit-example/main/CHANGES.md"
)

st.markdown(read_file_contents(FILE))
