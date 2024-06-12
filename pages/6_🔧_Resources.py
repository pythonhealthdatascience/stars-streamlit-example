'''
Resources page

Links to:
* Github
* Open science archive
* Documentation
* Simulation + Streamlit Tutorial
( Anything else relevant)
'''

import streamlit as st
from scripts.read_file import read_file_contents

FILE = "txt/resources.md"

st.markdown(read_file_contents(FILE))
