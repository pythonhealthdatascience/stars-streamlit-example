import streamlit as st
import pandas as pd
from treat_sim import model as md
from scripts.setup import page_config
from scripts.scenarios import create_scenarios
from scripts.read_file import read_file_contents

# Set page config
page_config()

# Text to be displayed on page
TITLE = "Create custom experiments"
UPLOAD_TITLE = "## Upload custom scenarios and compare results"
EXECUTE_TXT = "Execute custom experiments"
SHOW_TXT = "Show results"

# URLS and paths (to model, template and text)
MODEL_URL = "https://github.com/pythonhealthdatascience/stars-treat-sim/" \
            "blob/main/treat_sim/model.py"
TEMPLATE_PATH = "data/scenarios.csv"
INTRO_TEXT = "txt/upload.md"

# Display title and introduction
st.title(TITLE)
st.markdown(read_file_contents(INTRO_TEXT).format(
    url=MODEL_URL,
    n_triage=md.DEFAULT_N_TRIAGE,
    n_exam=md.DEFAULT_N_EXAM,
    n_cubicles_1=md.DEFAULT_N_CUBICLES_1,
    exam_mean=md.DEFAULT_EXAM_MEAN,
    n_trauma=md.DEFAULT_N_TRAUMA))

# Display and offer option to download template
template = pd.read_csv(TEMPLATE_PATH)
st.dataframe(template, hide_index=True)

# Section to upload file - if so, convert to df and save to session state
st.markdown(UPLOAD_TITLE)
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    st.session_state["uploaded_file"] = pd.read_csv(uploaded_file)
    # If there are any results in session state, remove them, else will keep
    # showing old results
    if "upload_results" in st.session_state:
        del st.session_state["upload_results"]

# If an upload is in the session state...
if "uploaded_file" in st.session_state:
    # Display the uploaded scenario table
    st.write("**Loaded Experiments**")
    st.table(st.session_state["uploaded_file"])

    # Set number of replications
    n_reps = st.slider("Replications", 3, 30, 5, step=1)

    # Button to loop through scenarios, create and run model
    if st.button(EXECUTE_TXT):

        # Create the cust scenarios based on upload
        cust_scenarios = create_scenarios(st.session_state["uploaded_file"])
        with st.spinner("Running scenario analysis"):
            # Run the scenario analysis
            results = md.run_scenario_analysis(
                scenarios=cust_scenarios,
                rc_period=md.DEFAULT_RESULTS_COLLECTION_PERIOD,
                n_reps=n_reps)
            # Convert into a results summary frame
            st.session_state["upload_results"] = (
                md.scenario_summary_frame(results).round(1))

if "upload_results" in st.session_state:
    # Display success message
    st.success("Done!")

    # Display results as dataframe (which has inbuilt download button, and can
    # easily select all and copy to clipboard)
    st.markdown("## Results")
    st.dataframe(st.session_state["upload_results"])
