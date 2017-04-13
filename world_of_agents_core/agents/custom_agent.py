'''
Generalized behavior for random walking, one grid cell at a time.
'''

import random

from mesa import Agent
from world_of_agents_core.objective.basic_objective import BasicObjective

class CustomAgent(Agent):
    '''
    Class implementing random walker methods in a generalized manner.

    Not indended to be used on its own, but to inherit its methods to multiple
    other agents.

    '''

    grid = None
    x = None
    y = None
    moore = True
    objectives = []

    def __init__(self, pos, model, moore=True):
        '''
        grid: The MultiGrid object in which the agent lives.
        x: The agent's current x coordinate
        y: The agent's current y coordinate
        moore: If True, may move in all 8 directions.
                Otherwise, only up, down, left, right.
        '''
        super().__init__(pos, model)
        self.pos = pos
        self.moore = moore

    def random_move(self):
        '''
        Step one cell in any allowable direction.
        '''
        # Pick the next cell from the adjacent cells.
        next_moves = self.model.grid.get_neighborhood(self.pos, self.moore, True)
        next_move = random.choice(next_moves)
        # Now move:
        self.model.grid.move_agent(self, next_move)

    def set_quest(self,objective):
        self.objectives.append(objective)

    def get_best_objective(self):
        if self.objectives.count() > 1:
            return self.objectives[0]

    def get_portrayal(self):
        portrayal = {"Shape": "circle",
                     "r": 1,
                     "Color": "black",
                     "Layer": 1,
                     "Filled": "true"}
