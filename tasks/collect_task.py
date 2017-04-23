from tasks.basic_task import BasicTask
from agents.collector import Collector
from agents.wood import WoodResource
import random

class CollectTask(BasicTask):

    def __init__(self, agent):
        super().__init__(agent)

    def execute(self):
        if not isinstance(self.agent, Collector):
            raise Exception('El objetivo de recolectar solo se puede asignar a un recolector'   )

        if self.agent.model.wood:

            # If there is wood available, take it
            this_cell = self.agent.model.grid.get_cell_list_contents([self.agent.pos])
            chop_tree = random.choice([True, True, False])
            for obj in this_cell:
                if isinstance(obj, WoodResource):
                    wood_patch = obj
                    if wood_patch.fully_grown:
                        if chop_tree:
                            print('Agent ', self.agent.pos, ' chopped the tree')
                            self.agent.wood += 1
                            self.agent.model.grid.remove_agent(obj)
                            self.agent.model.schedule.remove(obj)
                        else:
                            self.agent.wood += 1
                            wood_patch.fully_grown = False