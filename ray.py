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
        e2 = np.subtract(polygon.v2, polygon.v0)
        h = np.cross(self.dir, e2)
        a = np.inner(e1, h)

        if a > -0.0000001 and a < 0.0000001:
            return inf

        f = 1/a

        s = np.subtract(self.origin, polygon.v0)
        u = np.inner(s, h) * f

        if u < 0 or u > 1:
            # print(f"broke at 1, u={u}")
            return inf

        q = np.cross(s, e1)
        v = np.inner(self.dir, q)

        if v < 0.0 or u + v > 1.0:
            # print("broke at 2")
            return inf

        t = np.inner(q, e2) * f
        return t
        