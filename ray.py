from cmath import inf
import math
import numpy as np

class Ray:
    def __init__(self, dir, origin):
        self.dir = dir
        self.origin = origin

    # doomsday source: https://cadxfem.org/inf/Fast%20MinimumStorage%20RayTriangle%20Intersection.pdf
    def cast(self, polygon): # begin doomsday
        # print(f"casting ray with direction {self.dir} and origin {self.origin}")
        e1 = np.subtract(polygon.v1, polygon.v0)
        e2 = np.subtract(polygon.v2,polygon.v0)
        bigT = np.subtract(self.origin, polygon.v0)

        c1 = np.cross(self.dir, e2)
        c2 = np.cross(bigT, e1)

        inverse = 1/(np.dot(c1, e1))

        t = inverse*np.dot(c2, e2)
        u = inverse*np.dot(c1, bigT)
        v = inverse*np.dot(c2, self.dir)

        print(t, u, v)

        if u >= 0 and v >= 0 and u + v <= 1:
            return t
        else:
            return inf
        