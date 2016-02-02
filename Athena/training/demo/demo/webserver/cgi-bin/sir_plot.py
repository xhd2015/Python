
import os

# matplotlib needs a valid MPLCONFIGDIR environment variable for its rc file.
# We set it to the current directory before importing matplotlib.
os.environ['MPLCONFIGDIR'] = './mpl_config'

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


def plot_solution(t, sol):
    """
    Plot the solution to the SIR equations in three subplots.

    Returns an instance of a FigureCanvas (actually
    matplotlib.backends.backend_agg.FigureCanvasAgg).  Call the method
    print_figure(file) of this object to write the figure as a PNG file to
    'file'.
    """
    fig = Figure(figsize=(5,4), dpi=72)
    fig.subplots_adjust(hspace=0.4)
    
    S, I, R = sol.T

    # Plot S(t)
    ax1 = fig.add_subplot(3, 1, 1)
    ax1.plot(t, S)
    ax1.set_xlim(xmax=t[-1])
    ax1.set_title(r'$S(t)$', fontsize=10)
    ax1.set_xticklabels([])
    ylabels = ax1.get_yticklabels()
    for lbl in ylabels:
        lbl.set_fontsize(8)

    # Plot I(t)
    ax2 = fig.add_subplot(3, 1, 2)
    ax2.plot(t, I)
    ax2.set_xlim(xmax=t[-1])
    ax2.set_title(r'$I(t)$', fontsize=10)
    ax2.set_ylim(ymin=0.0)
    ax2.set_xticklabels([])
    ylabels = ax2.get_yticklabels()
    for lbl in ylabels:
        lbl.set_fontsize(8)

    # Plot R(t)
    ax3 = fig.add_subplot(3, 1, 3)
    ax3.plot(t, R)
    ax3.set_xlim(xmax=t[-1])
    ax3.set_title(r'$R(t)$', fontsize=10)
    ylabels = ax3.get_yticklabels()
    for lbl in ylabels:
        lbl.set_fontsize(8)
    xlabels = ax3.get_xticklabels()
    for lbl in xlabels:
        lbl.set_fontsize(8)
    ax3.set_xlabel('t', fontsize=8)

    # Send the PNG file to stdout
    canvas = FigureCanvas(fig)
    return canvas


def bad_values_canvas():
    fig = Figure(figsize=(7, 1), dpi=200)
    ax1 = fig.add_subplot(1, 1, 1)
    # ax1.set_frame_on(False)
    ax1.set_axis_off()
    ax1.text(0, 0.5, 'Bad numeric data entered. Please check your numbers.',
             bbox=dict(facecolor='red'))
    # (To do: tell the user *which* number is bad!) 
    canvas = FigureCanvas(fig)
    return canvas
