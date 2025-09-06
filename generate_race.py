import svgpathtools as svg
import numpy as np
import matplotlib.pyplot as plt
from drone import Drone
from simulation import simulation
from scipy.integrate import solve_ivp                                                                                                                                                                                                                                          

def generate_race(track_id, drone):
    path = svg.svg2paths("tracks/" + track_id + ".svg")[0][0]
    t0 = 0.0
    drone.t = t0
    starting_point = np.array([np.real(path.point(t0)), np.imag(path.point(t0))])
    drone.pos = starting_point
    starting_tangent = path.unit_tangent(t0)
    starting_angle = np.arctan2(np.imag(starting_tangent), np.real(starting_tangent))

    u0 = np.concatenate([starting_point, [starting_angle, 0.0]])
    ode_fun = lambda t,u : simulation(drone, path, u)

    def win_event(t,u):
        du = simulation(drone, path, u)
        return 0.95 - drone.t
    
    def lose_event(t,u):
        du = simulation(drone,path,u)
        return 5 - abs(drone.distance(path))

    win_event.terminal = True
    lose_event.terminal = True

    sol = solve_ivp(ode_fun,[0.0,10000.0],u0, max_step = 1, events=[win_event,lose_event], dense_output=True)
    return sol
