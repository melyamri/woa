from agents.custom_agent import CustomAgent
from controllers.task_manager import TaskManager
from controllers.rule_manager import RuleManager
from objectives.simple_objective import SimpleObjective
import os

class ActiveAgent(CustomAgent):
    x = None
    y = None

    def __init__(self, position, model):
        super().__init__(position, model)
        self.objective = SimpleObjective()
        self.quest_giver = None

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

    def add_objective(self, objective, quest_giver):
        if self.objective.priority < objective.priority:
            self.objective = objective
            self.quest_giver = quest_giver

    def execute_task(self, task):
        TaskManager.execute(task, self)

    def decide(self):
        RuleManager.reason(self)

    def step(self):
        self.decide()

    def class_name(self):
        return "CustomAgent"

    def _get_object_id(f):
        return "CustomAgent"

    def has_complex_objective(self):
        return self.objective.class_name().lower() != "simplebbjective"