import math
import numpy as np
from ray import Ray

class Camera:
    def __init__(self, origin): #facing positive z
        self.origin = origin
        self.rays = []
    
    def add_ray(self, x, y, z):
        dir = np.array([x, y, z])/np.linalg.norm(np.array([x, y, z]))
        ray = Ray(dir, self.origin) # normalized directional ray
        self.rays.append(ray)
    