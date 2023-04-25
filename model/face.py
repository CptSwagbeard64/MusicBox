from model.vertex import Vertex


class Face:

    def __init__(self, vert1, vert2, vert3):
        self.v1 = vert1
        self.v2 = vert2
        self.v3 = vert3

    def __str__(self):
        return f'f {self.v1} {self.v2} {self.v3}'
