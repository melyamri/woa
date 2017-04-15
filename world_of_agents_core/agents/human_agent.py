'''
Generalized behavior for random walking, one grid cell at a time.
'''

import random

from agents.custom_agent import CustomAgent
from objective.basic_objective import BasicObjective

class HumanAgent(CustomAgent):
    '''
    Class implementing random walker methods in a generalized manner.

    Not indended to be used on its own, but to inherit its methods to multiple
    other agents.

    '''

    objectives = []

    def __init__(self, position, model):
        '''
        map: The MultiGrid object in which the agent lives.
        x: The agent's current x coordinate
        y: The agent's current y coordinate
        multi_direction_movement: If True, may move in all 8 directions.
                Otherwise, only up, down, left, right.
        '''
        super().__init__(position, model)

    def random_move(self):
        '''
        Step one cell in any allowable direction.
        '''
        # Pick the next cell from the adjacent cells.
        next_moves = self.model.grid.get_neighborhood(self.position, True ,False)
        next_move = random.choice(next_moves)
        # Now move:
        self.model.grid.move_agent(self, next_move)
        self.position = next_move

    def set_quest(self,objective):
        self.objectives.append(objective)

    def execute_objectives(self):
        for objective in self.objectives:
            objective.execute(self)

    def step(self):
        self.random_move()
        self.execute_objectives()