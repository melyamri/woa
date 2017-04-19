from objective.move_objective import MoveObjective
from agents.collector import Collector
from agents.artisan import Artisan
from agents.wood import WoodResource
import random

class ToolObjective(MoveObjective):

    def __init__(self, priority):
        super().__init__(priority)
        self. waiting = False


    def execute(self, agent_source):

        if not(isinstance(agent_source, Artisan)):
            raise Exception('El objetivo de crear herramientas solo se puede asignar a un artesano')

        if not self.waiting:
            super().execute(agent_source)

        if agent_source.model.wood:

            # If there is wood available, take it
            this_cell = agent_source.model.grid.get_cell_list_contents([agent_source.pos])
            chop_tree = random.choice([True, True, False])
            for obj in this_cell:
                if isinstance(obj, WoodResource):
                    wood_patch = obj
                    if wood_patch.fully_grown:
                        if chop_tree:
                            print('Agent ', agent.pos, ' chopped the tree')
                            agent.wood += 1
                            agent.model.grid.remove_agent(obj)
                            agent.model.schedule.remove(obj)
                        else:
                            agent.wood += 1
                            wood_patch.fully_grown = False