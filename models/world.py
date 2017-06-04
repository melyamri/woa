import random

from mesa import Model
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from objectives.build_objective import BuildHouseObjective
from objectives.tools_objective import CreateToolsObjective

from agents.collector import Collector
from agents.artisan import Artisan
from agents.builder import Builder
from agents.wood import Wood
from agents.house import House
from agents.mine import Mine
from agents.terrain import Terrain

from controllers.world_controller import WorldController


class World(Model):
    height = 0
    width = 0

    initial_collector = 0
    wood = False
    wood_regrowth_time = 300
    iron = False

    verbose = False  # Print-monitoring
    log = []

    def __init__(self, height=30, width=30,
                 initial_collector=5,
                 initial_artisans=1,
                 initial_builders=1,
                 wood=False,
                 iron=False,
                 nmines = 3,
                 wood_regrowth_time=1000):

        # Set parameters
        self.height = height
        self.width = width
        self.nmines = nmines

        self.initial_collector = initial_collector
        self.initial_artisans = initial_artisans
        self.initial_builders = initial_builders

        self.wood = wood
        self.iron = iron
        self.wood_regrowth_time = wood_regrowth_time

        self.schedule = WorldController(self)
        self.grid = MultiGrid(self.height, self.width, torus=False)
        self.log = []

        self.datacollector = DataCollector(
            {"Wood": lambda m: m.schedule.get_breed_count(Wood),
             "Collectors": lambda m: m.schedule.get_breed_count(Collector),
             "Artisans": lambda m: m.schedule.get_breed_count(Artisan),
             "Builders": lambda m: m.schedule.get_breed_count(Builder),
             "Houses": lambda m: m.schedule.get_breed_count(House),
             "Mineral": lambda m: m.schedule.get_breed_count(Mine)
             })
        for agent, x, y in self.grid.coord_iter():
            terrain = Terrain((x, y), self)
            self.grid.place_agent(terrain, (x, y))

        for i in range(self.initial_collector):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            collector = Collector((x, y), self)
            self.grid.place_agent(collector, (x, y))
            self.schedule.add(collector)

        for i in range(self.initial_artisans):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            artisan = Artisan((x, y), self)
            self.grid.place_agent(artisan, (x, y))
            self.schedule.add(artisan)

        for i in range(self.initial_builders):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            builder = Builder((x, y), self)
            builder.add_objective(BuildHouseObjective(5), None)
            self.grid.place_agent(builder, (x, y))
            self.schedule.add(builder)

        # Create resources
        nminesplaced = 0
        if self.wood:

            for agent, x, y in self.grid.coord_iter():
                place_wood = random.choice([True, False, False, False, False])
                if place_wood:
                    fully_grown = random.choice(
                        [True, False, False, False, False, False, False, False, False, False, False])

                    if fully_grown:
                        countdown = self.wood_regrowth_time
                    else:
                        countdown = random.randrange(self.wood_regrowth_time)

                    patch = Wood((x, y), self, fully_grown, countdown)
                    self.grid.place_agent(patch, (x, y))
                    self.schedule.add(patch)

        if self.iron:
            for agent, x, y in self.grid.coord_iter():
                place_iron = random.choice([True, False, False,False, False,False, False ,False, False, False, False])
                if place_iron and nminesplaced < nmines:
                    empty = False
                    patch = Mine((x, y), self, empty)
                    self.grid.place_agent(patch, (x, y))
                    self.schedule.add(patch)
                    nminesplaced += 1

        self.running = True

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)
        if self.verbose:
            print('Step: ', [self.schedule.time,
                             self.schedule.get_breed_count(Collector)])

    def run_model(self, step_count=200):

        if self.verbose:
            print('Initial number collector: ', self.schedule.get_breed_count(Collector))

        for i in range(step_count):
            self.step()

        if self.verbose:
            print('')
            print('Final number collector: ', self.schedule.get_breed_count(Collector))
