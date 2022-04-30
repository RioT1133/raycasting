from OpenGL.GL import *
from OpenGL.GLUT import *
import random


width, height = 400, 300

def draw_pixels():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    data = [random.randint(0, 255) for _ in range (0, height*width*3)] # data must be a one-dimensional array, each pixel has 3 consecutive values
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


