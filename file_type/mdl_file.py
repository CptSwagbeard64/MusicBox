import numpy as np

from model.vertex import Vertex
from model.face import Face


class MDLFile:
    VERT_SIZE = 0x14

    def __init__(self, file_name):
        self.fn = file_name

        self.bytes = []
        self.vertices = []
        self.faces = []

        self.vertex_count = 0
        self.vertex_start_address = 0x00
        self.faces_start_address = 0x00
        self.faces_start_address = 0x00

    def read_bytes(self):
        with open(self.fn, "rb") as f:
            self.bytes = f.read()

    def find_vertex_start(self):
        ff_n = 0
        index = 0x00

        while self.vertex_start_address == 0x00:
            ff = (
                (self.bytes[index + 0] << 24) |
                (self.bytes[index + 1] << 16) |
                (self.bytes[index + 2] << 8) |
                (self.bytes[index + 3] << 0)
            )

            if ff == 4294967295:
                ff_n += 1

            if ff_n == 2:
                self.vertex_count = (self.bytes[index - 0x2E] << 8) | (self.bytes[index - 0x2D] << 0)
                index += 0x29
                self.vertex_start_address = index
                self.faces_start_address = self.vertex_start_address + (self.vertex_count * self.VERT_SIZE)
            else:
                index += 0x01

    def load_vertex_array(self):
        for index in range(self.vertex_start_address, self.faces_start_address, self.VERT_SIZE):
            x_half = ((self.bytes[index + 0] << 8) | (self.bytes[index + 1] << 0)).to_bytes(2, 'little')
            y_half = ((self.bytes[index + 2] << 8) | (self.bytes[index + 3] << 0)).to_bytes(2, 'little')
            z_half = ((self.bytes[index + 4] << 8) | (self.bytes[index + 5] << 0)).to_bytes(2, 'little')

            x = np.frombuffer(x_half, dtype=np.float16)[0]
            y = np.frombuffer(y_half, dtype=np.float16)[0]
            z = np.frombuffer(z_half, dtype=np.float16)[0]

            self.vertices.append(Vertex(x, y, z))

    def load_face_array(self):
        addr = self.faces_start_address
        while addr < len(self.bytes):
            vert_list = []
            vert = (self.bytes[addr] << 8) | (self.bytes[addr + 1] << 0)
            addr += 2

            while vert != 65535:
                if addr >= len(self.bytes) - 1:
                    return

                vert_list.append(vert)
                vert = (self.bytes[addr] << 8) | (self.bytes[addr + 1] << 0)
                addr += 2

            for vert_idx in range(len(vert_list)):
                if vert_idx + 1 < 3:
                    continue

                if vert_idx % 2 == 1:
                    self.faces.append(Face(
                        vert_list[vert_idx - 2] + 1,
                        vert_list[vert_idx - 1] + 1,
                        vert_list[vert_idx - 0] + 1,
                    ))
                else:
                    self.faces.append(Face(
                        vert_list[vert_idx - 0] + 1,
                        vert_list[vert_idx - 2] + 1,
                        vert_list[vert_idx - 1] + 1,
                    ))

    def parse(self):
        self.read_bytes()
        self.find_vertex_start()
        self.load_vertex_array()
        self.load_face_array()

