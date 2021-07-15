# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

# %% [markdown]
# # Pellet-Position Model
# The pupose of this notebook is to clean DLC output data and create a model that predicts reaching attempts based on pellet position.

# %%
def read_in_file(data_path):
    return pd.read_csv(data_path)

data_path = '/Users/ib-nosirov/REU_2021/ReachingTaskDetector/tests/data/1 preopDLC_resnet_50_pre_post_opJul4shuffle1_550000.csv'
df = read_in_file(data_path)
df

# %%
[i for i in df.iloc[0, 1::3]]

# %%
df_pellet = df.iloc[2:, 10:13]
df_pellet = df_pellet.reset_index(drop=True)

# %%
df_pellet = df_pellet.rename(columns = {'DLC_resnet_50_pre_post_opJul4shuffle1_550000.9': 'x_coord', 'DLC_resnet_50_pre_post_opJul4shuffle1_550000.10': 'y_coord', 'DLC_resnet_50_pre_post_opJul4shuffle1_550000.11': 'prob'})

# %%
df_pellet = df_pellet.to_numpy(dtype ='float32')

# %%
df_pellet.shape

# %%
for i in range(df_pellet.shape[0]):
    if (df_pellet[i, 2] < 0.5):
        df_pellet[i, 1] = 0
        df_pellet[i, 0] = 0

# %%
import numpy as np 
from matplotlib import pyplot as plt 

t = np.arange(5805)
y = df_pellet[:,1]
prob = df_pellet[:,2]
plt.title("y-position vs time") 
plt.xlabel("time") 
plt.ylabel("y-position") 
plt.scatter(t,y, c=prob)
plt.show()

# %%
t = np.arange(5805)
x = df_pellet[:,0]
prob = df_pellet[:,2]
plt.title("x-position vs time") 
plt.xlabel("time") 
plt.ylabel("x-position") 
plt.scatter(t, x, c=prob)
plt.show()


# %%
def convert_to_time(time):
    seconds = int(time % 60)
    minutes = int(time / 60)
    return (minutes, seconds)


# %%
# convert to time stamps
def output_time_stamps(data_frame):
    attempt_ongoing = False
    for i in range(data_frame.shape[0]):
        if (data_frame[i, 2] > 0.5):
            if (not attempt_ongoing):
                attempt_ongoing = True
                time = convert_to_time(i / 29)
                print("Start Attempt: ", str(time[0]) + ":" + str(time[1]))
        else:
            if (attempt_ongoing):
                time = convert_to_time(i / 29)
                print("End Attempt: ", str(time[0]) + ":" + str(time[1]))
                attempt_ongoing = False


# %%
output_time_stamps(df_pellet)

# %%
