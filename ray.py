from asyncio.windows_events import NULL
import numpy as np

class Ray:
    def __init__(self, dir, origin): # inclination is up-down (+-z), azimuth is left-right(+-y)
        self.dir = dir
        self.origin = origin

    # doomsday source: https://cadxfem.org/inf/Fast%20MinimumStorage%20RayTriangle%20Intersection.pdf
    def cast(self, world): # begin doomsday
        shortest_distance = 255
        for polygon in world.polygons:
            e1 = np.subtract(polygon.v1, polygon.v0)
            e2 = np.subtract(polygon.v2, polygon.v0)
            h = np.cross(self.dir, e2)
            a = np.dot(e1, h)

            if a > -0.00001 and a < 0.00001:
                break

            f = 1/a

            s = np.subtract(self.origin, polygon.v0)
            u = np.dot(s, h) * f

            if u < 0 or u > 1:
                break

            q = np.cross(s, e1)
            v = np.dot(self.dir, q)

            if v < 0.0 or u + v > 1.0:
                break

            t = np.dot(q, e2) * f

            if t < shortest_distance:
                shortest_distance = t
        return shortest_distance # end doomsday