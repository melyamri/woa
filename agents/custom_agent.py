'''
Generalized behavior for random walking, one grid cell at a time.
'''

from mesa import Agent
from controllers.task_manager import TaskManager
from py4j.java_gateway import JavaGateway
# from intellect.Intellect import Intellect

class CustomAgent(Agent):
    x = None
    y = None

    def __init__(self, position, model, file):
        super().__init__(position, model)
        self.position = position
        self.objectives = []
        gateway = JavaGateway()
        self.knowledge_session = gateway.entry_point.getKnowledgeSession("rules/collector.drl")
        # self.learn(file)

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
        TaskManager.execute(task, self)

    def decide(self):
        # self.reason(self.class_name)
        self.execute_task(TaskManager.MOVE)

    def step(self):
        self.decide()

    def class_name(self):
        return "CustomAgent"
