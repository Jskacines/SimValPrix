import numpy as np

def control_fun(distance, delta_angle, speed):
    if speed < 0.05:
        accel = 1.0
    else:
        accel = 0.0
    omega = 0.0
    return accel, omega