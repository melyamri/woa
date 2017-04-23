from tasks.basic_task import BasicTask
from agents.collector import Collector
from agents.wood import WoodResource
import random

class MoveTask(BasicTask):

    def __init__(self, agent):
        super().__init__(agent)

    def execute(self):
        self.agent.move()