from tasks.basic_task import BasicTask
from objectives.tools_objective import CreateToolsObjective

class BuilderTask(BasicTask):

    def execute(self, agent,  **kwargs):
        visible_area = agent.model.grid.get_neighborhood(agent.pos, True ,False, radius=2)
        for cell in visible_area:
            this_cell = agent.model.grid.get_cell_list_contents([cell])
            for agents in this_cell:
                class_name = agents.class_name().lower()
                if class_name == 'artisan':
                    if agents.add_objective(CreateToolsObjective(2),agent):
                        agent.waiting = True


class BuildHouseTask(BasicTask):
    def execute(self, agent, **kwargs):
        agent.build_house()