import random

from mesa import Agent

from world_of_agents_core.agents.custom_agent import CustomAgent
from world_of_agents_core.agents.wood import WoodResource


class Collector(CustomAgent):
    '''
    A sheep that walks around, reproduces (asexually) and gets eaten.

    The init is the same as the CustomAgent.
    '''

    wood = 0

    def __init__(self, pos, model, moore, wood=0):
        super().__init__(pos, model, moore=moore)
        self.wood = wood

    def step(self):
        '''
        A model step. Move, collect wood if there is any.
        '''
        self.random_move()
        living = True

        if self.model.wood:

            # If there is wood available, take it
            this_cell = self.model.grid.get_cell_list_contents([self.pos])
            chop_tree = random.choice([True,False])
            for obj in this_cell:
                if isinstance(obj, WoodResource):
                    wood_patch = obj
                    if wood_patch.fully_grown:
                        if chop_tree:
                            print('Agent ',self.pos,' chopped the tree')
                            self.wood += 1
                            self.model.grid.remove_agent(obj)
                            self.model.schedule.remove(obj)
                        else:
                            self.wood += 1
                            wood_patch.fully_grown = False

    def get_wood(self):
        return self.wood

    def get_portrayal(self):
        portrayal = {"Shape": "rect",
                     "h": 1,
                     "w": 1,
                     "Color": "blue",
                     "Layer": 2,
                     "Filled": "true"}

        if self.get_wood() > 10:
            portrayal["Color"] = "red"

        return portrayal