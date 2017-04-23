import random

from mesa import Model
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from objectives.collect_objective import CollectObjective
from agents.collector import Collector
from agents.wood import Wood
from controllers.world_controller import WorldController


class World(Model):
    height = 0
    width = 0

    initial_collector = 0
    wood = False
    wood_regrowth_time = 300

    verbose = False  # Print-monitoring

    def __init__(self, height=30, width=30,
                 initial_collector=5,
                 initial_artisans=1,
                 wood=False, wood_regrowth_time=1000):

        # Set parameters
        self.height = height
        self.width = width
        self.initial_collector = initial_collector
        self.wood = wood
        self.wood_regrowth_time = wood_regrowth_time

        self.schedule = WorldController(self)
        self.grid = MultiGrid(self.height, self.width, torus=False)

        # Create collector:
        for i in range(self.initial_collector):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            collector = Collector((x, y), self, wood)
            objective = CollectObjective(1)
            # collector.add_objective(objective)
            self.grid.place_agent(collector, (x, y))
            self.schedule.add(collector)


        #  Create wood patches
            if self.wood:

             for agent, x, y in self.grid.coord_iter():
                 place_wood = random.choice([True, False, False, False, False])
                 if place_wood:
                     fully_grown = random.choice([True, False, False, False, False, False, False, False, False, False, False])

                     if fully_grown:
                         countdown = self.wood_regrowth_time
                     else:
                         countdown = random.randrange(self.wood_regrowth_time)

                     patch = Wood((x, y), self, fully_grown, countdown)
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
            print('Initial number collector: ', self.schedule.get_breed_count(Collector))

        for i in range(step_count):
            self.step()

        if self.verbose:
            print('')
            print('Final number collector: ', self.schedule.get_breed_count(Collector))
