#!/usr/bin/env python
# -*- coding: utf-8 -*-

# project imports
from conf import ConfigReader
from conf2 import ConfigReader2
from world import World
from controller import FuzzyController
from controller2 import FuzzyController2
from controller3 import FuzzyController3
from manager import Manager


conf = ConfigReader()
conf2 = ConfigReader2()

if __name__ == '__main__':
    # simple
    # world = World(**conf.world_config())
    # controller = FuzzyController(**conf.controller_config())
    # manager = Manager(world, controller, **conf.simulation_config())
    # manager.run()

    # complex
    # world = World(**conf2.world_config())
    # controller = FuzzyController(**conf2.controller_config())
    # manager = Manager(world, controller, **conf2.simulation_config())
    # manager.run()

    # simple
    world = World(**conf.world_config())
    controller2 = FuzzyController2()
    manager = Manager(world, controller2, **conf.simulation_config())
    manager.run()

    # complex
    # world = World(**conf.world_config())
    # controller3 = FuzzyController3()
    # manager = Manager(world, controller3, **conf.simulation_config())
    # manager.run()
