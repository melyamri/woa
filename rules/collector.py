from controllers.task_manager import TaskManager


def run_all(agent):
    rule_move(agent)

def rule_move(agent):
    if True:
        agent.execute_task(TaskManager.MOVE)
