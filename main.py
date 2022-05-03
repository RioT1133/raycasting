from OpenGL.GL import *
from OpenGL.GLUT import *
import random
from pixelData import PixelData
from ray import Ray

width, height = 400, 300

horizontal_fov = 92 # degrees
vertical_fov = (float(horizontal_fov)/float(width))*float(height) # degrees

d_alpha = float(horizontal_fov)/float(width) # degrees

init_dir = 0.0 # degrees

rays = []

for i in range(height):
    for j in range(width):
        ray = Ray(float(height/2-i)  * d_alpha, float(-width/2+j) * d_alpha + init_dir)
        rays.append(ray)

pixel_data = PixelData(width, height)

def draw_pixels():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    data = pixel_data.pixels # data must be a one-dimensional array, each pixel has 3 consecutive values
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


