'''
Measure of Risk and Error (MORE) plot

Provides a simple summary of replications in terms of likely and 
unlikely ranges and CI ranges for mean and percentiles.

'''

import numpy as np
import pandas as pd
import warnings
import plotly.express as px


def ci_for_sample_mean(mean_value, std, n, critical_value=1.96):
    '''Confidence interval for mean.  Assume std is sample std.

    Notes:
    ------

    critical value hard coded at the moment.  
    Should update to use t dist.
    '''
    half_width = (critical_value * (std / np.sqrt(n)))
    mean_lower = mean_value - half_width
    mean_upper = mean_value + half_width
    return mean_lower, mean_upper


def ci_percentile(results, field, percentile, critical_value=1.96):
    '''Approximate confidence interval for percentile.
    Note these may or may not be symmetric.
    
    Notes:
    ------
    
    critical value hard coded at the moment.  
    Should update to use t dist.
    
    Params:
    ------
    results: pd.DataFrame
        Results dataframe - tabular data where each row is a rep and each col is a KPI
        
    field: int
        Field from data frame to analyse
        
    percentile: float
        The percentile around which to form the CI
        
    critical_value: float, optional (default = 1.96)
        critical value of the normal dist to use.
    '''
    half_width = critical_value * np.sqrt((percentile * (1 - percentile)) / (len(results) - 1))
    y_beta_1 = results[field].quantile(percentile - half_width)
    y_beta_2 = results[field].quantile(percentile + half_width)
    return y_beta_1, y_beta_2


def more_plotly(data, x_label, percentiles=(0.05, 0.95), suppress_warnings=False):
    """Interactive Measure of Risk and Error (MORE) plot via PLOTLY
    
    Risk illustrated via likely and unlikely ranges of replication values. 
    Error illustrated for CIs for mean and wide approx confidence intervals for percentiles
        
    Confidence intervals for percentiles will only be calculated if > 80 replications due to 
    approximation accuracy.
    
    Notes:
    ------
    Each value plotted represents the mean of a replication (e.g. daily throughput).  It should
    not be confused with an individuals results (e.g. an individuals throughput time). 
    
    If the system modelled contains time dependency the MORE plot may hide time of day/event effects.
    
    Params:
    ------
    data: np.ndarray
        Vector containing multiple replications
        
    x_label: str
        X axis label
    
    percentiles: type(float, float), optional (default = (0.05,0.95))
        The percentile to include in the MORE plot.

    suppress_warnings: bool, optional (default=False)
        Suppress warning that CIs for percentiles are not produced for < 80 replications.
    
    Returns:
    -------
        plotly.graph_objects.Figure: The Plotly figure object.
    
    See Also:
    ---------
    more_plot()

    Refs:
    -----
    
    Nelson 2008. (Winter Simulation Paper)
    https://ieeexplore.ieee.org/document/4736095       

    """

     # probably will shift these to module level scope.
    LIKELY = 'LIKELY'
    UNLIKELY = 'UNLIKELY'
    FONT_SIZE = 12
    LINE_WIDTH = 3
    LINE_STYLE = '-'
    CRIT_VALUE = 1.96
    UPPER_QUANTILE = percentiles[1]
    LOWER_QUANTILE = percentiles[0]
    INTERVAL_LW = 2
    MIN_N_FOR_PERCENTILE = 80
    WARN = f'CIs for percentiles are not generated as sample size < {MIN_N_FOR_PERCENTILE}.'
    WARN += ' To supress this msg set `supress_warnings=True`'

    # Calculate the 5th and 95th percentiles and round them up to the nearest integer
    p5 = np.ceil(np.percentile(data, LOWER_QUANTILE*100)).astype(int)
    p95 = np.ceil(np.percentile(data, UPPER_QUANTILE*100)).astype(int)
    mean = np.mean(data)
    
    # Calculate the 95% confidence interval for the mean
    std_err = np.std(data) / np.sqrt(len(data))
    lower_limit = mean - CRIT_VALUE * std_err
    upper_limit = mean + CRIT_VALUE * std_err
    
    # Calculate the histogram using NumPy
    counts, bins = np.histogram(data, bins='auto')
     
    # Determine the color for each bin
    colors = np.where((bins[:-1] < p5) | (bins[:-1] >= p95), UNLIKELY, LIKELY)
    
    # Create the color map for the histogram
    color_discrete_map = {
        LIKELY: '#4CAF50',  # Green
        UNLIKELY: '#F44336'  # Red
    }
    
    # Create the Plotly figure (uses plotly express - needs updated to `go`)
    fig = px.bar(x=bins[:-1], y=counts, color=colors, color_discrete_map=color_discrete_map,
                 range_x=[np.min(data),np.max(data) * 1.02])
    
    # remove gap between bars
    fig.update_layout(bargap=0.00, xaxis_title=x_label, legend_title=None, yaxis_title="Replications")

    # Add the vertical dotted lines
    fig.add_vline(x=mean, line_width=2, line_dash="dot", line_color="black", annotation_text="mean")
    fig.add_vline(x=p5, line_width=2, line_dash="dot", line_color="black", 
                  annotation_text="5th", annotation_position="top left")
    fig.add_vline(x=p95, line_width=2, line_dash="dot", line_color="black", annotation_text="95th")
    
    # Add CI for mean
    fig.add_vrect(x0=lower_limit, x1=upper_limit, line_width=0, fillcolor="#FFA726", opacity=0.5)  # Orange  

    # avoid approximation issues with small samples.  
    if len(data) >= MIN_N_FOR_PERCENTILE:

        # add the percentile large sample confidence intervals
        df = pd.DataFrame(data)
        df.columns = ['KPI']
        
        x0, x1 = ci_percentile(df, "KPI", 0.95)
        fig.add_vrect(x0=x0, x1=x1, 
                      line_width=0, 
                      fillcolor="#FFA726", 
                      opacity=0.4,
                      showlegend=True,
                      name="CI 95th Percentile")  # Orange

        x0, x1 = ci_percentile(df, "KPI", 0.05)
        fig.add_vrect(x0=x0, x1=x1, 
                      line_width=0, 
                      fillcolor="#FFA726", 
                      opacity=0.4, 
                      showlegend=True,
                      name="CI 5th Percentile")  # Orange

    
    elif not suppress_warnings:
        warnings.warn(WARN)

    note = 'Shaded regions around vertical lines are 95% Confidence Intervals'
    fig.add_annotation(
        showarrow=False,
        text=note,
        font=dict(size=10), 
        xref='x domain',
        x=0.0,
        yref='y domain',
        y=-0.25
        )

    # update legend position
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))

    return fig
