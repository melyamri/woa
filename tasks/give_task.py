from tasks.basic_task import BasicTask

class GiveTask(BasicTask):

    def execute(self, agent, **kwargs):
        class_name = agent.class_name().lower()
        if class_name == 'collector':
            if agent.give_wood():
                agent.quest_giver.receive_wood()
                agent.log('El agente '+ str(agent.pos)+ ' le entrega la madera al '+str(agent.quest_giver.pos))
            else:
                raise Exception("El agente ",agent.pos," no dispone de madera para el agente ",agent.quest_giver.pos)
        if class_name == 'artisan':
            if agent.give_tools():
                agent.quest_giver.receive_tools()
                agent.log('El agente '+ str(agent.pos)+ ' le entrega las herramientas al '+str(agent.quest_giver.pos))
            else:
                raise Exception("El agente ",agent.pos," no dispone de herramientas para el agente ",agent.quest_giver.pos)