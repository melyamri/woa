import random

from mesa import Agent

from agents.human_agent import HumanAgent
from agents.wood import WoodResource


class Collector(HumanAgent):
    '''
    A sheep that walks around, reproduces (asexually) and gets eaten.

    The init is the same as the CustomAgent.
    '''

    wood = 0

    def __init__(self, pos, model, wood=0):
        super().__init__(pos, model)
        self.wood = wood

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