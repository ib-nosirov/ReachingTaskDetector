from reachingtaskdetector import load_data
from reachingtaskdetector import model_position

def test_1():
  object_arrs = load_data.create_np_arr('data/preop_1.csv')
  load_data.apply_lh_filter(object_arrs["left_paw"])
  pellet_np_arr = object_arrs["pellet"]
  
  timestamps_list = model_position.create_timestamps(pellet_np_arr)
  model_position.output_timestamps(timestamps_list)
