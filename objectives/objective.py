class Objective():
    self.PENDING = "pending"
    self.SOLVING = "solving"
    self.FINISHED = "finished"

    status = Objective.PENDING
    priority = 0

    def __init__(self, priority):
        self.priority = priority
