from tasks.basic_task import BasicTask
from agents.collector import Collector
from agents.wood import Wood
import random

class MoveToTask(BasicTask):

    def execute(self, agent, target):
        (x, y) = target
        next_moves = agent.model.grid.get_neighborhood(agent.pos, True ,False)
        best_pos = next_moves[0]
        for px, py in next_moves:
            (bx, by) = best_pos
            if (abs(x-px)+abs(y-py)) <   (abs(x-bx)+abs(y-by)):
                best_pos = (px,px)
        next_move = best_pos
        # Now move:
        agent.log("El agente " + str(agent.pos) + " se mueve a la casilla " +  str(next_move))
        agent.model.grid.move_agent(agent, next_move)
