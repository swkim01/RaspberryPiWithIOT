import plotly.plotly as py
from plotly.graph_objs import *

from datetime import datetime
x = [
    datetime(year=2015, month=3, day=04),
    datetime(year=2015, month=4, day=05),
    datetime(year=2015, month=5, day=06)
]

data = Data([
    Scatter(
        x=x,
        y=[1, 3, 6]
    )
])
plot_url = py.plot(data, filename='python-datetime')
