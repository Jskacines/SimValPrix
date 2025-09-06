import numpy as np
def simulation(drone,track,u):
    max_speed = 10.0
    max_omega = 10.0
    max_accel = 1.0
    x,y,theta,v = u
    drone.pos = np.array([x,y])
    drone.theta = theta
    drone.speed = v
    accel, omega = drone.control(track)
    drone.omega = omega
    alpha = 0.0

    np.clip(v, -max_speed, max_speed)
    np.clip(omega, -max_omega, max_omega)
    np.clip(accel,-max_accel, max_accel)

    du = [
        v*np.cos(theta), v*np.sin(theta), omega, accel
    ]
    return du
