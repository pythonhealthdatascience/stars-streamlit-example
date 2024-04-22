'''
Change log page

A list of changes to each version of the app
'''

import streamlit as st
import urllib.request as request

FILE = (
    "https://raw.githubusercontent.com/pythonhealthdatascience/"
    + "stars-streamlit-example/main/CHANGES.md"
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


st.markdown(read_file_contents(FILE))
