from objective.move_objective import MoveObjective
from agents.collector import Collector
from agents.wood import WoodResource
import random

class CollectObjective(MoveObjective):

    def __init__(self, priority):
        super().__init__(priority)

    def execute(self, agent):

        if not isinstance(agent, Collector):
            raise Exception('El objetivo de recolectar solo se puede asignar a un recolector')

        super().execute(agent)

        if agent.model.wood:

            # If there is wood available, take it
            this_cell = agent.model.grid.get_cell_list_contents([agent.pos])
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