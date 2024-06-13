import streamlit as st
from PIL import Image
from scripts.read_file import read_file_contents
from scripts.setup import page_config

# Set page config
page_config()

# Text to display
INFO_1 = "**A simple simulation model of a urgent care and treatment centre.**"
OVERVIEW_PATH = "txt/overview.md"

# Title
st.title("Treatment Centre Simulation Model")

# NIHR logo
image = Image.open("img/nihr.png")
st.image(image)

# Display info and plain english summary
st.markdown(INFO_1)
st.markdown(read_file_contents(OVERVIEW_PATH))
