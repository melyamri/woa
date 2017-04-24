from controllers.task_manager import TaskManager
from objectives.objective import Objective
from objectives.simple_objective import SimpleObjective

def run_all(agent):
    rule_init(agent)
    rule_move(agent)
    rule_assign(agent)
    rule_build(agent)

def rule_init(agent):
    if agent.objective.status == Objective.PENDING:
        agent.objective.status = Objective.SOLVING

    if agent.objective.status == Objective.FINISHED:
        agent.objective = SimpleObjective()


def rule_move(agent):
    if agent.objective.class_name() == "BuildHouseObjective" \
            and agent.objective.status == Objective.SOLVING:
        agent.execute_task(TaskManager.MOVE)

    if agent.objective.class_name() == "SimpleObjective":
        agent.execute_task(TaskManager.MOVE)

def rule_assign(agent):
    if agent.objective.class_name() == "BuildHouseObjective" \
            and agent.objective.status == Objective.SOLVING\
            and agent.get_n_tools() < 1:
        agent.execute_task(TaskManager.BUILDER)

def rule_build(agent):
    if agent.objective.class_name() == "BuildHouseObjective" \
            and agent.objective.status == Objective.SOLVING\
            and agent.get_n_tools() > 0\
            and check_terrain(agent):
        agent.execute_task(TaskManager.BUILD_HOUSE)
        agent.execute_task(TaskManager.BUILD_HOUSE)
    return

def check_terrain(agent):
    return agent.is_terrain_buildable()