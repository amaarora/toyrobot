# AUTOGENERATED! DO NOT EDIT! File to edit: 03_main.ipynb (unless otherwise specified).

__all__ = ['get_direction_idx', 'main']

# Cell
from .direction import Direction
from .robot import *
from argparse import ArgumentParser
import re

# Cell
def get_direction_idx(direction, directions=['NORTH', 'SOUTH', 'EAST', 'WEST']):
    return directions.index(direction.upper())

# Cell
def main():
    parser = ArgumentParser()
    parser.add_argument(
        '--cmd_file_path',
        required=True,
        help="absolute path to the file containing commands for the ToyRobot."
    )
    args = parser.parse_args()
    robot = None
    f = open('./example1.txt', 'r')

    # make robot dance
    for line in f.readlines():
        args = re.findall(r'[^,\s]+', line)
        if args[0]=='PLACE' and robot is None:
            robot = ToyRobot.from_placement(int(args[1]), int(args[2]), get_direction_idx(args[3]))
        elif robot is not None and args[0] != 'PLACE':
            cmd = f"robot.{args[0].lower()}()"
            exec(cmd)

    robot.report()

# Cell
if __name__ == '__main__' and '__file__' in globals():
    main()