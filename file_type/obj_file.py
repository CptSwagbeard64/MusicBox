from model.vertex import Vertex
from model.face import Face


class OBJFile:

    def __init__(self, file_name):
        self.fn = file_name
        self.v = []
        self.f = []

    def export(self):
        with open(self.fn, 'w') as file:
            data = [f'# Vertices {len(self.v)}\n']
            for v in self.v:
                data.append(f'v {v.x} {v.y} {v.z}\n')
            data.append('\n')

            data.append(f'# Faces {len(self.f)}\n')
            for f in self.f:
                data.append(f'f {f.v1} {f.v2} {f.v3}\n')
            data.append('\n')

            file.writelines(data)
