# -*- coding: utf-8 -*-

# python imports
from copy import deepcopy
from math import degrees

import numpy as np
from fuzzy.storage.fcl.Reader import Reader


class FuzzyController2:
    def __init__(self, fcl_path):
        self.system = Reader().load_from_file(fcl_path)

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
        # output = self._make_output()
        # self.calculate(self._make_input(world), output)
        # return output['force']
        inputs = self._make_input(world)
        fuzzy_outputs = deepcopy(self.rules(inputs['pa'], inputs['pv']))

        for key, value in fuzzy_outputs.items():
            fuzzy_outputs[key] = max(list(value))

        print(fuzzy_outputs)
        x_axis = np.arange(-110, 110, 0.1)
        left_fast_force_points = []
        left_slow_points = []
        right_fast_points = []
        right_slow_points = []
        stop_points = []

        for x in x_axis:
            left_fast_force_points.append(self.left_fast_force(x, fuzzy_outputs['left_fast']))
            left_slow_points.append(self.left_slow_force(x, fuzzy_outputs['left_slow']))
            right_fast_points.append(self.right_fast_force(x, fuzzy_outputs['right_fast']))
            right_slow_points.append(self.right_slow_force(x, fuzzy_outputs['right_slow']))
            stop_points.append(self.stop_force(x, fuzzy_outputs['stop']))
        sum = 0
        sum_makhraj = 0

        for i in range(len(x_axis)):
            sum += max(left_fast_force_points[i], left_slow_points[i], right_fast_points[i], right_slow_points[i],
                       stop_points[i]) * x_axis[i]
            sum_makhraj += max(left_fast_force_points[i], left_slow_points[i], right_fast_points[i],
                               right_slow_points[i], stop_points[i])
        if sum_makhraj != 0:
            return sum / (sum_makhraj * 1.0)
        else:
            return 0.0



    def lineEquation(self, (x1, y1), (x2, y2), x):
        if x2 - x1 == 0:
            y = max(y1, y2) * 1.0
        else:
            m = (y2 - y1) / ((x2 - x1) * 1.0)
            b = -1 * m * x1 + y1
            y = m * x + b
        return y

    def up_more_right_pa1(self, x):
        if 0 <= x <= 30:
            return x / (30.0 * 1.0)
        elif 30 < x <= 60:
            return -(x - 60) / (30.0 * 1.0)
        else:
            return 0

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
        if x1 <= x <= x2:
            return 1.0
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
        elif x2 <= x <= x3:
            return 1.0
        else:
            return 0

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

    # def max_membership(self, x1, x2, key):
    # newVal = min(x1, x2)
    # if key in membership:
    #     membership[key] = max(membership[key], newVal)
    # else:
    #     membership[key] = newVal

    def max_membership(self, x1, x2, membership, key):
        membership[key].add(min(x1, x2))

    def rules(self, pa, pv):
        membership = {'left_fast': set(), 'left_slow': set(), 'stop': set(), 'right_slow': set(),
                      'right_fast': set()}

        membership['stop'].add(max(min((self.up_pa(pa), self.stop_pv(pv))),
                                   min((self.up_right_pa(pa), self.ccw_slow_pv(pv))),
                                   min((self.up_left_pa(pa), self.cw_slow_pv(pv)))))

        self.max_membership(self.up_more_right_pa(pa), self.ccw_slow_pv(pv), membership, 'right_fast')
        self.max_membership(self.up_more_right_pa(pa), self.cw_slow_pv(pv), membership, 'right_fast')
        self.max_membership(self.up_more_left_pa(pa), self.cw_slow_pv(pv), membership, 'left_fast')
        self.max_membership(self.up_more_left_pa(pa), self.ccw_slow_pv(pv), membership, 'left_fast')
        self.max_membership(self.up_more_right_pa(pa), self.ccw_fast_pv(pv), membership, 'left_slow')

        self.max_membership(self.up_more_right_pa(pa), self.cw_fast_pv(pv), membership, 'right_fast')
        self.max_membership(self.up_more_left_pa(pa), self.cw_fast_pv(pv), membership, 'right_slow')
        self.max_membership(self.up_more_left_pa(pa), self.ccw_fast_pv(pv), membership, 'left_fast')
        self.max_membership(self.down_more_right_pa(pa), self.ccw_slow_pv(pv), membership, 'right_fast')
        self.max_membership(self.down_more_right_pa(pa), self.cw_slow_pv(pv), membership, 'stop')

        self.max_membership(self.down_more_left_pa(pa), self.cw_slow_pv(pv), membership, 'left_fast')
        self.max_membership(self.down_more_left_pa(pa), self.ccw_slow_pv(pv), membership, 'stop')
        self.max_membership(self.down_more_right_pa(pa), self.ccw_fast_pv(pv), membership, 'stop')
        self.max_membership(self.down_more_right_pa(pa), self.cw_fast_pv(pv), membership, 'stop')
        self.max_membership(self.down_more_left_pa(pa), self.cw_fast_pv(pv), membership, 'stop')

        self.max_membership(self.down_more_left_pa(pa), self.ccw_fast_pv(pv), membership, 'stop')
        self.max_membership(self.down_right_pa(pa), self.ccw_slow_pv(pv), membership, 'right_fast')
        self.max_membership(self.down_right_pa(pa), self.cw_slow_pv(pv), membership, 'right_fast')
        self.max_membership(self.down_left_pa(pa), self.cw_slow_pv(pv), membership, 'left_fast')
        self.max_membership(self.down_left_pa(pa), self.ccw_slow_pv(pv), membership, 'left_fast')

        self.max_membership(self.down_right_pa(pa), self.ccw_fast_pv(pv), membership, 'stop')
        self.max_membership(self.down_right_pa(pa), self.cw_fast_pv(pv), membership, 'right_slow')
        self.max_membership(self.down_left_pa(pa), self.cw_fast_pv(pv), membership, 'stop')
        self.max_membership(self.down_left_pa(pa), self.ccw_fast_pv(pv), membership, 'left_slow')
        self.max_membership(self.up_right_pa(pa), self.ccw_slow_pv(pv), membership, 'right_slow')

        self.max_membership(self.up_right_pa(pa), self.cw_slow_pv(pv), membership, 'right_fast')
        self.max_membership(self.up_right_pa(pa), self.stop_pv(pv), membership, 'right_fast')
        self.max_membership(self.up_left_pa(pa), self.cw_slow_pv(pv), membership, 'left_slow')
        self.max_membership(self.up_left_pa(pa), self.ccw_slow_pv(pv), membership, 'left_fast')
        self.max_membership(self.up_left_pa(pa), self.stop_pv(pv), membership, 'left_fast')

        self.max_membership(self.up_right_pa(pa), self.ccw_fast_pv(pv), membership, 'left_fast')
        self.max_membership(self.up_right_pa(pa), self.cw_fast_pv(pv), membership, 'right_fast')
        self.max_membership(self.up_left_pa(pa), self.cw_fast_pv(pv), membership, 'right_fast')
        self.max_membership(self.up_left_pa(pa), self.ccw_fast_pv(pv), membership, 'left_fast')
        self.max_membership(self.down_pa(pa), self.stop_pv(pv), membership, 'right_fast')

        self.max_membership(self.down_pa(pa), self.cw_fast_pv(pv), membership, 'stop')
        self.max_membership(self.down_pa(pa), self.ccw_fast_pv(pv), membership, 'stop')
        self.max_membership(self.up_pa(pa), self.ccw_slow_pv(pv), membership, 'left_slow')
        self.max_membership(self.up_pa(pa), self.ccw_fast_pv(pv), membership, 'left_fast')
        self.max_membership(self.up_pa(pa), self.cw_slow_pv(pv), membership, 'right_slow')

        self.max_membership(self.up_pa(pa), self.cw_fast_pv(pv), membership, 'right_fast')
        self.max_membership(self.up_pa(pa), self.stop_pv(pv), membership, 'stop')

        print(min((self.up_pa(pa), self.stop_pv(pv))),
                                   min((self.up_right_pa(pa), self.ccw_slow_pv(pv))),
                                   min((self.up_left_pa(pa), self.cw_slow_pv(pv))), 'stop')
        print(self.up_more_right_pa(pa), self.ccw_slow_pv(pv), 'right_fast')
        print(self.up_more_right_pa(pa), self.cw_slow_pv(pv), 'right_fast')
        print(self.up_more_left_pa(pa), self.cw_slow_pv(pv), 'left_fast')
        print(self.up_more_left_pa(pa), self.ccw_slow_pv(pv), 'left_fast')
        print(self.up_more_right_pa(pa), self.ccw_fast_pv(pv), 'left_slow')

        print(self.up_more_right_pa(pa), self.cw_fast_pv(pv), 'right_fast')
        print(self.up_more_left_pa(pa), self.cw_fast_pv(pv), 'right_slow')
        print(self.up_more_left_pa(pa), self.ccw_fast_pv(pv), 'left_fast')
        print(self.down_more_right_pa(pa), self.ccw_slow_pv(pv), 'right_fast')
        print(self.down_more_right_pa(pa), self.cw_slow_pv(pv), 'stop')

        print(self.down_more_left_pa(pa), self.cw_slow_pv(pv), 'left_fast')
        print(self.down_more_left_pa(pa), self.ccw_slow_pv(pv), 'stop')
        print(self.down_more_right_pa(pa), self.ccw_fast_pv(pv), 'stop')
        print(self.down_more_right_pa(pa), self.cw_fast_pv(pv), 'stop')
        print(self.down_more_left_pa(pa), self.cw_fast_pv(pv), 'stop')

        print(self.down_more_left_pa(pa), self.ccw_fast_pv(pv), 'stop')
        print(self.down_right_pa(pa), self.ccw_slow_pv(pv), 'right_fast')
        print(self.down_right_pa(pa), self.cw_slow_pv(pv), 'right_fast')
        print(self.down_left_pa(pa), self.cw_slow_pv(pv), 'left_fast')
        print(self.down_left_pa(pa), self.ccw_slow_pv(pv), 'left_fast')

        print(self.down_right_pa(pa), self.ccw_fast_pv(pv), 'stop')
        print(self.down_right_pa(pa), self.cw_fast_pv(pv), 'right_slow')
        print(self.down_left_pa(pa), self.cw_fast_pv(pv), 'stop')
        print(self.down_left_pa(pa), self.ccw_fast_pv(pv), 'left_slow')
        print(self.up_right_pa(pa), self.ccw_slow_pv(pv), 'right_slow')

        print(self.up_right_pa(pa), self.cw_slow_pv(pv), 'right_fast')
        print(self.up_right_pa(pa), self.stop_pv(pv), 'right_fast')
        print(self.up_left_pa(pa), self.cw_slow_pv(pv), 'left_slow')
        print(self.up_left_pa(pa), self.ccw_slow_pv(pv), 'left_fast')
        print(self.up_left_pa(pa), self.stop_pv(pv), 'left_fast')

        print(self.up_right_pa(pa), self.ccw_fast_pv(pv), 'left_fast')
        print(self.up_right_pa(pa), self.cw_fast_pv(pv), 'right_fast')
        print(self.up_left_pa(pa), self.cw_fast_pv(pv), 'right_fast')
        print(self.up_left_pa(pa), self.ccw_fast_pv(pv), 'left_fast')
        print(self.down_pa(pa), self.stop_pv(pv), 'right_fast')

        print(self.down_pa(pa), self.cw_fast_pv(pv), 'stop')
        print(self.down_pa(pa), self.ccw_fast_pv(pv), 'stop')
        print(self.up_pa(pa), self.ccw_slow_pv(pv), 'left_slow')
        print(self.up_pa(pa), self.ccw_fast_pv(pv), 'left_fast')
        print(self.up_pa(pa), self.cw_slow_pv(pv), 'right_slow')

        print(self.up_pa(pa), self.cw_fast_pv(pv), 'right_fast')
        print(self.up_pa(pa), self.stop_pv(pv), 'stop')
        return membership

    # def calculate(self, world, output):
    #     self.rules(world['pa'], world['cp'])
    #     x = np.arange(-100, 100, 0.1)
    #     y = np.zeros(len(x))
    #     for i in enumerate(x):
    #         # print(self.left_fast_force(i, membership['left_slow']),
    #         #       self.left_slow_force(i, membership['right_fast']),
    #         #       self.right_fast_force(i, membership['right_slow']),
    #         #       self.right_slow_force(i, membership['stop']),
    #         #       self.stop_force(i, membership['left_fast']))
    #         y[i[0]] = max(self.left_fast_force(i[1], membership['left_slow']),
    #                    self.left_slow_force(i[1], membership['right_fast']),
    #                    self.right_fast_force(i[1], membership['right_slow']),
    #                    self.right_slow_force(i[1], membership['stop']),
    #                    self.stop_force(i[1], membership['left_fast']))
    #     output['force'] = self.COM(x, y)
    #
    # def COM(self, x, y):
    #     centroid = 0
    #     s = 0
    #     for i in enumerate(x):
    #         centroid += y[i[0]] * x[i[0]]
    #         s += y[i[0]]
    #     print centroid
    #     print s
    #     print centroid / (s * 1.0)
    #     if s == 0:
    #         return 0.0
    #     return centroid / (s * 1.0)
