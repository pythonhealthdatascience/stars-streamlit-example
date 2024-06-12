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

FILE = "txt/acknowledgement.md"

st.markdown(read_file_contents(FILE))
