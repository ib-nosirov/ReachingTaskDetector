import numpy as np

def reach(np_arr):
  is_reaching = False

  for i in range(np_arr.shape[0] - 1):
    if(np_arr[i] < 810 and np_arr[i] > 740):
      temp = i+1
      while(np_arr[i] == np.nan):
        i = i + 1
        print(i)
      velocity = (np_arr[i] - np_arr[temp])/(i - temp)
      if(velocity < -50 and not is_reaching):
        is_reaching = True
        print('reach ' + str(convert_to_time(i)))
      else:
        is_reaching = False

def create_timestamps(data_frame):
  timestamps_list = []
  attempt_ongoing = False
  for i in range(data_frame.shape[0]):
    if(data_frame[i,2] > 0.8):
      if(not attempt_ongoing):
        attempt_ongoing = True
        time = convert_to_time(i/59)
        timestamps_list.append(time)
      else:
        if(attempt_ongoing):
          time = convert_to_time(i/59)
          timestamps_list.append(time)
          attempt_ongoing = False
  return timestamps_list
  
def output_timestamps(timestamps_list):
  i = 0
  for time in timestamps_list:
    if (i%2 == 0):
      print("Start Attempt: ", str(time[0]) + ":" + str(time[1]))
    else:
      print("End Attempt: ", str(time[0]) + ":" + str(time[1]))
    i = i+1


def convert_to_time(frame):
  time = float(frame / 59)
  seconds = float(time % 60)
  minutes = int(time / 60)
  return (minutes,seconds)

