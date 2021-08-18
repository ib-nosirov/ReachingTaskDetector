import numpy as np
import load_data
import model_position
import plot_data as plot

marker_dict = load_data.create_np_arr('../tests/data/IMG_4286.csv')
np_left_front_paw = marker_dict['left_front_paw']
load_data.apply_prob_filter(np_left_front_paw)
np_pellet = marker_dict['pellet']
load_data.apply_prob_filter(np_pellet)
np_snout = marker_dict['snout']
load_data.apply_prob_filter(np_snout)

np_snout_paw = np_snout - np_left_front_paw

for i in range(np_pellet.shape[0]):
  if(np_pellet[i, 0] > 765):
    np_pellet[i, 1] = np.nan 
    np_pellet[i, 0] = np.nan

reach_list = model_position.get_reaches(np_left_front_paw[:,0], np_pellet[:,0])
attempts_list = model_position.check_attempt(reach_list)

for e in attempts_list:
  if(e[2] < 3 and model_position.is_successful(np_snout_paw[:,0], e[1])):
    print(model_position.convert_to_time(e[0]),
        model_position.convert_to_time(e[1]), 'success')
  else:
    print(model_position.convert_to_time(e[0]),
          model_position.convert_to_time(e[1]), 'failure')
plot.make_xcoord_scatter('Paw x-position vs. Minutes', 'Minutes',
'Paw x-position', np_left_front_paw[:2000])
