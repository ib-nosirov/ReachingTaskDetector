import numpy as np

def position_reach(np_arr):
  is_reaching = False
  temp = 0
  for i in range(np_arr.shape[0]-1):
    if(np_arr[i] < 755 and not is_reaching):
      temp = i
      is_reaching = True
      print('start' + str(convert_to_time(i)))
        
    if(is_reaching and (i - temp)>30):
      print('end' + str(convert_to_time(i)))
      is_reaching = False
   
  print(reach_count)

#def classify_attempt(np_arr):
  

def position_reach_with_pellet(np_arr):
  is_reaching = False
  reach_count = 0
  temp = 0
  for i in range(np_arr.shape[0]-1):
    if(np_arr[i,0] < 755 and not is_reaching and not np.isnan(np_arr[i,1])):
      temp = i
      is_reaching = True
      print('start' + str(convert_to_time(i)))
      reach_count = reach_count + 1
        
    if(is_reaching and (i - temp)>30):
      print('end' + str(convert_to_time(i)))
      is_reaching = False
   
  print(reach_count)

def sliding_window(np_arr):
  np_sums = np.empty(np_arr.shape[0] - 30, dtype=np.float32)
  np_sums[:] = np.NaN
  for i in range(np_arr.shape[0] - 30):
    if(np_arr[i] < 810 and np_arr[i] > 740):
      sum = 0
      for j in range(30):
        sum = sum + np_arr[i+j]
      if(not np.isnan(sum)):
        np_sums[i] = sum
  return np_sums

def velocity_reach(np_arr):
  is_reaching = False
  reach_count = 0
  for i in range(np_arr.shape[0] - 1):
    if(np_arr[i] < 810 and np_arr[i] > 740):
      temp = i+1
      velocity = (np_arr[i] - np_arr[temp])/(i - temp)
      if(velocity < -10 and not is_reaching):
        is_reaching = True
        reach_count = reach_count + 1
        #print('reach ' + str(convert_to_time(i)))
      else:
        is_reaching = False

  print(reach_count)

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

def convert_windows_to_time(frame):
  frame = frame + 20
  time = float(frame / 59)
  seconds = float(time % 60)
  minutes = int(time / 60)
  return (minutes,seconds)
