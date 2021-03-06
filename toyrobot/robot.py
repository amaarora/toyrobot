# AUTOGENERATED! DO NOT EDIT! File to edit: 02_robot.ipynb (unless otherwise specified).

__all__ = ['ToyRobot', 'Table']

# Cell
from .direction import Direction
import numpy as np
from numpy import sin, cos, pi

# Cell
class ToyRobot:
    "The actual ToyRobot class the does the moving."
    def __init__(self, x, y, idx=None, th=5, tw=5, verbose=False):
        self.f = Direction(idx=idx)
        self.x = x
        self.y = y
        self.table = Table(th, tw)
        self.verbose = verbose

    def report(self):
        "report the current (X,Y) coordinates and direction."
        print(f"{self.x},{self.y},{self.f}")

    def left(self):
        "update direction anticlockwise."
        self.f = self.f.left()
        if self.verbose: self.report()

    def right(self):
        "update direction clockwise."
        self.f = self.f.right()
        if self.verbose: self.report()

    def move(self):
        """
        get curent direction, take a step in the direction and only update the X and Y coords
        if the new position is inside the table.
        """
        idx = self.f.get_idx()
        new_x = self.x + (sin(idx*(pi/2)).astype(int))
        new_y = self.y + (cos(idx*(pi/2)).astype(int))
        if (new_x, new_y) in self.table:
            self.x = new_x
            self.y = new_y
        if self.verbose: self.report()

    @classmethod
    def from_placement(cls, x:int, y:int, idx:int, verbose=False):
        "place a robot if it's inside the table and ignore otherwise"
        if not (isinstance(x, int) and isinstance(y, int)):
            raise ValueError(f"only integer values are acceptable for `x`, `y` coordinates.")

        if max(x,y)<=5:
            return cls(x, y, idx=idx, verbose=verbose)

# Cell
class Table:
    def __init__(self, h=5, w=5):
        self.h = h
        self.w = w

    def __contains__(self, o):
        if isinstance(o, ToyRobot):
            return min(self.h, self.w) >= max(o.x, o.y)
        else:
            return min(self.h, self.w) >= max(o[0], o[1])