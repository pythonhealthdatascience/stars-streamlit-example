import streamlit as st
import urllib.request as request

LICENSE_FILE = (
    "https://raw.githubusercontent.com/pythonhealthdatascience/"
    + "stars-streamlit-example/dev/LICENSE"
)

LICENSE_PAGE_TXT = (
    "https://raw.githubusercontent.com/pythonhealthdatascience/"
    + "stars-streamlit-example/dev/txt/license_page.md"
)


def read_file_contents(path):
    """
    Download the content of a file from the GitHub Repo and return as a utf-8 string

    Notes:
    -------
        adapted from 'https://github.com/streamlit/demo-self-driving'

    Parameters:
    ----------
    path: str
        e.g. file_name.md

    Returns:
    --------
    utf-8 str

    """
    response = request.urlopen(path)
    return response.read().decode("utf-8")

# show license header and badge
#st.markdown(read_file_contents(LICENSE_PAGE_TXT))
st.markdown("# License")

# show MIT license.
license_txt = read_file_contents(LICENSE_FILE)
st.code(license_txt, language="markdown", line_numbers=False)