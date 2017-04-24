import random

from agents.custom_agent import CustomAgent

class House(CustomAgent):

    def __init__(self, pos, model):
        '''
        Creates a new patch of wood

        Args:
            grown: (boolean) Whether the patch of wood is fully grown or not
            countdown: Time for the patch of wood to be fully grown again
        '''
        super().__init__(pos, model)

    def get_portrayal(self):
        return {
            "Shape": "assets/house.png",
            "Color": "green",
            "Layer": 1,
            "Filled": "true",
            "r" : "1"
        }
