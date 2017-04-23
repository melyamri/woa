from tasks.basic_task import BasicTask
from agents.collector import Collector
from agents.wood import WoodResource
import random

class MoveToTask(BasicTask):

    def __init__(self, agent, x, y):
        super().__init__(agent)
        self.target = (x, y)

    def execute(self):
        self.agent.move_to(self.target)