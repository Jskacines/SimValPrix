import svgpathtools as svg
from scipy.optimize import minimize_scalar

class Track:
    def __init__(self,track_id):
        self.path = svg.svg2paths(track_id)
        
        
