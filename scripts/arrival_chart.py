import plotly.express as px
import pandas as pd

from treat_sim import model as md


def get_arrival_chart():
    '''
    Create and return a plotly express bar chart of
    arrivals

    Returns:
    --------
    plotly figure.
    '''
    arrivals = pd.read_csv(md.NSPP_PATH)
    fig = px.bar(arrivals, x='period', y='arrival_rate',
                 labels={
                    "period": "hour of day",
                    "arrival_rate": "mean arrivals"
                 })

    return fig
