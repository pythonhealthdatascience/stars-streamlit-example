import streamlit as st
from treat_sim import model as md
from scripts.more_plot import more_plotly
from scripts.setup import page_config

# Set page config
page_config()

# Text to display on the page
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

# Create widgets to adjust model parameters within the sidebar
with st.sidebar:
    st.markdown("# Parameters")

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
with st.expander("Model recap", expanded=True):
    st.markdown(INFO_2)
    st.image("img/treat_sim_flow_diagram_labels.png")

# Suggestion to vary parameters
st.markdown(INFO_3)

# Set up scenario
args = md.Scenario()
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

# Set the number of replications
replications = st.number_input(
    "Multiple runs", value=10, placeholder="Enter no. replications to run...",
    help="Number of replications to run")

if st.button("Simulate treatment centre"):
    # Get results
    with st.spinner("Simulating the treatment centre..."):
        results = md.multiple_replications(args, n_reps=replications)
    st.success("Done!")

    # Display table of results
    col1, col2 = st.columns(2)
    with col1.expander("Tabular results", expanded=True):
        summary_series = results.mean().round(1)
        summary_series.name = "Mean"
        st.table(summary_series)

    # Display MORE plot
    with col2.expander("MORE Plot", expanded=True):
        more_fig = more_plotly(results["09_throughput"].to_numpy(),
                               x_label="Average Daily Throughput")
        st.plotly_chart(more_fig, use_container_width=True)
