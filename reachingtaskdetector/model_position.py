import numpy as np

def get_reaches(np_arr, np_pellet):
    is_reaching = False
    temp = 0
    reach_list = []
    for i in range(np_arr.shape[0]-1):
        if(np_arr[i] < 765 and not is_reaching and not np.isnan(np_pellet[i])):
            temp = i
            is_reaching = True
            reach_list.append((i, i))

        if(is_reaching):
            if((i - temp)>30 or np_arr[i] > 765):
                is_reaching = False
                reach_list[-1] = (temp, i)
    return reach_list

def is_successful(np_snout_paw, end):
    truth_value = False
    count = 0
    for i in range(90):
        np_velocity = np_snout_paw[end+i+1] - np_snout_paw[end+i]
        if(np_velocity < 1 and np_velocity > -1):
            count = count + 1
    if(count > 30):
        truth_value = True
    return truth_value

def check_attempt(reach_list):
    attempts_list = [(reach_list[0][0], reach_list[0][1], 1)]
    for i in range(len(reach_list)-1):
        if(reach_list[i+1][0]-reach_list[i][1] < 60):
            if(reach_list[i+1][0]-attempts_list[-1][1] < 60):
                attempts_list[-1] = (attempts_list[-1][0], reach_list[i+1][1],
                                     attempts_list[-1][2]+1)
            else:
                attempts_list.append((reach_list[i][0], reach_list[i+1][1], 2))
        else:
            attempts_list.append((reach_list[i+1][0], reach_list[i+1][1], 1))
    return attempts_list

def convert_to_time(frame):
    time = float(frame / 60)
    seconds = float(time % 60)
    minutes = int(time / 60)
    return (minutes,seconds)
