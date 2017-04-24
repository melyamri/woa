from tasks.move_task import MoveTask
from tasks.collect_task import CollectTask
from tasks.give_task import GiveTask
from tasks.tools_task import ToolsTask
from tasks.move_to_task import MoveToTask
from tasks.build_task import *

class TaskManager():

    MOVE = MoveTask()
    MOVETO = MoveToTask()
    COLLECT = CollectTask()
    GIVE = GiveTask()
    TOOLS = ToolsTask()
    BUILDER = BuilderTask()
    BUILD_HOUSE = BuildHouseTask()

    def __init__(self):
        return

    def execute(task, agent):
        task.execute(agent)
