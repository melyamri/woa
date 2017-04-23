class Objective():
    PENDING = "pending"
    SOLVING = "solving"
    FINISHED = "finished"

    status = PENDING
    priority = 0

    def __init__(self, priority):
        self.priority = priority

    def class_name(self):
        return "Objective"
