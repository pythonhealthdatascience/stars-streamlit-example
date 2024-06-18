"""
About page:

Links to:
* STARS (to add when created) and funders
* Researchers via ORCIDs
* Sim software
( Anything else relevant)
"""

import streamlit as st
from scripts.read_file import read_file_contents
from scripts.setup import page_config

# Set page config
page_config()

# File paths to text and images
FILE = "txt/acknowledgement.md"
STARS = "img/stars_logo_blue_text.png"

# Get text and partition into sections
about = read_file_contents(FILE)
about_1 = about.partition("start_1")[2].partition("end_1")[0]
about_2 = about.partition("start_2")[2].partition("end_2")[0]

# Display text and images
st.markdown(about_1)
st.image(STARS, output_format="PNG", width=400)
st.markdown(about_2)
