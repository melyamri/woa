from tasks.basic_task import BasicTask
import random

class MoveTask(BasicTask):

    def execute(self, agent):
        '''
        Step one cell in any allowable direction.
        '''
        # Pick the next cell from the adjacent cells.
        next_moves = agent.model.grid.get_neighborhood(agent.pos, True ,False)
        next_move = random.choice(next_moves)
        # Now move:
        agent.log("El agente " + str(agent.pos) + " se mueve a la casilla " +  str(next_move))
        agent.model.grid.move_agent(agent, next_move)
        #self.pos = next_move
