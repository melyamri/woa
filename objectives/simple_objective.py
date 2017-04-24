from objectives.objective import Objective

class SimpleObjective(Objective):

    def __init__(self):
        super().__init__(0)

    def class_name(self):
        return "SimpleObjective"
