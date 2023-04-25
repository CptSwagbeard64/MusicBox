import os
import sys

from file_type.mdl_file import MDLFile
from file_type.obj_file import OBJFile


def print_usage():
    print('Usage: music_box -f <input_file> [-o <output_file>]')


def convert_files(in_f='', out_f=''):
    if in_f != '' and os.path.exists(in_f):
        existing_file = MDLFile(in_file)

        if out_f != '':
            new_file = OBJFile(out_f)
        else:
            new_file = OBJFile(in_file.replace('.mdl', '.obj'))

        existing_file.parse()
        new_file.v = existing_file.vertices
        new_file.f = existing_file.faces

        print(f'Parsed verts: {len(new_file.v)}')
        print(f'Parsed faces: {len(new_file.f)}')

        new_file.export()
        print(f'OBJ exported successfully: {new_file.fn}')
    else:
        print(f'File "{in_f}" not found.')
        print_usage()


if __name__ == '__main__':
    in_file = ''
    out_file = ''
    arg_len = len(sys.argv)

    if arg_len < 2:
        print_usage()
    else:
        try:
            if sys.argv[1] == '-f':
                in_file = sys.argv[2]
                if arg_len == 5 and sys.argv[3] == '-o':
                    out_file = sys.argv[4]
            convert_files(in_file, out_file)

        except:
            print('Invalid arguments.\n')
            print_usage()

