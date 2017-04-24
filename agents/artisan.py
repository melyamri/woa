from agents.custom_agent import CustomAgent

class Artisan(CustomAgent):
    '''
    A sheep that walks around, reproduces (asexually) and gets eaten.

    The init is the same as the CustomAgent.
    '''

    def __init__(self, pos, model, wood=0):
        super().__init__(pos, model)
        self.tools = 0

    def get_portrayal(self):
        portrayal = {"Shape": "assets/art_full.png" if (self.tools > 0) else "assets/art.png",
                     "h": 1,
                     "w": 1,
                     "Color": "green",
                     "Layer": 2,
                     "Filled": "true"}

        if self.tools > 0:
            portrayal["Color"] = "black"

        return portrayal

    def class_name(self):
        return "Artisan"

    def get_n_tools(self):
        return self.tools

    def receive_wood(self):
        self.tools += 1

    def give_tools(self):
        if self.tools > 0:
            self.tools -= 1
            return True
        else:
            return False