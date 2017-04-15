from objective.basic_objective import BasicObjective
from agents.collector import Collector
from agents.wood import WoodResource
import random

class CollectObjective(BasicObjective):

    def __init__(self, priority):
        super().__init__(priority)

    def execute(self, agent):

        if isinstance(agent, Collector):
            agent = agent
        else:
            raise Exception('El objetivo de recolectar solo se puede asignar a un recolector')

        if agent.model.wood:

            # If there is wood available, take it
            this_cell = agent.model.grid.get_cell_list_contents([agent.position])
            chop_tree = random.choice([True, True, False])
            for obj in this_cell:
                if isinstance(obj, WoodResource):
                    wood_patch = obj
                    if wood_patch.fully_grown:
                        if chop_tree:
                            print('Agent ', agent.position, ' chopped the tree')
                            agent.wood += 1
                            agent.model.grid.remove_agent(obj)
                            agent.model.schedule.remove(obj)
                        else:
                            agent.wood += 1
                            wood_patch.fully_grown = False