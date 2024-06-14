import streamlit as st
from treat_sim import model as md
from scripts.setup import page_config
from scripts.read_file import read_file_contents

# Set page config
page_config()

# File paths and text to display
TITLE = "Run multiple experiments"
INFO_2 = "### Run 5 pre-specified scenarios and compare results."
SCENARIO_PATH = "txt/scenarios.md"

# Title and introduction
st.title(TITLE)
st.markdown(INFO_2)
st.markdown(read_file_contents(SCENARIO_PATH))
st.markdown("")

if st.button("Run all scenarios and compare"):

    scenarios = md.get_scenarios()

    with st.spinner("Running scenario analysis"):
        results = md.run_scenario_analysis(
            scenarios=scenarios,
            rc_period=md.DEFAULT_RESULTS_COLLECTION_PERIOD,
            n_reps=5)

        st.session_state["preset_results"] = (
            md.scenario_summary_frame(results).round(1))

if "preset_results" in st.session_state:
    # Success message
    st.success("Done!")

    # Display results (which has inbuilt download button, and can easily
    # select all and copy to clipboard)
    st.dataframe(st.session_state["preset_results"])
