import numpy as np

def control_fun(distance, delta_angle, speed):
    if speed < 0.1:
        accel = 1.0
    else:
        accel = 0.0

    if distance > 0.0 and delta_angle > np.deg2rad(-15):
        omega = 0.05
    elif distance < 0.0 and delta_angle < np.deg2rad(15):
        omega = -0.05
    else:
        omega = 0.0

    return accel, omega


