'''
Wolf-Collector Predation Model
================================

Replication of the model found in NetLogo:
    Wilensky, U. (1997). NetLogo Wolf Collector Predation model.
    http://ccl.northwestern.edu/netlogo/models/WolfCollectorPredation.
    Center for Connected Learning and Computer-Based Modeling,
    Northwestern University, Evanston, IL.
'''

import random

from mesa import Model
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from objective.collect_objective import CollectObjective
from agents.collector import Collector
from agents.wood import WoodResource
from controller.schedule_controller import RandomActivationByBreed


class CollectorModel(Model):
    '''
    Wolf-Collector Predation Model
    '''

    height = 0
    width = 0

    initial_collector = 0

    collector_reproduce = 0.04
    wood = False
    wood_regrowth_time = 300
    collector_gain_from_food = 4

    verbose = False  # Print-monitoring

    def __init__(self, height=30, width=30,
                 initial_collector=5,
                 collector_reproduce=0.04,
                 wood=False, wood_regrowth_time=1000):
        '''
        Create a new Wolf-Collector model with the given parameters.

        Args:
            initial_collector: Number of collector to start with
            collector_reproduce: Probability of each collector reproducing each step
            wood_regrowth_time: How long it takes for a wood patch to regrow
                                 once it is eaten
        '''

        # Set parameters
        self.height = height
        self.width = width
        self.initial_collector = initial_collector
        self.collector_reproduce = collector_reproduce
        self.wood = wood
        self.wood_regrowth_time = wood_regrowth_time

        self.schedule = RandomActivationByBreed(self)
        self.grid = MultiGrid(self.height, self.width, torus=True)

        # Create collector:
        for i in range(self.initial_collector):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            wood = 0
            collector = Collector((x, y), self, wood)
            collector.set_quest(CollectObjective(1))
            self.grid.place_agent(collector, (x, y))
            self.schedule.add(collector)


        # Create wood patches
        if self.wood:

            for agent, x, y in self.grid.coord_iter():
                place_wood = random.choice([True, False, False, False, False])
                if place_wood:
                    fully_grown = random.choice([True, False, False, False, False, False, False, False, False, False, False])

                    if fully_grown:
                        countdown = self.wood_regrowth_time
                    else:
                        countdown = random.randrange(self.wood_regrowth_time)

                    patch = WoodResource((x, y), self, fully_grown, countdown)
                    self.grid.place_agent(patch, (x, y))
                    self.schedule.add(patch)

        self.running = True

    def step(self):
        self.schedule.step()
        if self.verbose:
            print('Step: ',[self.schedule.time,
                   self.schedule.get_breed_count(Collector)])

    def run_model(self, step_count=200):

        if self.verbose:
            print('Initial number collector: ',
                  self.schedule.get_breed_count(Collector))

        for i in range(step_count):
            self.step()

        if self.verbose:
            print('')
            print('Final number collector: ',
                  self.schedule.get_breed_count(Collector))
