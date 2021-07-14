import numpy as np


def create_timestamps(data_frame):
  timestamps_list = []
  attempt_ongoing = False
  for i in range(data_frame.shape[0]):
    if (data_frame[i, 2] > 0.5):
      if (not attempt_ongoing):
        attempt_ongoing = True
        time = convert_to_time(i / 29)
        timestamps_list.append(time)
      else:
        if (attempt_ongoing):
          time = convert_to_time(i / 29)
          timestamps_list.append(time)
          attempt_ongoing = False
  return timestamps_list
  
def output_timestamps(timestamps_list):
  i = 0
  for time in timestamps_list:
    if (i % 2 == 0):
      print("Start Attempt: ", str(time[0]) + ":" + str(time[1]))
    else:
      print("End Attempt: ", str(time[0]) + ":" + str(time[1]))
    i = i + 1


def convert_to_time(time):
  seconds = int(time % 60)
  minutes = int(time / 60)
  return (minutes,seconds)
