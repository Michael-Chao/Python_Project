import plotly as py
import numpy as np
import pandas as pd
import plotly.figure_factory as ff

if __name__ == "__main__":
    data = pd.read_csv("gantt.csv")

    pyplt = py.offline.plot
    fig = ff.create_gantt(data)
    pyplt(fig, filename="gantt_chart.html")