class Vertex:

    def __init__(self, x_pos, y_pos, z_pos):
        self.x = x_pos
        self.y = y_pos
        self.z = z_pos

    def __str__(self):
        return f'v {self.x} {self.y} {self.z}'
