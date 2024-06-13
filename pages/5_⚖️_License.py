import streamlit as st
from scripts.read_file import read_file_contents
from scripts.setup import page_config

# Set page config
page_config()

LICENSE_FILE = ("LICENSE")

# Title
st.markdown("# License")

# Show MIT license
license_txt = read_file_contents(LICENSE_FILE)
st.code(license_txt, language="markdown", line_numbers=False)