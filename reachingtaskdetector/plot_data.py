import numpy as np
from matplotlib import pyplot as plt

def make_scatterplot(x, y, color=None, title, x_axis, y_axis):
  plt.title(title)
  plt.xlabel(x_axis)
  plt.ylabel(y_axis)
  plt.scatter(t, y, c=color)

  # Make the plot.
  plt.show()
