# print('Hello!')
# for i in range(10, 0, -2):
#     print(i)

# PLOT . LY - basic example

import plotly.plotly as py
from plotly.graph_objs import *

py.sign_in('PythonAPI', 'ubpiol2cve')

data = Data([
    Bar(
        x=['giraffes', 'orangutans', 'monkeys'],
        y=[20, 14, 23]
    )
])
plot_url = py.plot(data, filename='basic-bar')