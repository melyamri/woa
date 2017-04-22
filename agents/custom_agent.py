'''
Generalized behavior for random walking, one grid cell at a time.
'''

from mesa import Agent
from intellect.Intellect import Intellect

class CustomAgent(Agent, Intellect):
    x = None
    y = None

    def __init__(self, position, model, file):
        super().__init__(position, model)
        self.position = position
        self.objectives = []
        self.learn(file)

    def get_portrayal(self):
        return {
            "Shape": "circle",
            "r": 1,
            "Color": "black",
            "Layer": 1,
            "Filled": "true"
        }


    def add_objective(self, objective):
        self.objectives.append(objective)

    def execute_task(self, task):
        task_manager.execute(task, self)

    def decide(self):
        self.reason(self.class_name)

    def step(self):
        self.decide()

    def class_name(self):
        return "CustomAgent"
