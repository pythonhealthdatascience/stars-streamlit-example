import streamlit as st
from scripts.read_file import read_file_contents

LICENSE_FILE = (
    "https://raw.githubusercontent.com/pythonhealthdatascience/"
    + "stars-streamlit-example/dev/LICENSE"
)

# LICENSE_PAGE_TXT = (
#     "https://raw.githubusercontent.com/pythonhealthdatascience/"
#     + "stars-streamlit-example/dev/txt/license_page.md"
# )

# Show license header and badge
#st.markdown(read_file_contents(LICENSE_PAGE_TXT))
st.markdown("# License")

# show MIT license.
license_txt = read_file_contents(LICENSE_FILE)
st.code(license_txt, language="markdown", line_numbers=False)