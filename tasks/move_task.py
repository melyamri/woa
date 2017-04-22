import random

class MoveTask():
    def execute(self, agent):
        next_moves = agent.model.grid.get_neighborhood(agent.pos, True ,False)
        next_move = random.choice(next_moves)
        # Now move:
        print("El agente " ,agent.pos, " se mueve a la casilla ", next_move)
        agent.model.grid.move_agent(agent, next_move)
