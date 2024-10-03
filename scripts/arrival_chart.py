import plotly.express as px
import streamlit as st


def get_arrival_chart(arrivals):
    """
    Create and return a plotly express bar chart of arrivals

    Parameters:
    -----------
    arrivals : pandas dataframe
      Dataframe with hourly arrivals

    Returns:
    --------
    plotly figure.
    """
    fig = px.bar(arrivals, x="period", y="arrival_rate",
                 labels={
                    "period": "hour of day",
                    "arrival_rate": "mean arrivals"
                 })

    return fig


@st.cache_data
def convert_df(df):
    """
    Convert dataframe to utf-8, cacheing it to prevent computation on
    every rerun. Used when downloading template arrival profile.

    Source: https://docs.streamlit.io/develop/api-reference/widgets/st.download_button

    Parameters:
    -----------
    df : pandas dataframe
    """
    return df.to_csv().encode("utf-8")
