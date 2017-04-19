'''
Generalized behavior for random walking, one grid cell at a time.
'''

from mesa import Agent

class CustomAgent(Agent):
    '''
    Clase agente para todos los agentes del sistema.

    La clase consta de:
    - Grid: es el puntero al mapa para poder sacar información de el.
    - X,Y: es la posición del mapa en la que se encuenta el agente.
    '''

    x = None
    y = None

    def __init__(self, pos, model):
        '''
        map: The MultiGrid object in which the agent lives.
        x: The agent's current x coordinate
        y: The agent's current y coordinate
        multi_direction_movement: If True, may move in all 8 directions.
                Otherwise, only up, down, left, right.
        '''
        super().__init__(pos, model)
        self.pos = pos

    def get_portrayal(self):
        portrayal = {"Shape": "circle",
                     "r": 1,
                     "Color": "black",
                     "Layer": 1,
                     "Filled": "true"}

    def get_position(self):
        return self.pos