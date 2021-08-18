import numpy as np
import pandas as pd
def create_np_arr(data_path):
  """Create a dictionary of NumPy arrays with labels corresponding to each
     object marker.
     The arrays contain three columns:
       column 1: x_coord
       column 2: y_coord
       column 3: likelihood - lh

  Args:
    data_path: The full path of the .csv file containing object marker
      positions for every frame of video.
  """
  # Read in data from path
  data_frame = read_in_file(data_path)

  # Extract the labels of the object markers.
  df_labels = get_labels(data_frame)

  # Clean up extraneous labels.
  data_frame = remove_labels(data_frame)

  # Split and sort the array into corresponding to labels
  numpy_df = data_frame.to_numpy(dtype = 'float32')
  numpy_dict = create_np_dict(df_labels, numpy_df)
  return numpy_dict

def create_np_dict(labels_list, numpy_df):
  numpy_dict = {}
  for i in range(0, numpy_df.shape[1], 3):
    j = int(i / 3)
    numpy_dict[labels_list[j]] = numpy_df[:, i:i + 3]
  return numpy_dict

def remove_labels(data_frame):
  data_frame = data_frame.iloc[2:, 1:]
  data_frame = data_frame.reset_index(drop=True)
  return data_frame

def get_labels(data_frame):
  return [i for i in data_frame.iloc[0, 1::3]]

def read_in_file(data_path):
  return pd.read_csv(data_path)

def apply_prob_filter(numpy_arr, threshold=.5):
  for i in range(numpy_arr.shape[0]):
    if(numpy_arr[i, 2] < threshold):
      numpy_arr[i, 1] = np.nan 
      numpy_arr[i, 0] = np.nan
