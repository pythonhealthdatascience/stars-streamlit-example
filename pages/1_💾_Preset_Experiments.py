import streamlit as st
from treat_sim import model as md
from scripts.setup import page_config
from scripts.read_file import read_file_contents
# Widgets and JS events from bokeh to execute copy to clipboard
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
# Return bokeh events from streamlit
from streamlit_bokeh_events import streamlit_bokeh_events

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
    print(scenarios)

    with st.spinner("Running scenario analysis"):
        # will only compute once... due to cache
        results = md.run_scenario_analysis(
            scenarios=scenarios,
            rc_period=md.DEFAULT_RESULTS_COLLECTION_PERIOD,
            n_reps=5)

        st.session_state['preset_results'] = md.scenario_summary_frame(results).round(1)

if 'preset_results' in st.session_state:
    st.success("Done!")

    # Display results table
    st.table(st.session_state['preset_results'])

    # Download results (with dependence on session state meaning the table no
    # longer vanishes when this is clicked)
    st.download_button(
        "Download results as .csv",
        st.session_state['preset_results'].to_csv().encode("utf-8"),
        "experiment_results.csv",
        "text/csv",
        key="download-csv")

    # Copy table workaround for streamlit bug. Code based on
    # https://discuss.streamlit.io/t/copy-dataframe-to-clipboard/2633
    copy_button = Button(label="Copy results to clipboard")
    copy_button.js_on_event("button_click", CustomJS(
        args=dict(df=st.session_state['preset_results'].to_csv(sep="\t")),
        code="navigator.clipboard.writeText(df);"))
    no_event = streamlit_bokeh_events(
        copy_button,
        events="GET_TEXT",
        key="get_text",
        refresh_on_update=True,
        override_height=75,
        debounce_time=0)
