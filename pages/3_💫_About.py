'''
About page:

Links to:
* STARS (to add when created) and funders
* Researchers via ORCIDs
* Sim software
( Anything else relevant)
'''

import streamlit as st
from scripts.read_file import read_file_contents
from scripts.setup import page_config

# Set page config
page_config()

FILE = "txt/acknowledgement.md"

st.markdown(read_file_contents(FILE))
