'''
Generalized behavior for random walking, one grid cell at a time.
'''

import random

from agents.custom_agent import CustomAgent

class HumanAgent(CustomAgent):
    '''
    Class implementing random walker methods in a generalized manner.

    Not indended to be used on its own, but to inherit its methods to multiple
    other agents.

    '''

    def __init__(self, pos, model):
        '''
        map: The MultiGrid object in which the agent lives.
        x: The agent's current x coordinate
        y: The agent's current y coordinate
        multi_direction_movement: If True, may move in all 8 directions.
                Otherwise, only up, down, left, right.
        '''
        super().__init__(pos, model)
        self.objectives = []
        self.tasks = []

    def move(self):
        '''
        Step one cell in any allowable direction.
        '''
        # Pick the next cell from the adjacent cells.
        next_moves = self.model.grid.get_neighborhood(self.pos, True ,False)
        next_move = random.choice(next_moves)
        # Now move:
        self.log("El agente " + str(self.pos) + " se mueve a la casilla " +  str(next_move))

        self.model.grid.move_agent(self, next_move)
        #self.pos = next_move

    def move_to(self, target):
        (x, y) = target
        next_moves = self.model.grid.get_neighborhood(self.pos, True ,False)
        best_pos = next_moves[0]
        for px, py in next_moves:
            (bx, by) = best_pos
            if (abs(x-px)+abs(y-py)) <   (abs(x-bx)+abs(y-by)):
                best_pos = (px,px)
        next_move = best_pos
        # Now move:
        self.log("El agente " + str(self.pos) + " se mueve a la casilla " + str(next_move))
        self.model.grid.move_agent(self, next_move)

    def set_objective(self,objective):
        self.objectives.append(objective)

    def evaluate_objectives(self):
        for objective in self.objectives:
            objective.execute(self)

    def step(self):
        self.evaluate_objectives()
        self.execute_tasks()

    def add_task(self, task):
        self.tasks.append(task)

    def execute_tasks(self):
        for task in self.tasks:
            task.execute()
        self.tasks = []