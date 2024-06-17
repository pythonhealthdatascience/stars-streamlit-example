import streamlit as st
from scripts.read_file import read_file_contents
from scripts.setup import page_config
from scripts.arrival_chart import get_arrival_chart

# Set page config
page_config()

# File paths
OVERVIEW = "txt/overview.md"
PROCESS_IMG = "img/process_flow_img.png"

# Text to display
INFO_1 = "**A simple simulation model of a urgent care and treatment centre.**"
INFO_2 = """This treatment process diagram describes the simple rules that
clinic has for caring for patients.

**Trauma arrivals:** patients with severe illness and trauma that must first be
stablised in a trauma room. These patients then undergo treatment in a cubicle
before being discharged.

**Non-trauma arrivals:** patients with minor illness and no trauma go through
registration and examination activities. A proportion of non-trauma patients
require treatment in a cubicle before being discharged."""

# Title
st.title("Treatment Centre Simulation Model")

# Get text and partition into sections
overview = read_file_contents(OVERVIEW)
overview_1 = overview.partition("start_1")[2].partition("end_1")[0]
overview_2 = overview.partition("start_2")[2].partition("end_2")[0]
overview_3 = overview.partition("start_3")[2].partition("end_3")[0]

# Display info about treatment centre inc. graph with daily arrivals
st.markdown(INFO_1)
st.markdown(overview_1)
with st.expander("View arrival pattern", expanded=False):
    st.plotly_chart(get_arrival_chart(), use_container_width=True)

# Display info on model applications and how it is set up, including
# the treatment process diagram
st.markdown(overview_2)
with st.expander("View treatment process", expanded=False):
    st.image(PROCESS_IMG)
    st.markdown(INFO_2)

# Display info on using model to explore different scenarios
st.markdown(overview_3)
