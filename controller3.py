# -*- coding: utf-8 -*-

# python imports
from __future__ import division

from math import degrees

# pyfuzzy imports
import numpy as np

from fuzzy.storage.fcl.Reader import Reader


class FuzzyController3:

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

    # def decide(self, world):
    #      output = self._make_output()
    #      self.system.calculate(self._make_input(world), output)
    #      return output['force']

    def up_more_right_pa(self, x):
        if x >= 0 and x <= 30:
            return x / (30.0 * 1.0)
        elif x > 30 and x <= 60:
            return -(x - 60) / (30.0 * 1.0)
        else:
            return 0

    def up_right_pa(self, x):
        if x >= 30 and x <= 60:
            return (x - 30) / (30.0 * 1.0)
        elif x > 60 and x <= 90:
            return -(x - 90) / (30.0 * 1.0)
        else:
            return 0

    def up_pa(self, x):
        if x >= 60 and x <= 90:
            return (x - 60) / (30.0 * 1.0)
        elif x > 90 and x <= 120:
            return -(x - 120) / (30.0 * 1.0)
        else:
            return 0

    def up_left_pa(self, x):
        if x >= 90 and x <= 120:
            return (x - 90) / (30.0 * 1.0)
        elif x > 120 and x <= 150:
            return -(x - 150) / (30.0 * 1.0)
        else:
            return 0

    def up_more_left_pa(self, x):
        if x >= 120 and x <= 150:
            return (x - 120) / (30.0 * 1.0)
        elif x > 150 and x <= 180:
            return -(x - 180) / (30.0 * 1.0)
        else:
            return 0

    def down_more_left_pa(self, x):
        if x >= 180 and x <= 210:
            return (x - 180) / (30.0 * 1.0)
        elif x > 210 and x <= 240:
            return -(x - 240) / (30.0 * 1.0)
        else:
            return 0

    def down_left_pa(self, x):
        if x >= 210 and x <= 240:
            return (x - 210) / (30.0 * 1.0)
        elif x > 240 and x <= 270:
            return -(x - 270) / (30.0 * 1.0)
        else:
            return 0

    def down_pa(self, x):
        if x >= 240 and x <= 270:
            return (x - 240) / (30.0 * 1.0)
        elif x > 270 and x <= 300:
            return -(x - 300) / (30.0 * 1.0)
        else:
            return 0

    def down_right_pa(self, x):
        if x >= 270 and x <= 300:
            return (x - 270) / (30.0 * 1.0)
        elif x > 300 and x <= 330:
            return -(x - 330) / (30.0 * 1.0)
        else:
            return 0

    def down_more_right_pa(self, x):
        if x >= 300 and x <= 330:
            return (x - 300) / (30.0 * 1.0)
        elif x > 330 and x <= 360:
            return -(x - 360) / (30.0 * 1.0)
        else:
            return 0

    def cw_fast(self, x):
        if x == -200:
            return 1
        elif x <= -100 and x > -200:
            return -(x + 100) / (100.0 * 1.0)
        else:
            return 0

    def cw_slow(self, x):
        if x >= -200 and x <= -100:
            return (x + 200) / (100.0 * 1.0)
        elif x > -100 and x <= 0:
            return -(x) / (100.0 * 1.0)
        else:
            return 0

    def stop(self, x):
        if x >= -100 and x <= 0:
            return (x + 100) / (100.0 * 1.0)
        elif x > 0 and x <= 100:
            return -(x - 100) / (100.0 * 1.0)
        else:
            return 0

    def ccw_slow(self, x):
        if x >= 0 and x <= 100:
            return (x) / (100.0 * 1.0)
        elif x > 100 and x <= 200:
            return -(x - 200) / (100.0 * 1.0)
        else:
            return 0

    def ccw_fast(self, x):
        if x == 200:
            return 1.0
        elif x >= 100 and x < 200:
            return (x - 200) / (100.0 * 1.0)
        else:
            return 0.0

    def left_fast_force(self, x, ceil):

        if x >= -100 and x <= -80:
            out = (x + 100) / (20.0 * 1.0)
        elif x > -80 and x <= -60:
            out = -(x + 60) / (20.0 * 1.0)
        else:
            out = 0 * 1.0
        if out < ceil:
            return out * 1.0
        else:
            return ceil * 1.0

    def left_slow_force(self, x, ceil):
        if x >= -80 and x <= -60:
            out = (x + 80) / (20.0 * 1.0)
        elif x > -60 and x <= 0:
            out = -(x) / (60.0 * 1.0)
        else:
            out = 0 * 1.0
        if out < ceil:
            return out * 1.0
        else:
            return ceil * 1.0

    def stop_force(self, x, ceil):
        if x >= -60 and x <= 0:
            out = (x + 60) / (60.0 * 1.0)
        elif x > 0 and x <= 60:
            out = -(x - 60) / (60.0 * 1.0)
        else:
            out = 0 * 1.0

        if out < ceil:
            return out * 1.0
        else:
            return ceil * 1.0

    def right_slow_force(self, x, ceil):
        if x >= 0 and x <= 60:
            out = x / (60.0 * 1.0)
        elif x > 60 and x <= 80:
            out = -(x - 80) / (20.0 * 1.0)
        else:
            out = 0 * 1.0
        if out < ceil:
            return out * 1.0
        else:
            return ceil * 1.0

    def right_fast_force(self, x, ceil):
        if x >= 60 and x <= 80:
            out = (x - 60) / (20.0 * 1.0)
        elif x > 80 and x <= 100:
            out = -(x - 100) / (20.0 * 1.0)
        else:
            out = 0 * 1.0
        if out < ceil:
            return out * 1.0
        else:
            return ceil * 1.0

    def rules(self, pa, pv):

        force_fuzzy_memberships = {'left_fast': set(), 'left_slow': set(), 'stop': set(), 'right_slow': set(),
                                   'right_fast': set()}

        force_fuzzy_memberships['stop'].add(
            max(min(self.up_pa(pa), self.stop(pv)), min(self.up_right_pa(pa), self.ccw_slow(pv)),
                min(self.up_left_pa(pa), self.cw_slow(pv))))

        force_fuzzy_memberships['right_fast'].add(min(self.up_more_right_pa(pa), self.ccw_slow(pv)))
        force_fuzzy_memberships['right_fast'].add(min(self.up_more_right_pa(pa), self.cw_slow(pv)))

        force_fuzzy_memberships['left_fast'].add(min(self.up_more_left_pa(pa), self.ccw_slow(pv)))
        force_fuzzy_memberships['left_fast'].add(min(self.up_more_left_pa(pa), self.cw_slow(pv)))

        force_fuzzy_memberships['left_slow'].add(min(self.up_more_right_pa(pa), self.ccw_fast(pv)))
        force_fuzzy_memberships['right_fast'].add(min(self.up_more_right_pa(pa), self.cw_fast(pv)))

        force_fuzzy_memberships['right_slow'].add(min(self.up_more_left_pa(pa), self.cw_fast(pv)))
        force_fuzzy_memberships['left_fast'].add(min(self.up_more_left_pa(pa), self.ccw_fast(pv)))

        force_fuzzy_memberships['right_fast'].add(min(self.down_more_right_pa(pa), self.ccw_slow(pv)))
        force_fuzzy_memberships['stop'].add(min(self.down_right_pa(pa), self.cw_slow(pv)))

        force_fuzzy_memberships['left_fast'].add(min(self.down_more_left_pa(pa), self.cw_fast(pv)))
        force_fuzzy_memberships['stop'].add(min(self.down_more_left_pa(pa), self.ccw_fast(pv)))

        # RULE 13: IF (pa IS down_more_right) AND (pv IS ccw_fast) THEN force IS stop;
        # RULE 14: IF (pa IS down_more_right) AND (pv IS cw_fast) THEN force IS stop;
        force_fuzzy_memberships['stop'].add(min(self.down_more_right_pa(pa), self.ccw_fast(pv)))
        force_fuzzy_memberships['stop'].add(min(self.down_more_right_pa(pa), self.cw_fast(pv)))

        # RULE 15: IF (pa IS down_more_left) AND (pv IS cw_fast) THEN force IS stop;
        # RULE 16: IF (pa IS down_more_left) AND (pv IS ccw_fast) THEN force IS stop;
        force_fuzzy_memberships['stop'].add(min(self.down_more_left_pa(pa), self.cw_fast(pv)))
        force_fuzzy_memberships['stop'].add(min(self.down_more_left_pa(pa), self.ccw_fast(pv)))

        # RULE 17: IF (pa IS down_right) AND (pv IS ccw_slow) THEN force IS right_fast;
        # RULE 18: IF (pa IS down_right) AND (pv IS cw_slow) THEN force IS right_fast;
        force_fuzzy_memberships['right_fast'].add(min(self.down_right_pa(pa), self.ccw_slow(pv)))
        force_fuzzy_memberships['right_fast'].add(min(self.down_right_pa(pa), self.cw_slow(pv)))

        # RULE 19: IF (pa IS down_left) AND (pv IS cw_slow) THEN force IS left_fast;
        # RULE 20: IF (pa IS down_left) AND (pv IS ccw_slow) THEN force IS left_fast;
        force_fuzzy_memberships['left_fast'].add(min(self.down_left_pa(pa), self.cw_slow(pv)))
        force_fuzzy_memberships['left_fast'].add(min(self.down_left_pa(pa), self.ccw_slow(pv)))

        # RULE 21: IF (pa IS down_right) AND (pv IS ccw_fast) THEN force IS stop;
        # RULE 22: IF (pa IS down_right) AND (pv IS cw_fast) THEN force IS right_slow;
        force_fuzzy_memberships['stop'].add(min(self.down_right_pa(pa), self.ccw_fast(pv)))
        force_fuzzy_memberships['right_slow'].add(min(self.down_right_pa(pa), self.cw_fast(pv)))

        # RULE 23: IF (pa IS down_left) AND (pv IS cw_fast) THEN force IS stop;
        # RULE 24: IF (pa IS down_left) AND (pv IS ccw_fast) THEN force IS left_slow;
        force_fuzzy_memberships['stop'].add(min(self.down_left_pa(pa), self.cw_fast(pv)))
        force_fuzzy_memberships['left_slow'].add(min(self.down_left_pa(pa), self.ccw_fast(pv)))

        # RULE 25: IF (pa IS up_right) AND (pv IS ccw_slow) THEN force IS right_slow;
        # RULE 26: IF (pa IS up_right) AND (pv IS cw_slow) THEN force IS right_fast;
        # RULE 27: IF (pa IS up_right) AND (pv IS stop) THEN force IS right_fast;
        # RULE 28: IF (pa IS up_left) AND (pv IS cw_slow) THEN force IS left_slow;
        # RULE 29: IF (pa IS up_left) AND (pv IS ccw_slow) THEN force IS left_fast;
        # RULE 30: IF (pa IS up_left) AND (pv IS stop) THEN force IS left_fast;
        force_fuzzy_memberships['right_slow'].add(min(self.up_right_pa(pa), self.ccw_slow(pv)))
        force_fuzzy_memberships['right_fast'].add(min(self.up_right_pa(pa), self.cw_slow(pv)))
        force_fuzzy_memberships['right_fast'].add(min(self.up_right_pa(pa), self.stop(pv)))
        force_fuzzy_memberships['left_slow'].add(min(self.up_left_pa(pa), self.cw_slow(pv)))
        force_fuzzy_memberships['left_fast'].add(min(self.up_left_pa(pa), self.ccw_slow(pv)))
        force_fuzzy_memberships['left_fast'].add(min(self.up_left_pa(pa), self.stop(pv)))

        # RULE 31: IF (pa IS up_right) AND (pv IS ccw_fast) THEN force IS left_fast;
        # RULE 32: IF (pa IS up_right) AND (pv IS cw_fast) THEN force IS right_fast;
        # RULE 33: IF (pa IS up_left) AND (pv IS cw_fast) THEN force IS right_fast;
        # RULE 34: IF (pa IS up_left) AND (pv IS ccw_fast) THEN force IS left_fast;
        force_fuzzy_memberships['left_fast'].add(min(self.up_right_pa(pa), self.ccw_fast(pv)))
        force_fuzzy_memberships['right_fast'].add(min(self.up_right_pa(pa), self.cw_fast(pv)))
        force_fuzzy_memberships['right_fast'].add(min(self.up_left_pa(pa), self.cw_fast(pv)))
        force_fuzzy_memberships['left_fast'].add(min(self.up_left_pa(pa), self.ccw_fast(pv)))

        # RULE 35: IF (pa IS down) AND (pv IS stop) THEN force IS right_fast;
        # RULE 36: IF (pa IS down) AND (pv IS cw_fast) THEN force IS stop;
        # RULE 37: IF (pa IS down) AND (pv IS ccw_fast) THEN force IS stop;
        force_fuzzy_memberships['right_fast'].add(min(self.down_pa(pa), self.stop(pv)))
        force_fuzzy_memberships['stop'].add(min(self.down_pa(pa), self.cw_fast(pv)))
        force_fuzzy_memberships['stop'].add(min(self.down_pa(pa), self.ccw_fast(pv)))

        # RULE 38: IF (pa IS up) AND (pv IS ccw_slow) THEN force IS left_slow;
        # RULE 39: IF (pa IS up) AND (pv IS ccw_fast) THEN force IS left_fast;
        # RULE 40: IF (pa IS up) AND (pv IS cw_slow) THEN force IS right_slow;
        # RULE 41: IF (pa IS up) AND (pv IS cw_fast) THEN force IS right_fast;
        # RULE 42: IF (pa IS up) AND (pv IS stop) THEN force IS stop;
        force_fuzzy_memberships['left_slow'].add(min(self.up_pa(pa), self.ccw_slow(pv)))
        force_fuzzy_memberships['left_fast'].add(min(self.up_pa(pa), self.ccw_fast(pv)))
        force_fuzzy_memberships['right_slow'].add(min(self.up_pa(pa), self.cw_slow(pv)))
        force_fuzzy_memberships['right_fast'].add(min(self.up_pa(pa), self.cw_fast(pv)))
        force_fuzzy_memberships['stop'].add(min(self.up_pa(pa), self.stop(pv)))

        print('stop', min(self.up_pa(pa), self.stop(pv)), min(self.up_right_pa(pa), self.ccw_slow(pv)),
                min(self.up_left_pa(pa), self.cw_slow(pv)))
        print('right_fast', (self.up_more_right_pa(pa), self.ccw_slow(pv)))
        print('right_fast', (self.up_more_right_pa(pa), self.cw_slow(pv)))
        print('left_fast', (self.up_more_left_pa(pa), self.ccw_slow(pv)))
        print('left_fast', (self.up_more_left_pa(pa), self.cw_slow(pv)))
        print('left_slow', (self.up_more_right_pa(pa), self.ccw_fast(pv)))
        print('right_fast', (self.up_more_right_pa(pa), self.cw_fast(pv)))
        print('right_slow', (self.up_more_left_pa(pa), self.cw_fast(pv)))
        print('left_fast', (self.up_more_left_pa(pa), self.ccw_fast(pv)))
        print('right_fast', (self.down_more_right_pa(pa), self.ccw_slow(pv)))
        print('stop', (self.down_right_pa(pa), self.cw_slow(pv)))
        print('left_fast', (self.down_more_left_pa(pa), self.cw_fast(pv)))
        print('stop', (self.down_more_left_pa(pa), self.ccw_fast(pv)))
        print('stop', (self.down_more_right_pa(pa), self.ccw_fast(pv)))
        print('stop', (self.down_more_right_pa(pa), self.cw_fast(pv)))
        print('stop', (self.down_more_left_pa(pa), self.cw_fast(pv)))
        print('stop', (self.down_more_left_pa(pa), self.ccw_fast(pv)))
        print('right_fast', (self.down_right_pa(pa), self.ccw_slow(pv)))
        print('right_fast', (self.down_right_pa(pa), self.cw_slow(pv)))
        print('left_fast', (self.down_left_pa(pa), self.cw_slow(pv)))
        print('left_fast', (self.down_left_pa(pa), self.ccw_slow(pv)))
        print('stop', (self.down_right_pa(pa), self.ccw_fast(pv)))
        print('right_slow', (self.down_right_pa(pa), self.cw_fast(pv)))
        print('stop', (self.down_left_pa(pa), self.cw_fast(pv)))
        print('left_slow', (self.down_left_pa(pa), self.ccw_fast(pv)))
        print('right_slow', (self.up_right_pa(pa), self.ccw_slow(pv)))
        print('right_fast', (self.up_right_pa(pa), self.cw_slow(pv)))
        print('right_fast', (self.up_right_pa(pa), self.stop(pv)))
        print('left_slow', (self.up_left_pa(pa), self.cw_slow(pv)))
        print('left_fast', (self.up_left_pa(pa), self.ccw_slow(pv)))
        print('left_fast', (self.up_left_pa(pa), self.stop(pv)))
        print('left_fast', (self.up_right_pa(pa), self.ccw_fast(pv)))
        print('right_fast', (self.up_right_pa(pa), self.cw_fast(pv)))
        print('right_fast', (self.up_left_pa(pa), self.cw_fast(pv)))
        print('left_fast', (self.up_left_pa(pa), self.ccw_fast(pv)))
        print('right_fast', (self.down_pa(pa), self.stop(pv)))
        print('stop', (self.down_pa(pa), self.cw_fast(pv)))
        print('stop', (self.down_pa(pa), self.ccw_fast(pv)))
        print('left_slow', (self.up_pa(pa), self.ccw_slow(pv)))
        print('left_fast', (self.up_pa(pa), self.ccw_fast(pv)))
        print('right_slow', (self.up_pa(pa), self.cw_slow(pv)))
        print('right_fast', (self.up_pa(pa), self.cw_fast(pv)))
        print('stop', (self.up_pa(pa), self.stop(pv)))
        return force_fuzzy_memberships

    def decide(self, world):
        inputs = self._make_input(world)
        fuzzy_outputs = self.rules(inputs['pa'], inputs['pv'])

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
            sum += max(left_fast_force_points[i],left_slow_points[i],right_fast_points[i],right_slow_points[i],stop_points[i]) * x_axis[i]
            sum_makhraj += max(left_fast_force_points[i],left_slow_points[i],right_fast_points[i],right_slow_points[i],stop_points[i])
        if sum_makhraj !=0:
            return sum/(sum_makhraj*1.0)
        else:
            return 0