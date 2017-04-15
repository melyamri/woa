

class BasicObjective():

    priority = 0


    def __init__(self, priority):
        self.priority = priority

    def execute(self, agent):
        return