from controllers.task_manager import TaskManager
from objectives.objective import Objective
from objectives.simple_objective import SimpleObjective


def run_all(agent):
    rule_init(agent)
    rule_move(agent)
    rule_give(agent)
    rule_collect(agent)


def rule_init(agent):
    if agent.objective.status == Objective.PENDING:
        agent.objective.status = Objective.SOLVING

    if agent.objective.status == Objective.FINISHED:
        agent.objective = SimpleObjective()

def rule_move(agent):
    if agent.objective.class_name() == "CollectObjective" \
            and agent.objective.status == Objective.SOLVING\
            and (agent.check_wood() < 1 or agent.check_iron() < 1 ):
        agent.execute_task(TaskManager.MOVE)

    if agent.objective.class_name() == "CollectObjective" \
            and agent.objective.status == Objective.SOLVING\
            and agent.check_wood() > 0\
            and agent.check_iron() > 0:
        agent.execute_task(TaskManager.MOVETO)

    if agent.objective.class_name() == "SimpleObjective":
        agent.execute_task(TaskManager.MOVE)

def rule_collect(agent):
    if agent.objective.class_name() == "CollectObjective" \
            and agent.objective.status == Objective.SOLVING\
            and (agent.check_wood() < 1 or agent.check_iron() < 1 ):
        agent.execute_task(TaskManager.COLLECT)

def rule_give(agent):
    if agent.objective.class_name() == "CollectObjective" \
            and agent.objective.status == Objective.SOLVING\
            and agent.check_wood() > 0\
            and agent.check_iron() > 0\
            and artisan_in_range(agent):
        agent.execute_task(TaskManager.GIVE)
        agent.objective.status = Objective.FINISHED
    return

def artisan_in_range(agent):
    (x,y) = agent.pos
    (tx,ty) = agent.quest_giver.pos
    if abs(x-tx) <= 1 and abs(y-ty) <=1:
        return True
    else:
        return False