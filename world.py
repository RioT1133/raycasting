class World:
    def __init__(self, polygons=[]):
        self.polygons = polygons
    
    def add_polygon(self, p):
        self.polygons.append(p)