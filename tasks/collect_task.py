from tasks.basic_task import BasicTask
from agents.collector import Collector
from agents.wood import Wood
import random

class CollectTask(BasicTask):

    def execute(self, agent):
        if not isinstance(agent, Collector):
            raise Exception('El objetivo de recolectar solo se puede asignar a un recolector'   )

        if agent.model.wood:

            # If there is wood available, take it
            this_cell = agent.model.grid.get_cell_list_contents([agent.pos])
            chop_tree = random.choice([True, True, False])
            for obj in this_cell:
                if isinstance(obj, Wood):
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
