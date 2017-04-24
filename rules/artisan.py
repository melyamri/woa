from controllers.task_manager import TaskManager
from objectives.objective import Objective
from objectives.simple_objective import SimpleObjective

def run_all(agent):
    rule_init(agent)
    rule_move(agent)
    rule_assign(agent)
    rule_give(agent)

def rule_init(agent):
    if agent.objective.status == Objective.PENDING:
        agent.objective.status = Objective.SOLVING

    if agent.objective.status == Objective.FINISHED:
        agent.objective = SimpleObjective()


def rule_move(agent):
    if agent.objective.class_name() == "CreateToolsObjective" \
            and agent.objective.status == Objective.SOLVING\
            and agent.get_n_tools() < 1:
        agent.execute_task(TaskManager.MOVE)

    if agent.objective.class_name() == "CreateToolsObjective" \
            and agent.objective.status == Objective.SOLVING\
            and agent.get_n_tools() > 0:
        agent.execute_task(TaskManager.MOVETO)

    if agent.objective.class_name() == "SimpleObjective":
        agent.execute_task(TaskManager.MOVE)

def rule_assign(agent):
    if agent.objective.class_name() == "CreateToolsObjective" \
            and agent.objective.status == Objective.SOLVING\
            and agent.get_n_tools() < 1:
        agent.execute_task(TaskManager.TOOLS)

def rule_give(agent):
    if agent.objective.class_name() == "CreateToolsObjective" \
            and agent.objective.status == Objective.SOLVING\
            and agent.get_n_tools() > 0\
            and builder_in_range(agent):
        agent.execute_task(TaskManager.GIVE)
        agent.objective.status = Objective.FINISHED
    return

def builder_in_range(agent):
    (x,y) = agent.pos
    (tx,ty) = agent.quest_giver.pos
    if abs(x-tx) <= 1 and abs(y-ty) <=1:
        return True
    else:
        return False