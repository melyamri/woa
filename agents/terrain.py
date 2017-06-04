from agents.inert_agent import InertAgent

class Terrain(InertAgent):

    def __init__(self, pos, model):
        '''
        Creates a new patch of wood

        Args:
            grown: (boolean) Whether the patch of wood is fully grown or not
            countdown: Time for the patch of wood to be fully grown again
        '''
        super().__init__(pos, model)

    def get_portrayal(self):
        return {
            "Shape": "assets/terrain.png",
            "Color": "green",
            "Layer": 0,
            "Filled": "true",
            "r" : "1"
        }

    def class_name(self):
        return "Terrain"