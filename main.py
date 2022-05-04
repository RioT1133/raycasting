from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
import random
from camera import Camera
from pixelData import PixelData
from polygon import Polygon
from ray import Ray
from world import World

width, height = 400, 300

horizontal_fov = 90 # degrees
vertical_fov = (float(horizontal_fov)/float(width))*float(height) # degrees

d_alpha = float(horizontal_fov)/float(width) # degrees

v0 = np.array([3.0, 0.0, 0.0])
v1 = np.array([3.3, 1.0, 1.0])
v2 = np.array([3.6, 1.0, -1.0])

polygon = Polygon(v0, v1, v2)

world = World([polygon])

init_dir = 0 # degrees

camera = Camera(np.array([0, 0, 0]), 0.0)

pixelData = PixelData(width, height)

for i in range(height):
    for j in range(width):
        inclination = float(height/2-i)  * d_alpha
        azimuth = float(-width/2+j) * d_alpha + init_dir
        camera.add_ray(inclination, azimuth)
        # print(inclination, azimuth)
        # print(len(camera.rays))

for i in range(len(camera.rays)):
    distance = camera.rays[i].cast(world)
    # print(i%width, i//width)
    pixelData.set_pixel(i%width, i//width, distance, distance, distance)


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


