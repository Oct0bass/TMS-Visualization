from manim import *
import math


def x(a): return a[0]
def y(a): return a[1]


def slope(start, end, line: Line = None):
    if line is not None:
        if start or end:
            raise ValueError("cannot accept both slope and line")
        start = line.start
        end = line.end

    dx = x(end) - x(start)
    if dx == 0:
        return math.inf
    return (y(start) - y(end))/dx
