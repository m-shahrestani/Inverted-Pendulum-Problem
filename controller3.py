# -*- coding: utf-8 -*-

# python imports
from math import degrees

import numpy as np


class FuzzyController3:

    def __init__(self):
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
        self.system.calculate(self._make_input(world), output)
        return output['force']


class System:

    def __init__(self):
        pass

    def lineEquation(self, (x1, y1), (x2, y2), x):
        if x2 - x1 == 0:
            y = max(y1, y2) * 1.0
        else:
            m = (y2 - y1) / ((x2 - x1) * 1.0)
            b = -1 * m * x1 + y1
            y = m * x + b
        return y

    # Fuzzification
    # pa
    def up_more_right_pa(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (0, 0), (30, 1), (60, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    def up_right_pa(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (30, 0), (60, 1), (90, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    def up_pa(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (60, 0), (90, 1), (120, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    def up_left_pa(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (90, 0), (120, 1), (150, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    def up_more_left_pa(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (120, 0), (150, 1), (180, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    def down_more_left_pa(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (180, 0), (210, 1), (240, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    def down_left_pa(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (210, 0), (240, 1), (270, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    def down_pa(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (240, 0), (270, 1), (300, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    def down_right_pa(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (270, 0), (300, 1), (330, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    def down_more_right_pa(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (300, 0), (330, 1), (360, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    # pv
    def cw_fast_pv(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (-200, 0), (-200, 1), (-100, 0)
        if x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    def cw_slow_pv(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (-200, 0), (-100, 1), (0, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    def stop_pv(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (-100, 0), (0, 1), (100, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    def ccw_slow_pv(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (0, 0), (100, 1), (200, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    def ccw_fast_pv(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (100, 0), (200, 1), (200, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    # cp
    def left_far_cp(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (-10, 0), (-10, 1), (-5, 0)
        if x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    def left_near_cp(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (-10, 0), (-2.5, 1), (0, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    def stop_cp(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (-2.5, 0), (0, 1), (2.5, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    def right_near_cp(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (0, 0), (2.5, 1), (10, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    def right_far_cp(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (5, 0), (10, 1), (10, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    # cv
    def left_fast_cv(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (-5, 0), (-5, 1), (-2.5, 0)
        if x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    def left_slow_cv(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (-5, 0), (-1, 1), (0, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    def stop_cv(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (-1, 0), (0, 1), (1, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    def right_slow_cv(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (0, 0), (1, 1), (5, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    def right_fast_cv(self, x):
        (x1, y1), (x2, y2), (x3, y3) = (2.5, 0), (5, 1), (5, 0)
        if x1 <= x <= x2:
            return self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x:
            return self.lineEquation((x3, y3), (x2, y2), x)
        else:
            return 0

    # force
    def left_fast_force(self, x, limit):
        (x1, y1), (x2, y2), (x3, y3) = (-100, 0), (-80, 1), (-60, 0)
        if x1 <= x <= x2:
            y = self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            y = self.lineEquation((x3, y3), (x2, y2), x)
        else:
            y = 0
        if limit < y:
            return limit * 1.0
        else:
            return y * 1.0

    def left_slow_force(self, x, limit):
        (x1, y1), (x2, y2), (x3, y3) = (-80, 0), (-60, 1), (0, 0)
        if x1 <= x <= x2:
            y = self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            y = self.lineEquation((x3, y3), (x2, y2), x)
        else:
            y = 0
        if limit < y:
            return limit * 1.0
        else:
            return y * 1.0

    def stop_force(self, x, limit):
        (x1, y1), (x2, y2), (x3, y3) = (-60, 0), (0, 1), (60, 0)
        if x1 <= x <= x2:
            y = self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            y = self.lineEquation((x3, y3), (x2, y2), x)
        else:
            y = 0
        if limit < y:
            return limit * 1.0
        else:
            return y * 1.0

    def right_slow_force(self, x, limit):
        (x1, y1), (x2, y2), (x3, y3) = (0, 0), (60, 1), (80, 0)
        if x1 <= x <= x2:
            y = self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            y = self.lineEquation((x3, y3), (x2, y2), x)
        else:
            y = 0
        if limit < y:
            return limit * 1.0
        else:
            return y * 1.0

    def right_fast_force(self, x, limit):
        (x1, y1), (x2, y2), (x3, y3) = (60, 0), (80, 1), (100, 0)
        if x1 <= x <= x2:
            y = self.lineEquation((x1, y1), (x2, y2), x)
        elif x2 <= x <= x3:
            y = self.lineEquation((x3, y3), (x2, y2), x)
        else:
            y = 0
        if limit < y:
            return limit * 1.0
        else:
            return y * 1.0

    # Inference
    def max_membership(self, membership, x1, x2, key):
        newVal = min(x1, x2)
        if key in membership:
            membership[key] = max(membership[key], newVal)
        else:
            membership[key] = newVal

    def rules(self, pa, pv, cp, cv):
        membership = dict()
        membership['stop'] = max(min((self.up_pa(pa), self.stop_pv(pv))),
                                 min((self.up_right_pa(pa), self.ccw_slow_pv(pv))),
                                 min((self.up_left_pa(pa), self.cw_slow_pv(pv))))
        self.max_membership(membership, self.up_more_right_pa(pa), self.ccw_slow_pv(pv), 'right_fast')
        self.max_membership(membership, self.up_more_right_pa(pa), self.cw_slow_pv(pv), 'right_fast')
        self.max_membership(membership, self.up_more_left_pa(pa), self.cw_slow_pv(pv), 'left_fast')
        self.max_membership(membership, self.up_more_left_pa(pa), self.ccw_slow_pv(pv), 'left_fast')
        self.max_membership(membership, self.up_more_right_pa(pa), self.ccw_fast_pv(pv), 'left_slow')
        self.max_membership(membership, self.up_more_right_pa(pa), self.cw_fast_pv(pv), 'right_fast')
        self.max_membership(membership, self.up_more_left_pa(pa), self.cw_fast_pv(pv), 'right_slow')
        self.max_membership(membership, self.up_more_left_pa(pa), self.ccw_fast_pv(pv), 'left_fast')
        self.max_membership(membership, self.down_more_right_pa(pa), self.ccw_slow_pv(pv), 'right_fast')
        self.max_membership(membership, self.down_more_right_pa(pa), self.cw_slow_pv(pv), 'stop')
        self.max_membership(membership, self.down_more_left_pa(pa), self.cw_slow_pv(pv), 'left_fast')
        self.max_membership(membership, self.down_more_left_pa(pa), self.ccw_slow_pv(pv), 'stop')
        self.max_membership(membership, self.down_more_right_pa(pa), self.ccw_fast_pv(pv), 'stop')
        self.max_membership(membership, self.down_more_right_pa(pa), self.cw_fast_pv(pv), 'stop')
        self.max_membership(membership, self.down_more_left_pa(pa), self.cw_fast_pv(pv), 'stop')
        self.max_membership(membership, self.down_more_left_pa(pa), self.ccw_fast_pv(pv), 'stop')
        self.max_membership(membership, self.down_right_pa(pa), self.ccw_slow_pv(pv), 'right_fast')
        self.max_membership(membership, self.down_right_pa(pa), self.cw_slow_pv(pv), 'right_fast')
        self.max_membership(membership, self.down_left_pa(pa), self.cw_slow_pv(pv), 'left_fast')
        self.max_membership(membership, self.down_left_pa(pa), self.ccw_slow_pv(pv), 'left_fast')
        self.max_membership(membership, self.down_right_pa(pa), self.ccw_fast_pv(pv), 'stop')
        self.max_membership(membership, self.down_right_pa(pa), self.cw_fast_pv(pv), 'right_slow')
        self.max_membership(membership, self.down_left_pa(pa), self.cw_fast_pv(pv), 'stop')
        self.max_membership(membership, self.down_left_pa(pa), self.ccw_fast_pv(pv), 'left_slow')
        self.max_membership(membership, self.up_right_pa(pa), self.ccw_slow_pv(pv), 'right_slow')
        self.max_membership(membership, self.up_right_pa(pa), self.cw_slow_pv(pv), 'right_fast')
        self.max_membership(membership, self.up_right_pa(pa), self.stop_pv(pv), 'right_fast')
        self.max_membership(membership, self.up_left_pa(pa), self.cw_slow_pv(pv), 'left_slow')
        self.max_membership(membership, self.up_left_pa(pa), self.ccw_slow_pv(pv), 'left_fast')
        self.max_membership(membership, self.up_left_pa(pa), self.stop_pv(pv), 'left_fast')
        self.max_membership(membership, self.up_right_pa(pa), self.ccw_fast_pv(pv), 'left_fast')
        self.max_membership(membership, self.up_right_pa(pa), self.cw_fast_pv(pv), 'right_fast')
        self.max_membership(membership, self.up_left_pa(pa), self.cw_fast_pv(pv), 'right_fast')
        self.max_membership(membership, self.up_left_pa(pa), self.ccw_fast_pv(pv), 'left_fast')
        self.max_membership(membership, self.down_pa(pa), self.stop_pv(pv), 'right_fast')
        self.max_membership(membership, self.down_pa(pa), self.cw_fast_pv(pv), 'stop')
        self.max_membership(membership, self.down_pa(pa), self.ccw_fast_pv(pv), 'stop')
        self.max_membership(membership, self.up_pa(pa), self.ccw_slow_pv(pv), 'left_slow')
        self.max_membership(membership, self.up_pa(pa), self.ccw_fast_pv(pv), 'left_fast')
        self.max_membership(membership, self.up_pa(pa), self.cw_slow_pv(pv), 'right_slow')
        self.max_membership(membership, self.up_pa(pa), self.cw_fast_pv(pv), 'right_fast')
        self.max_membership(membership, self.up_pa(pa), self.stop_pv(pv), 'stop')
        return membership

    # Defuzzification
    def COM(self, x, y):
        centroid = 0
        integral = 0
        for i in enumerate(x):
            centroid += y[i[0]] * x[i[0]]
            integral += y[i[0]]
        if integral == 0:
            return 0.0
        return centroid / (integral * 1.0)

    def calculate(self, inputs, output):
        if inputs['pa'] < 0:
            inputs['pa'] = inputs['pa'] * -1
        print inputs
        membership = self.rules(inputs['pa'], inputs['pv'], inputs['cp'], inputs['cv'])
        x = np.arange(-100, 100, 0.1)
        y = np.zeros(len(x))
        for i in enumerate(x):
            y[i[0]] = max(self.left_fast_force(i[1], membership['left_fast']),
                          self.left_slow_force(i[1], membership['left_slow']),
                          self.right_fast_force(i[1], membership['right_fast']),
                          self.right_slow_force(i[1], membership['right_slow']),
                          self.stop_force(i[1], membership['stop']))
        output['force'] = self.COM(x, y)
