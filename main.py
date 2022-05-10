from OpenGL.GL import *
from OpenGL.GLUT import *
from cmath import inf
import math
import numpy as np
import random
from camera import Camera
from pixelData import PixelData
from polygon import Polygon
from ray import Ray
from world import World

width, height = 400, 300

horizontal_fov = 120

plane_dist = width/(2*math.tan(math.radians(horizontal_fov/2)))

d_alpha = float(horizontal_fov)/float(width) # degrees

x_inc = 0
y_inc = 0

v0 = np.array([5.0, 1.0, 7.5])
v1 = np.array([-2.0, 4.0, 7.0])
v2 = np.array([-2.0, -2.0, 6.0])
v3 = np.array([0.0, 0.0, 2.0])

p1 = Polygon(v0, v1, v2)
p2 = Polygon(v1, v2, v3)
p3 = Polygon(v2, v3, v0)
p4 = Polygon(v3, v0, v1)

world = World([p1, p2, p3, p4])

camera = Camera(np.array([-0.0, 0.0, 0.0]))

pixelData = PixelData(width, height)


for i in range(height):
    for j in range(width):
        camera.add_ray(-width/2 + j, -height/2 + i, plane_dist)
        # print(-width/2 + j, -height/2 + i, plane_dist)

for i in range(len(camera.rays)):
    smallest_dist = inf
    for j in range(len(world.polygons)):
        distance = camera.rays[i].cast(world.polygons[j])
        if distance < smallest_dist:
            smallest_dist = distance
    # print(i%width, i//width)
    # print(distance)
    if smallest_dist == inf:
        brightness = 0
    else:
        # print(distance)
        brightness = int(((-(math.sqrt(smallest_dist))) + 255) * 128.0)
    # print(brightness)
    pixelData.set_pixel(i%width, i//width, brightness, brightness, brightness)


def draw_pixels():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    data = pixelData.pixels # data must be a one-dimensional array, each pixel has 3 consecutive values
    glDrawPixels(width, height, GL_RGB, GL_UNSIGNED_BYTE, (GLubyte * len(data))(*data)) # last argument typecasts data into a list of GLubytes
    glutSwapBuffers()

def setup():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(200, 200)
    window = glutCreateWindow("wassup gang")
    glutDisplayFunc(draw_pixels)
    glutIdleFunc(draw_pixels)
    glutMainLoop()

if __name__ == "__main__":
    setup()


