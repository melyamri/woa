from objectives.objective import Objective

class CreateToolsObjective(Objective):

    def __init__(self, priority):
        super().__init__(priority)
        self. waiting = False

    def class_name(self):
        return "CreateToolsObjective"

