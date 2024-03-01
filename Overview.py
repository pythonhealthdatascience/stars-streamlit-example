import streamlit as st
from PIL import Image
import urllib
import urllib.request as request

st.set_page_config(
    # page_title="Ex-stream-ly Cool App",
    # page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        #    'Get Help': 'https://www.extremelycoolapp.com/help',
        #    'Report a bug': "https://www.extremelycoolapp.com/bug",
        "About": "## Treatment centre sim.  Adapted from Nelson (2013)."
    },
)

INFO_1 = """**A simple simulation model of a urgent care and treatment centre.**"""

OVERVIEW_PATH = (
    "https://raw.githubusercontent.com/pythonhealthdatascience/"
    + "stars-streamlit-example/main/txt/overview.md"
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


st.title("Treatment Centre Simulation Model")

image = Image.open("img/nihr.png")
st.image(image)

st.markdown(INFO_1)

# plain english summary
st.markdown(read_file_contents(OVERVIEW_PATH))
