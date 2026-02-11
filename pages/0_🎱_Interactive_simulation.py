import streamlit as st
import pandas as pd
from treat_sim import model as md
from treat_sim import datasets
from scripts.arrival_chart import get_arrival_chart, convert_df
from scripts.more_plot import more_plotly
from scripts.setup import page_config
from scripts.label_results import label_results
from scripts.read_file import read_file_contents

# Set page config
page_config()

# Image paths
PROCESS_IMG = "img/treat_sim_flow_diagram_labels.png"

# Text to display on the page
RESULTS_PATH = "txt/results_table.md"

INFO_1 = """On this page, you can run the treatment centre simulation model
introduced on the "Overview page"."""

INFO_2 = """ This is a model of a clinic for:
* **Trauma arrivals** - patients with severe illness and trauma. They are
first stabilised in a trauma room, then undergo treatment in a cubicle before
being discharged.
* **Non-trauma arrivals** - patients with minor illness and no trauma. They
go through registration and examination activities. A proportion of non-trauma
patients require treatment in a cubicle before being discharged.

The treatment process is summarised in the diagram below, with the
parameters you can change on this page highlighted with yellow circles 🟡."""

INFO_3 = """## Run the simulation

You should:
1. Use the **sidebar** to change the model parameters.
2. Click the **button** below to run the model.
3. Re-run the model with different parameters and **look at the effect** on
waiting times and utilisation of rooms."""

INFO_4 = """The MORE (**M**easure **O**f **R**isk and **E**rror) plot displays
the distribution in the average daily throughput that was found in each run
of the model.
* Dotted lines indicate the **mean** throughoutput and the **5th and 95th
percentile**
* The shaded yellow box shows the **95% confidence interval** of the mean
* The bars indicate the **frequency** of that level of throughput that occurred
between the runs. These are coloured:
    * Green if they fall within the 5th and 95th percentile (indicating
    "**likely**" results)
    * Red if they fall outside these (indicating "**unlikely**" results)"""


# Amended version of a function from treat_sim.datasets
def valid_profile(arrival_profile):
    """
    Provides a simple check that a dataframe containing an arrival
    profile is in a valid format.

    Raise an exception if invalid
    """

    if not isinstance(arrival_profile, pd.DataFrame):
        return """Invalid arrival profile. Profile must a DataFrame
        in the correct format."""

    if not {"period", "arrival_rate"}.issubset(arrival_profile.columns):
        return """Invalid arrival profile. DataFrame must contain period and
        arrival_rate columns"""

    if arrival_profile.shape[0] != 18:
        return f"""Invalid arrival profile. Profile should contain 18 1-hour
        periods. But selected DataFrame contains {arrival_profile.shape[0]}
        rows."""

    return True


# Create widgets to adjust model parameters within the sidebar
with st.sidebar:
    st.markdown("# Parameters")

    # Arrival profile
    st.markdown("## Arrivals")
    # Dictionary with simple key (used in code) and detailed label (displayed)
    arrival_options = {
        "Use default arrival profile": "default",
        "Use alternative arrival profile": "alternative",
        "Upload custom arrival profile": "custom"}
    # Radio button to choose arrival profile, which maps to simple key
    arrival_choice = arrival_options[
        st.radio(
            label="Arrival profile",
            label_visibility="collapsed",  # No label, as is covered by title
            options=arrival_options.keys(),
            captions=["""Default arrival profile from Nelson 2013, as
                      displayed on the 'Overview' page""",
                      """Altered default profile with higher peak in arrivals
                      at 6pm""",
                      """CSV file with arrivals rates between 6am and 12am 
                      in 60 minute intervals. Should have two columns: period
                      (e.g. '6AM-7AM') and arrival_rate (e.g. 14.5)"""],
            help="please work!")]

    # Set defaults for arrivals to None
    arrival_profile = None
    uploaded_arrivals = None

    # If choose default or alternative, then get appropriate dataset
    if arrival_choice == "default":
        arrival_profile = datasets.load_nelson_arrivals()
    elif arrival_choice == "alternative":
        arrival_profile = datasets.load_alternative_arrivals()
    # If choose custom upload, display upload widget with instructions
    elif arrival_choice == "custom":
        # Get arrival template
        arrival_template = convert_df(pd.read_csv("data/arrivals.csv"))
        # Download template arrival profile csv
        st.download_button(
            label="Download template arrival profile",
            data=arrival_template,
            file_name="data/arrivals.csv",
            mime="text/csv")
        # Upload customised arrival profile csv
        uploaded_arrivals = st.file_uploader(
            label="Please **upload** your arrival profile:")

    # If a custom arrival profile has been uploaded, download it
    if uploaded_arrivals is not None:
        arrival_profile = pd.read_csv(uploaded_arrivals)

    # Run check that arrival profile exists - if not, will prevent from
    # running simulation
    if arrival_profile is None:
        st.session_state.disabled = True
    else:
        st.session_state.disabled = False

    # Run check that arrival profile is valid - if not, will disable run
    # simulation and plot of arrival profile, and provide an informative error
    # message
    if arrival_profile is not None:
        if valid_profile(arrival_profile) is not True:
            st.session_state.disabled = True
            st.error(valid_profile(arrival_profile), icon="🚨")
        else:
            st.session_state.disabled = False

    # View chosen arrival profile, if it has been uploaded
    if uploaded_arrivals is not None:
        if valid_profile(arrival_profile) is True:
            with st.expander("View plot of chosen arrival profile",
                             expanded=False):
                # Create figure and reduce height, then display on Streamlit
                fig = get_arrival_chart(arrival_profile)
                fig.update_layout(height=250)
                st.plotly_chart(fig)

    # Number of rooms
    st.markdown("## Capacity constraints")

    triage_bays = st.slider(
        "Triage bays (A)", 1, 5, md.DEFAULT_N_TRIAGE,
        help="Number of triage cubicles")

    exam_rooms = st.slider(
        "Exam rooms (B)", 1, 5, md.DEFAULT_N_EXAM,
        help="Number of examination rooms")

    treat_rooms = st.slider(
        "Non-trauma treatment cubicles (C)", 1, 5, md.DEFAULT_N_CUBICLES_1,
        help="Number of non-trauma treatment cubicles")

    # Trauma pathway
    st.markdown("## Trauma Pathway")

    trauma_p = st.slider(
        "Probability trauma patient (D)", 0.0, 1.0, md.DEFAULT_PROB_TRAUMA,
        0.01, help="Probability that a new arrival is a trauma patient")

    trauma_mean = st.slider(
        "Mean treatment time (E)", 0.0, 100.0, md.DEFAULT_TRAUMA_TREAT_MEAN,
        1.0, help="Mean treatment time on trauma pathway (min)")

    trauma_var = st.slider(
        "Variance of treatment time (E)", 0.0, 10.0,
        md.DEFAULT_TRAUMA_TREAT_VAR, 0.5,
        help="Variance in treatment times on trauma pathway (min)")

    # Non-trauma pathway
    st.markdown("## Non-Trauma Pathway")

    exam_mean = st.slider(
        "Mean examination time (F)", 0.0, 45.0, md.DEFAULT_EXAM_MEAN, 1.0,
        help="Mean length of examination (min)")

    exam_var = st.slider(
        "Variance of examination time (F)", 0.0, 15.0, md.DEFAULT_EXAM_VAR,
        0.5, help="Variance in length of examination (min)")

    nontrauma_treat = st.slider(
        "Probability non-trauma treatment (G)", 0.0, 1.0,
        md.DEFAULT_NON_TRAUMA_TREAT_P,
        help="Probability that non-trauma patient requires treatment")

    nt_trauma_mean = st.slider(
        "Mean treatment time (H)", 0.0, 100.0,
        md.DEFAULT_NON_TRAUMA_TREAT_MEAN, 1.0,
        help="Mean length of non-trauma treatment (min)")

    nt_trauma_var = st.slider(
        "Variance of treatment time (H)", 0.0, 10.0,
        md.DEFAULT_NON_TRAUMA_TREAT_VAR, 0.5,
        help="Variance in length of non-trauma treatment (min)")

# Title
st.title("Interactive simulation")

# Intro section with treatment process
st.markdown(INFO_1)
with st.expander("Model recap", expanded=False):
    st.markdown(INFO_2)
    st.image(PROCESS_IMG, width="stretch")

# Suggestion to vary parameters
st.markdown(INFO_3)

# Set the number of replications
replications = st.number_input(
    "Multiple runs", value=30, placeholder="Enter no. replications to run...",
    help="Number of replications to run")

if st.button("Simulate treatment centre",
             disabled=st.session_state.get("disabled", True)):

    # Set up scenario (have to set arrival profile when define class, else it
    # won't run the process of setting it to arrivals, from __init__)
    args = md.Scenario(arrival_profile=arrival_profile)
    args.n_triage = triage_bays
    args.n_exam = exam_rooms
    args.n_cubicles_1 = treat_rooms
    args.trauma_treat_mean = trauma_mean
    args.trauma_treat_var = trauma_var
    args.non_trauma_treat_p = nontrauma_treat
    args.non_trauma_treat_mean = nt_trauma_mean
    args.non_trauma_treat_var = nt_trauma_var
    args.prob_trauma = trauma_p
    args.exam_mean = exam_mean
    args.exam_var = exam_var

    # Get results
    with st.spinner("Simulating the treatment centre..."):
        results = md.multiple_replications(args, n_reps=replications)
    st.success("Done!")

    # Display table of results
    st.header("Results")
    # col1, col2 = st.columns(2)
    with st.expander("Tabular results", expanded=True):
        st.markdown(read_file_contents(RESULTS_PATH))
        # Get mean to 1 decimal place for each column in results
        summary_series = results.mean().round(1)
        summary_series.name = "Mean (across model runs)"
        # Convert to dataframe and relabel each of the results
        summary_df = label_results(summary_series)
        # Display results
        st.dataframe(
            summary_df, height=597, use_container_width=True)

    # Display MORE plot
    with st.expander("MORE Plot", expanded=True):
        # Advice for interpretation of MORE plot
        st.markdown(INFO_4)
        # Create plot
        more_fig = more_plotly(results["09_throughput"].to_numpy(),
                               x_label="Average Daily Throughput")
        st.plotly_chart(more_fig, use_container_width=True)

# Message that displays if on custom arrival profile but no upload
if st.session_state.get("disabled", True):
    st.markdown("""**Note:** This button has been disabled as you have not
        yet uploaded a valid custom arrival profile. Please upload a valid
        profile, or return to the provided default or alternative profiles.""")
