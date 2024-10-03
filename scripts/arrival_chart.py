import plotly.express as px
import pandas as pd

from treat_sim import model as md
from treat_sim.datasets import load_nelson_arrivals

def get_arrival_chart():
    """
    Create and return a plotly express bar chart of
    arrivals

    Returns:
    --------
    plotly figure.
    """
    arrivals = load_nelson_arrivals()
    fig = px.bar(arrivals, x="period", y="arrival_rate",
                 labels={
                    "period": "hour of day",
                    "arrival_rate": "mean arrivals"
                 })

    return fig
