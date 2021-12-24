# -*- coding: utf-8 -*-

# python imports
from math import degrees

# pyfuzzy imports
from fuzzy.storage.fcl.Reader import Reader


def lineEquation((x1, y1), (x2, y2), x):
    if x2 - x1 == 0:
        y = x1
    else:
        m = (y2 - y1) / (x2 - x1)
        b = -1 * m * x1 - y1
        y = m * x + b
    return y


def up_more_right_pa(x):
    (x1, y1), (x2, y2), (x3, y3) = (0, 0), (30, 1), (60, 0)
    if x1 <= x <= x2:
        return lineEquation((x1, y1), (x2, y2), x)
    elif x2 <= x <= x3:
        return lineEquation((x3, y3), (x2, y2), x)
    else:
        return 0


def up_right_pa(x):
    (x1, y1), (x2, y2), (x3, y3) = (30, 0), (60, 1), (90, 0)
    if x1 <= x <= x2:
        return lineEquation((x1, y1), (x2, y2), x)
    elif x2 <= x <= x3:
        return lineEquation((x3, y3), (x2, y2), x)
    else:
        return 0


#
def up_pa(x):
    (x1, y1), (x2, y2), (x3, y3) = (60, 0), (90, 1), (120, 0)
    if x1 <= x <= x2:
        return lineEquation((x1, y1), (x2, y2), x)
    elif x2 <= x <= x3:
        return lineEquation((x3, y3), (x2, y2), x)
    else:
        return 0


def up_left_pa(x):
    (x1, y1), (x2, y2), (x3, y3) = (90, 0), (120, 1), (150, 0)
    if x1 <= x <= x2:
        return lineEquation((x1, y1), (x2, y2), x)
    elif x2 <= x <= x3:
        return lineEquation((x3, y3), (x2, y2), x)
    else:
        return 0


def up_more_left_pa(x):
    (x1, y1), (x2, y2), (x3, y3) = (120, 0), (150, 1), (180, 0)
    if x1 <= x <= x2:
        return lineEquation((x1, y1), (x2, y2), x)
    elif x2 <= x <= x3:
        return lineEquation((x3, y3), (x2, y2), x)
    else:
        return 0


def down_more_left_pa(x):
    (x1, y1), (x2, y2), (x3, y3) = (180, 0), (210, 1), (240, 0)
    if x1 <= x <= x2:
        return lineEquation((x1, y1), (x2, y2), x)
    elif x2 <= x <= x3:
        return lineEquation((x3, y3), (x2, y2), x)
    else:
        return 0


def down_left_pa(x):
    (x1, y1), (x2, y2), (x3, y3) = (210, 0), (240, 1), (270, 0)
    if x1 <= x <= x2:
        return lineEquation((x1, y1), (x2, y2), x)
    elif x2 <= x <= x3:
        return lineEquation((x3, y3), (x2, y2), x)
    else:
        return 0


def down_pa(x):
    (x1, y1), (x2, y2), (x3, y3) = (240, 0), (270, 1), (300, 0)
    if x1 <= x <= x2:
        return lineEquation((x1, y1), (x2, y2), x)
    elif x2 <= x <= x3:
        return lineEquation((x3, y3), (x2, y2), x)
    else:
        return 0


def down_right_pa(x):
    (x1, y1), (x2, y2), (x3, y3) = (270, 0), (300, 1), (330, 0)
    if x1 <= x <= x2:
        return lineEquation((x1, y1), (x2, y2), x)
    elif x2 <= x <= x3:
        return lineEquation((x3, y3), (x2, y2), x)
    else:
        return 0


def down_more_right_pa(x):
    (x1, y1), (x2, y2), (x3, y3) = (300, 0), (330, 1), (360, 0)
    if x1 <= x <= x2:
        return lineEquation((x1, y1), (x2, y2), x)
    elif x2 <= x <= x3:
        return lineEquation((x3, y3), (x2, y2), x)
    else:
        return 0


# pv
def cw_fast_pv(x):
    (x1, y1), (x2, y2), (x3, y3) = (-200, 0), (-200, 1), (-100, 0)
    if x1 <= x <= x2:
        return lineEquation((x1, y1), (x2, y2), x)
    elif x2 <= x <= x3:
        return lineEquation((x3, y3), (x2, y2), x)
    else:
        return 0


def cw_slow_pv(x):
    (x1, y1), (x2, y2), (x3, y3) = (-200, 0), (-100, 1), (0, 0)
    if x1 <= x <= x2:
        return lineEquation((x1, y1), (x2, y2), x)
    elif x2 <= x <= x3:
        return lineEquation((x3, y3), (x2, y2), x)
    else:
        return 0


def stop_pv(x):
    (x1, y1), (x2, y2), (x3, y3) = (-100, 0), (0, 1), (100, 0)
    if x1 <= x <= x2:
        return lineEquation((x1, y1), (x2, y2), x)
    elif x2 <= x <= x3:
        return lineEquation((x3, y3), (x2, y2), x)
    else:
        return 0


def ccw_slow_pv(x):
    (x1, y1), (x2, y2), (x3, y3) = (0, 0), (100, 1), (200, 0)
    if x1 <= x <= x2:
        return lineEquation((x1, y1), (x2, y2), x)
    elif x2 <= x <= x3:
        return lineEquation((x3, y3), (x2, y2), x)
    else:
        return 0


def ccw_fast_pv(x):
    (x1, y1), (x2, y2), (x3, y3) = (100, 0), (200, 1), (200, 0)
    if x1 <= x <= x2:
        return lineEquation((x1, y1), (x2, y2), x)
    elif x2 <= x <= x3:
        return lineEquation((x3, y3), (x2, y2), x)
    else:
        return 0


def left_fast_force(x, limit):
    (x1, y1), (x2, y2), (x3, y3) = (-100, 0), (-80, 1), (-60, 0)
    if x1 <= x <= x2:
        y = lineEquation((x1, y1), (x2, y2), x)
    elif x2 <= x <= x3:
        y = lineEquation((x3, y3), (x2, y2), x)
    else:
        y = 0
    if limit < y:
        return limit
    else:
        return y


def left_slow_force(x, limit):
    (x1, y1), (x2, y2), (x3, y3) = (-80, 0), (-60, 1), (0, 0)
    if x1 <= x <= x2:
        y = lineEquation((x1, y1), (x2, y2), x)
    elif x2 <= x <= x3:
        y = lineEquation((x3, y3), (x2, y2), x)
    else:
        y = 0
    if limit < y:
        return limit
    else:
        return y


def stop_force(x, limit):
    (x1, y1), (x2, y2), (x3, y3) = (-60, 0), (0, 1), (60, 0)
    if x1 <= x <= x2:
        y = lineEquation((x1, y1), (x2, y2), x)
    elif x2 <= x <= x3:
        y = lineEquation((x3, y3), (x2, y2), x)
    else:
        y = 0
    if limit < y:
        return limit
    else:
        return y


def right_slow_force(x, limit):
    (x1, y1), (x2, y2), (x3, y3) = (0, 0), (60, 1), (80, 0)
    if x1 <= x <= x2:
        y = lineEquation((x1, y1), (x2, y2), x)
    elif x2 <= x <= x3:
        y = lineEquation((x3, y3), (x2, y2), x)
    else:
        y = 0
    if limit < y:
        return limit
    else:
        return y


def right_fast_force(x, limit):
    (x1, y1), (x2, y2), (x3, y3) = (60, 0), (80, 1), (100, 0)
    if x1 <= x <= x2:
        y = lineEquation((x1, y1), (x2, y2), x)
    elif x2 <= x <= x3:
        y = lineEquation((x3, y3), (x2, y2), x)
    else:
        y = 0
    if limit < y:
        return limit
    else:
        return y





class System:
    def __init__(self):
        pv_set = 0


class FuzzyController2:

    def __init__(self, fcl_path):
        # self.system = Reader().load_from_file(fcl_path)
        self.system = System()

    def _make_input(self, world):
        return dict(
            cp=world.x,
            cv=world.v,
            pa=degrees(world.theta),
            pv=degrees(world.omega)
        )

    def _make_output(self):
        return dict(
            force=0.
        )

    def decide(self, world):
        output = self._make_output()
        print(output)
        self.system.calculate(self._make_input(world), output)
        print("lllllllll")
        print(output)
        return output['force']
