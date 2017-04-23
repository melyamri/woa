'''
Generalized behavior for random walking, one grid cell at a time.
'''

from mesa import Agent
#from controllers.task_manager import TaskManager
from py4j.java_gateway import JavaGateway, CallbackServerParameters
# from intellect.Intellect import Intellect

class CustomAgent(Agent, object):
    x = None
    y = None

    def __init__(self, position, model,): # file):
        super().__init__(position, model)
        self.pos = position
        self.objectives = []
        self.model = model

    def log(self, text):
        self.model.log.append(text)
        self.model.log = self.model.log[-5:]

    def get_portrayal(self):
        return {
            "Shape": "circle",
            "r": 1,
            "Color": "black",
            "Layer": 1,
            "Filled": "true"
        }

    '''
    def test(self, name):
        print(name)

    def add_objective(self, objective):
        self.objectives.append(objective)

    def execute_task(self, task):
        TaskManager.execute(task, self)

    def decide(self):
        # self.reason(self.class_name)
        # self.execute_task(TaskManager.MOVE)
        self.knowledge_session.fireAllRules()

    def step(self):
        self.decide()

    def class_name(self):
        return "CustomAgent"

    def _get_object_id(f):
        return "CustomAgent"
'''

