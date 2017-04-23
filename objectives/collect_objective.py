from objectives.objective import Objective

class CollectObjective(Objective):

    def __init__(self, priority):
        super().__init__(priority)

    def class_name(self):
        return "CollectObjective"
