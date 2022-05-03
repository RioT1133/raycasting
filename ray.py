import math

class Ray:
    def __init__(self, inclination_angle, azimuth): # inclination is up-down (+-z), azimuth is left-right(+-y)
        self.x = math.sin(math.radians(inclination_angle))*math.cos(math.radians(azimuth))
        self.y = math.sin(math.radians(inclination_angle))*math.sin(math.radians(azimuth))
        self.z = math.cos(math.radians(inclination_angle))
        print(self.x, self.y, self.z, inclination_angle, azimuth)