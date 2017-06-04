from tasks.basic_task import BasicTask
import random

class MoveTask(BasicTask):

    def execute(self, agent,  **kwargs):
        '''
        Step one cell in any allowable direction.
        '''
        # Pick the next cell from the adjacent cells.
        class_name = agent.class_name().lower()
        if class_name == 'collector':
            self.collector_move(agent)
        elif class_name == 'artisan':
            self.artisan_move(agent)
        elif class_name == 'builder':
            self.builder_move(agent)
        else:
            self.random_move(agent)

    def collector_move(self, agent):
        visible_area = agent.model.grid.get_neighborhood(agent.pos, True, False, radius=4)
        candidate = None
        good_candidate = False
        dist = 1000
        for cell in visible_area:
            contents = agent.model.grid.get_cell_list_contents(cell)
            if agent.has_complex_objective():
                for obj in contents:
                    if agent.check_wood() <1:
                        if obj.class_name().lower() is "wood":
                            if (candidate is None) or (dist > self.dist(agent, candidate)):
                                candidate = cell
                                good_candidate = True
                                dist = self.dist(agent, candidate)
                    if agent.check_iron() <1:
                        if obj.class_name().lower() is "iron":
                            if (candidate is None) or (dist > self.dist(agent, candidate)):
                                candidate = cell
                                good_candidate = True
                                dist = self.dist(agent, candidate)

            else:
                for obj in contents:
                    if obj.class_name().lower() is "artisan":
                        if (candidate is None) or (dist > self.dist(agent, candidate)):
                            candidate = cell
                            good_candidate = True
                            dist = self.dist(agent, candidate)

        if good_candidate:
            self.move_towards(agent, candidate)
        else:
            self.random_move(agent)

    def artisan_move(self, agent):
        visible_area = agent.model.grid.get_neighborhood(agent.pos, True, False, radius=4)
        candidate = None
        good_candidate = False
        dist = 1000
        for cell in visible_area:
            contents = agent.model.grid.get_cell_list_contents(cell)
            if agent.has_complex_objective():
                for obj in contents:
                    if obj.class_name().lower() is "collector":
                        if (candidate is None) or (dist > self.dist(agent, candidate)):
                            candidate = cell
                            good_candidate = True
                            dist = self.dist(agent, candidate)
            else:
                for obj in contents:
                    if obj.class_name().lower() is "builder":
                        if (candidate is None) or (dist > self.dist(agent, candidate)):
                            candidate = cell
                            good_candidate = True
                            dist = self.dist(agent, candidate)

        if good_candidate:
            self.move_towards(agent, candidate)
        else:
            self.random_move(agent)

    def builder_move(self, agent):
        visible_area = agent.model.grid.get_neighborhood(agent.pos, True, False, radius=4)
        candidate = None
        good_candidate = False
        dist = 1000
        for cell in visible_area:
            contents = agent.model.grid.get_cell_list_contents(cell)
            if agent.get_n_tools() == 0:
                for obj in contents:
                    if obj.class_name().lower() is "artisan":
                        if (candidate is None) or (dist > self.dist(agent,candidate)):
                            candidate = cell
                            good_candidate = True
                            dist = self.dist(agent, candidate)
            else:
                clean_terrain = True
                for obj in contents:
                    if obj.class_name().lower() is "wood":
                        clean_terrain = False
                if clean_terrain:
                    good_candidate = True
                    candidate = cell

        if good_candidate:
            self.move_towards(agent, candidate)
        else:
            self.random_move(agent)

    def dist(self,agent,cell):
        (x, y) = cell
        (px,py) = agent.pos
        return abs(x - px) + abs(y - py)

    def move_towards(self,agent,target):
        (x, y) = target
        next_moves = agent.model.grid.get_neighborhood(agent.pos, True, False)
        best_pos = next_moves[0]
        for px, py in next_moves:
            (bx, by) = best_pos
            if (abs(x - px) + abs(y - py)) < (abs(x - bx) + abs(y - by)):
                best_pos = (px, py)
        next_move = best_pos
        # Now move:
        agent.log("El agente " + str(agent.pos) + " se mueve a la casilla " + str(next_move))
        agent.model.grid.move_agent(agent, next_move)

    def random_move(self,agent):
        next_moves = agent.model.grid.get_neighborhood(agent.pos, True, False)
        next_move = random.choice(next_moves)
        # Now move:
        agent.log("El agente " + str(agent.pos) + " se mueve a la casilla " + str(next_move))
        agent.model.grid.move_agent(agent, next_move)