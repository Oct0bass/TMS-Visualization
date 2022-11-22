from manim import *

from util import x, y


def _crossing_slope(line: Line, crossing: Line):
    lxrange, lyrange = np.vstack(line.start, line.end).T
    cxrange, cyrange = np.vstack(crossing.start, crossing.end).T
    pass


def is_point_inside(point: np.array, outer: VMobject):
    ray = Line(point, (8, point[0]))
    windnum = 0
    pass
