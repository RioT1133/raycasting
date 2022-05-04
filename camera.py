import math
import numpy as np
from ray import Ray

class Camera:
    def __init__(self, origin, dir=0.0):
        self.origin = origin
        self.dir = dir
        self.rays = []
    
    def add_ray(self, inclination_angle, azimuth):
        x = math.sin(math.radians(inclination_angle))*math.cos(math.radians(azimuth))
        y = math.sin(math.radians(inclination_angle))*math.sin(math.radians(azimuth))
        z = math.cos(math.radians(inclination_angle))
        ray = Ray(np.array([x, y, z]), self.origin) # normalized directional ray
        self.rays.append(ray)
    