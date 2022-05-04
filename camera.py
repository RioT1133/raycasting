import math
from ray import Ray

class Camera:
    def __init__(self, x, y, z, dir=0.0):
        self.x = x
        self.y = y
        self.z = z
        self.dir = dir
        self.rays = []
    
    def add_ray(self, inclination_angle, azimuth):
        x = math.sin(math.radians(inclination_angle))*math.cos(math.radians(azimuth))
        y = math.sin(math.radians(inclination_angle))*math.sin(math.radians(azimuth))
        z = math.cos(math.radians(inclination_angle))
        ray = Ray(x, y, z)
    