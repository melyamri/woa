from objective.basic_objective import BasicObjective

class MoveObjective(BasicObjective):

    def __init__(self, priority):
        super().__init__(priority)

    def execute(self, agent):
        agent.move()
        return