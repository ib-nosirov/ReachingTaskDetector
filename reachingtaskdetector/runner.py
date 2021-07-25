import numpy as np
import load_data
import model_position
import plot_data as plot

object_arrs = load_data.create_np_arr('../tests/data/IMG_42860.csv')
np_marker_arrs = object_arrs['left_front_paw', 'pellet', 'snout']

model_position.position_reach(np_marker_arrs)
