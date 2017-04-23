from agents.human_agent import HumanAgent


class Artisan(HumanAgent):
    '''
    A sheep that walks around, reproduces (asexually) and gets eaten.

    The init is the same as the CustomAgent.
    '''

    def __init__(self, pos, model, wood=0):
        super().__init__(pos, model)
        self.tools = 0

    def get_portrayal(self):
        portrayal = {"Shape": "assets/artisan.png",
                     "h": 1,
                     "w": 1,
                     "Color": "green",
                     "Layer": 2,
                     "Filled": "true"}

        if self.tools > 0:
            portrayal["Color"] = "black"

        return portrayal