# AUTOGENERATED! DO NOT EDIT! File to edit: 02_robot.ipynb (unless otherwise specified).

__all__ = ['ToyRobot', 'Table']

# Cell
from .direction import Direction
import numpy as np
from numpy import sin, cos, pi

# Cell
class ToyRobot:
    def __init__(self, x, y, idx=None, th=5, tw=5):
        self.f = Direction(idx=idx)
        self.x = x
        self.y = y
        self.table = Table(th, tw)

    def __repr__(self):
        return f"{self.__class__.__name__}, currently at ({self.x}, {self.y}) and facing {self.f}!"

    def report(self): print(self)

    def left(self):
        self.f = self.f.left()
        print(f"{self.__class__.__name__} facing new direction: {self.f}")

    def right(self):
        self.f = self.f.right()
        print(f"{self.__class__.__name__} facing new direction: {self.f}")

    def move(self):
        idx = self.f.get_idx()
        self.x = self.x + (sin(idx*(pi/2)).astype(int))
        self.y = self.y + (cos(idx*(pi/2)).astype(int))
        print(f"New position on table: {self.x, self.y}")

    @classmethod
    def from_placement(cls, x, y, idx):
        return cls(x, y, idx=idx)

# Cell
class Table:
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def __contains__(self, robot: ToyRobot):
        return min(self.h, self.w) >= max(robot.x, robot.y)