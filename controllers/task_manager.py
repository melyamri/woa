from tasks.move_task import MoveTask
from tasks.collect_task import CollectTask

class TaskManager():

    MOVE = MoveTask()
    COLLECT = CollectTask()

    def __init__(self):
        return

    def execute(task, agent):
        task.execute(agent)
