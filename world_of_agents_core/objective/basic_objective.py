

class BasicObjective():

    def __init__(self, priority):
        self.priority = priority
        self.active = True

    def execute(self, agent):
        return