from agents.active_agent import ActiveAgent

class Artisan(ActiveAgent):
    '''
    A sheep that walks around, reproduces (asexually) and gets eaten.

    The init is the same as the CustomAgent.
    '''

    def __init__(self, pos, model, wood=0):
        super().__init__(pos, model)
        self.tools = 0

    def get_portrayal(self):
        portrayal = {"Shape": "assets/artusan_full.gif" if (self.tools > 0) else "assets/artisan.gif",
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

    def receive_materials(self):
        self.tools += 1

    def give_tools(self):
        if self.tools > 0:
            self.tools -= 1
            return True
        else:
            return False