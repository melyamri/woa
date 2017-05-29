from tasks.basic_task import BasicTask
import random

class CollectTask(BasicTask):

    def execute(self, agent,  **kwargs):
        if agent.class_name() is not "Collector":
            raise Exception('El objetivo de recolectar solo se puede asignar a un recolector'   )

        if agent.model.wood:

            # If there is wood available, take it
            this_cell = agent.model.grid.get_cell_list_contents([agent.pos])
            chop_tree = random.choice([True, True, False])
            for obj in this_cell:
                if obj.class_name() is "Wood":
                    wood_patch = obj
                    if wood_patch.fully_grown:
                        if chop_tree:
                            print('Agent ', agent.pos, ' chopped the tree')
                            agent.wood += 1
                            agent.model.grid.remove_agent(obj)
                            agent.model.schedule.remove(obj)
                        else:
                            agent.wood += 1
                            wood_patch.fully_grown = False

        if agent.model.iron:

            # If there is iron available, take it
            this_cell = agent.model.grid.get_cell_list_contents([agent.pos])
            chop_tree = random.choice([True, True, False])
            for obj in this_cell:
                if obj.class_name() is "Mine":
                    mine = obj
                    if  not mine.empty:
                        agent.iron +=1
                        mine.resources -=1
                        if mine.resources == 0:
                            mine.empty = True
                            agent.model.grid.remove_agent(obj)
                            agent.model.schedule.remove(obj)
