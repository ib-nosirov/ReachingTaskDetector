import numpy as np
import load_data
import model_position
import plot_data as plot

object_arrs = load_data.create_np_arr('../tests/data/IMG_42860.csv')
np_pellet = object_arrs['pellet']
load_data.apply_prob_filter(np_pellet)
np_left_front_paw = object_arrs['left_front_paw']
load_data.apply_prob_filter(np_left_front_paw)

np_pellet_copy = np_pellet
np_left_front_paw_copy = np_left_front_paw

#plot.make_xcoord_scatter('x-position vs time', 'time', 'x-position',
#np_pellet_copy, np_left_front_paw_copy)
model_position.reach(np_left_front_paw_copy[:, 0])
