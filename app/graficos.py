import numpy as np
import pandas as pd
import altair as alt
from fh_altair import altair2fasthtml

def generate_chart1():
    pltr = pd.DataFrame({'y': [1, 2, 3, 2], 'x': [3, 1, 2, 4]})
    chart = alt.Chart(pltr).mark_line().encode(x='x', y='y').properties(width=400, height=200)
    return altair2fasthtml(chart)

def generate_chart2():
    pltr = pd.DataFrame({'y': [1, 2, 3, 2], 'x': [3, 1, 2, 4]})
    chart2 = alt.Chart(pltr).mark_line().encode(x='x', y='y').properties(width=400, height=200)
    return altair2fasthtml(chart2)