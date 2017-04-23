from tasks.basic_task import BasicTask

class MoveTask(BasicTask):

    def __init__(self, agent):
        super().__init__(agent)

    def execute(self):
        self.agent.move()