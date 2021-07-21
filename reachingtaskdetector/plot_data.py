import numpy as np
from matplotlib import pyplot as plt

def make_xcoord_scatter(title, x_axis, y_axis, *args):
  plt.title(title)
  plt.xlabel(x_axis)
  plt.ylabel(y_axis)

  # Stack scatterplots
  for tuple in args:
    t_minutes = convert_frames_to_minutes(tuple.shape[0])
    plt.scatter(t_minutes, tuple[:,0], s=5)

  # Make the plot.
  plt.show()

def convert_frames_to_minutes(num_frames):
  np_frames = np.arange(num_frames)
  return np_frames / 3600.
