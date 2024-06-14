import streamlit as st
# Widgets and JS events from bokeh to execute copy to clipboard
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
# Return bokeh events from streamlit
from streamlit_bokeh_events import streamlit_bokeh_events


def copy_results():
    """
    Create button that, when clicked, copies table to clipboard

    Notes:
    ------
    Code based on:
    https://discuss.streamlit.io/t/copy-dataframe-to-clipboard/2633
    """
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
