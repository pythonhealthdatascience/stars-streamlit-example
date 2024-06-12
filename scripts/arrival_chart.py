import model as md
import plotly.express as px
import pandas as pd


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
