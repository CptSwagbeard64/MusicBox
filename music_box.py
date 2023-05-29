import os
import argparse

from file_type.mdl_file import MDLFile
from file_type.obj_file import OBJFile


def convert_files(in_f, out_f):
    """ Converts a file from MDL to OBJ """
    if in_f == '' or not os.path.exists(in_f):
        print(f'File "{in_f}" not found.')
        return

    existing_file = MDLFile(in_f)

    if out_f is not None:
        new_file = OBJFile(out_f)
    else:
        new_file = OBJFile(in_f.replace('.mdl', '.obj'))

    existing_file.parse()
    new_file.v = existing_file.vertices
    new_file.f = existing_file.faces

    print(f'Parsed verts: {len(new_file.v)}')
    print(f'Parsed faces: {len(new_file.f)}')

    new_file.export()
    print(f'OBJ exported successfully: {new_file.fn}')


def main():
    """ Parse arguments and call convert function """
    parser = argparse.ArgumentParser(description="Converts MDL to OBJ")
    parser.add_argument('file', help='Specifies the MDL file to convert to OBJ')
    parser.add_argument('-o', '--output', help='Specifies name of the OBJ file to create (uses MDL name by default)')
    args = parser.parse_args()
    convert_files(args.file, args.output)


if __name__ == '__main__':
    main()
