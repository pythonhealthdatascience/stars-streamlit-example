import streamlit as st
import pandas as pd
from treat_sim import model as md
from scripts.setup import page_config

# Set page config
page_config()

# Title and link to model (used in description)
TITLE = "Create custom experiments"
MODEL_URL = "https://github.com/pythonhealthdatascience/stars-treat-sim/" \
            "blob/main/treat_sim/model.py"

# Path to template file
TEMPLATE_PATH = "data/scenarios.csv"

# Intro text (provided here rather than seperate .md file due to frequent input
# of parameters, as set-up as f string)
INFO_1 = f"""The "🎱 Interactive simulation" page allowed you to run one
scenario at a time. This page enables you to get the results from multiple
scenarios, compared in a single table.

## Create a scenario CSV file

To run these experiments, you need to upload a CSV file containing a
table of parameters. In the table, each row is a scenario, and each
column is an argument for the model Scenario() object.

> See [stars-treat-sim/treat_sim/model.py]({MODEL_URL}) for a full list of
parameters that you can vary in each scenario.

For each scenario, values are interpreted as **relative changes** to parameters
from their default values.

**Resource counts are bounded at 0** - you will therefore get an error if you
set the count to be too low).

### Template

This template varies four parameters:

* **n_triage** - the number of triage cubicles - default: {md.DEFAULT_N_TRIAGE}
* **n_exam** - the number of examination rooms - default: {md.DEFAULT_N_EXAM}
* **n_cubicles_1** - the number of non-trauma treatment cubicles - default:
{md.DEFAULT_N_CUBICLES_1}
* **exam_mean** - the mean length of examination (min) - default:
{md.DEFAULT_EXAM_MEAN}
* **n_trauma** - number of trauma bays for stabilisation - default:
{md.DEFAULT_N_TRAUMA}

Hover over the table to view **download** button in top right corner."""

INFO_2 = "## Upload custom scenarios and compare results"

# Test shown after upload and running
EXECUTE_TXT = "Execute custom experiments"
SHOW_TXT = "Show results"


def create_scenarios(df_scenarios):
    """
    Returns dictionary of Scenario object based on contents of a dataframe

    Params:
    ------
    df_scenarios: pandas.DataFrame
        Dataframe of scenarios. First two columns are id, name followed by
        variable names. No fixed width.

    Returns:
    --------
    dict

    Notes:
    -----
    No validation is currently done.  This will crash when format or variable
    names do not meet assumptions or are invalid.
    """
    cust_scenarios = {}
    for index, row in df_scenarios.iterrows():
        scenario_i = md.Scenario()
        # loop through variable names
        for var_name in df_scenarios.columns.tolist()[2:]:
            # get the value for update
            current_value = getattr(scenario_i, var_name)

            # update the variable using the relative
            setattr(scenario_i, var_name, current_value + row[var_name])

        cust_scenarios[row["name"]] = scenario_i

    return cust_scenarios


def convert_df(df):
    return df.to_csv().encode("utf-8")


def run_experiments(scenarios, n_reps):
    return md.run_scenario_analysis(scenarios,
                                    md.DEFAULT_RESULTS_COLLECTION_PERIOD,
                                    n_reps)


def results_as_summary_frame(results):
    return md.scenario_summary_frame(results).round(1)


st.title(TITLE)
st.markdown(INFO_1)

# Display and offer option to download template
template = pd.read_csv(TEMPLATE_PATH)
st.dataframe(template, hide_index=True)

# Upload section
st.markdown(INFO_2)
uploaded_file = st.file_uploader("Choose a file")

df_results = pd.DataFrame()
if uploaded_file is not None:
    # assumes CSV
    df_scenarios = pd.read_csv(uploaded_file, index_col=0)
    st.write("**Loaded Experiments**")
    st.table(df_scenarios)

    # loop through scenarios, create and run model
    n_reps = st.slider("Replications", 3, 30, 5, step=1)

    if st.button(EXECUTE_TXT):

        # create the cust scenarios based on upload
        cust_scenarios = create_scenarios(df_scenarios)
        with st.spinner("Running scenario analysis"):
            results = run_experiments(cust_scenarios, n_reps)
            st.success("Done!")
            df_results = results_as_summary_frame(results)
            # display in the app via table
            st.table(df_results)

        # Display results (which has inbuilt download button, and can easily
        # select all and copy to clipboard)
        st.dataframe(df_results)
