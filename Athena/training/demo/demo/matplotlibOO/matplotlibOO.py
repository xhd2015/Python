#!/usr/bin/env python
"""
A pure OO example using the agg backend.

Original code from http://matplotlib.sourceforge.net/leftwich_tut.txt
"""
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

fig = Figure()
canvas = FigureCanvas(fig)
ax = fig.add_subplot(111)
ax.plot([1,2,3])
ax.set_title('hi plamen')
ax.grid(True)
ax.set_xlabel('time')
ax.set_ylabel('volts')

# Print to a png file
canvas.print_figure('test', dpi = 500)
