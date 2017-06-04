from agents.custom_agent import CustomAgent
from controllers.task_manager import TaskManager
from controllers.rule_manager import RuleManager
from objectives.simple_objective import SimpleObjective

class InertAgent(CustomAgent):

    def __init__(self, position, model):
        super().__init__(position, model)

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

    def class_name(self):
        return "InertAgent"

    def _get_object_id(f):
        return "InertAgent"
