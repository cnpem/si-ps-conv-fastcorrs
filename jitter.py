import epics
import time
import matplotlib.pyplot as plt
from collections import deque

# Store the last 100 jitter values
jitter_values = deque(maxlen=1000)
samples = 0
timestamp_Curr = None
timestamp_Kick = None

def on_change_Curr(pvname=None, value=None, char_value=None, **kwargs):
    global timestamp_Curr
    timestamp_Curr = time.time()
    #print(f"PV Curr changed to {value} at {timestamp_Curr}")

def on_change_Kick(pvname=None, value=None, char_value=None, **kwargs):
    global timestamp_Kick
    timestamp_Kick = time.time()
    #print(f"PV Kick changed to {value} at {timestamp_Kick}")
    calculate_jitter()

def calculate_jitter():
    global samples
    if timestamp_Curr is not None and timestamp_Kick is not None:
        jitter = timestamp_Kick - timestamp_Curr
        jitter_values.append(jitter)
        #print(f"Jitter between Curr and Kick: {jitter} seconds")
        samples += 1
        if samples > 1000:
            samples = 0
            print(f"Average jitter: {sum(jitter_values) / len(jitter_values)} seconds")

pv_Curr = epics.PV('SI-01M2:PS-FCH:Current-Mon', callback=on_change_Curr)
pv_Kick = epics.PV('my-SI-01M2:PS-FCH:Kick-Mon', callback=on_change_Kick)

# Keep the script running
while True:
    time.sleep(1)


