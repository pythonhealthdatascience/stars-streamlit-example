'''
Change log page

A list of changes to each version of the app
'''

import streamlit as st
from scripts.read_file import read_file_contents

FILE = "CHANGES.md"

st.markdown(read_file_contents(FILE))
