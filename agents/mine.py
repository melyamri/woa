import random

from agents.custom_agent import CustomAgent
from agents.house import House

class Mine(CustomAgent):
    '''Mina que da recursos, una vez se recogen todos los que puede generar, desaparece'''

    resources = 100
    empty = False

    def __init__(self, pos, model, empty):
        '''Creamos una nueva mina

        Args:
            empty: (boolean) Si la mina esta llena, empty = false
        '''
        super().__init__(pos, model)
        self.empty = empty
    def step(self):
        #if not self.empty:
            # Si la mina no esta vacia
        #    self.resources -=1

    def get_portrayal(self):
        return {
            "Shape": "assets/mine.png" if not self.empty else "assets/mine.png",
            "Color": "Grey",
            "Layer": 1,
        }


    def class_name(self):
        return "Mine"
