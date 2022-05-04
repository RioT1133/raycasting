import math
import random

class PixelData:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [0 for i in range(3*width*height)]
    
    def get_pixel(self, x, y):
        return((self.pixels[3*self.width*y + x], self.pixels[3*self.width*y + x + 1], self.pixels[3*self.width*y + x + 2])) # returns the pixel's (at x, y) current rgb values in a tuple
    
    def set_pixel(self, x, y, new_r, new_b, new_g):
        self.pixels[3*self.width*y + x] = new_r
        self.pixels[3*self.width*y + x + 1] = new_b
        self.pixels[3*self.width*y + x + 2] = new_g
    