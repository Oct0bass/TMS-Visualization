from manim import *
import math


def x(a): return a[0]
def y(a): return a[1]


def slope(start=None, end=None, line: Line = None):
    if start is None and end is None and line is None:
        raise ValueError("No points or line specified")

    if line is not None:
        if start is not None or end is not None:
            raise ValueError("Cannot accept both slope and line")
        start = line.start
        end = line.end

    dx = x(end) - x(start)
    if dx == 0:
        return math.inf
    return (y(start) - y(end))/dx
