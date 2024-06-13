import streamlit as st
from PIL import Image


def page_config():
    """
    Set page configuration throughout app
    """
    # Import STARS logo
    logo = Image.open("img/stars_logo_blue.png")

    # Set site configuration settings
    st.set_page_config(
        page_title="STARS Streamlit Example",
        page_icon=logo,
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            "About": "## Treatment centre sim.  Adapted from Nelson (2013)."
        }
    )
