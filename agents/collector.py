import random

from mesa import Agent

from agents.custom_agent import CustomAgent
from agents.wood import WoodResource


class Collector(CustomAgent):
    wood = 0

    def __init__(self, pos, model, wood=0):
        super().__init__(pos, model, "rules/collector.drl")
        self.wood = wood

    def get_portrayal(self):
        return {
            "Shape": "rect",
            "h": 1,
            "w": 1,
            "Color": red if (self.wood > 10) else "blue",
            "Layer": 2,
            "Filled": "true"
        }
