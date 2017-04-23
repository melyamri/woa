from controllers.task_manager import TaskManager
from objectives.objective import Objective


def run_all(agent):
    rule_init(agent)
    rule_move(agent)
    rule_collect(agent)

def rule_init(agent):
    if agent.objectives[0].status == Objective.PENDING:
        agent.objectives[0].status = Objective.SOLVING

def rule_move(agent):
    if agent.objectives[0].class_name() == "CollectObjective" and agent.objectives[0].status == Objective.SOLVING:
        agent.execute_task(TaskManager.MOVE)

def rule_collect(agent):
    if agent.objectives[0].class_name() == "CollectObjective" and agent.objectives[0].status == Objective.SOLVING:
        agent.execute_task(TaskManager.COLLECT)
