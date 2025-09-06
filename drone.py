import svgpathtools as svg
import numpy as np
from scipy.optimize import minimize, Bounds
from scipy.optimize import minimize_scalar

class Drone:
    def __init__(self, control_fun):
        self.pos = np.array([0.0,0.0])
        self.speed = 0.0
        self.theta = 0.0
        self.omega = 0.0
        self.t = 0.0
        self.control_fun = control_fun

    def path_t(self,track):
        dist_fun = lambda t: np.linalg.norm(self.pos - np.array([np.real(track.point(t)), np.imag(track.point(t))]))
        lb = np.clip(self.t - 0.05, 0,1)
        ub = np.clip(self.t + 0.05, 0,1)

        res = minimize_scalar(dist_fun, bounds=(lb,ub))
        self.t = res.x

    def distance(self,track):
        point = np.array([np.real(track.point(self.t)), np.imag(track.point(self.t))])
        distance_vec = np.array(self.pos - point)
        abs_distance = np.linalg.norm(distance_vec)
        track_norm = np.array([np.real(track.normal(self.t)), np.imag(track.normal(self.t))])
        distance_sign = np.sign(np.dot(distance_vec, track_norm))
        return abs_distance*distance_sign

    def angle(self,track):
        tangent = np.array([np.real(track.unit_tangent(self.t)),np.imag(track.unit_tangent(self.t))])
        trajectory = np.array([np.cos(self.theta), np.sin(self.theta)])
        tangent_angle = np.arctan2(np.cross(trajectory, tangent), np.dot(trajectory, tangent))
        return tangent_angle

    def control(self, track):
        self.path_t(track)
        distance = self.distance(track)
        delta_angle = self.angle(track)
        speed = self.speed
        accel, omega = self.control_fun(distance, delta_angle, speed)
        return accel, omega
    


    