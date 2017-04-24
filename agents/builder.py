from agents.custom_agent import CustomAgent
from agents.wood import Wood
from agents.house import House

class Builder(CustomAgent):
    '''
    A sheep that walks around, reproduces (asexually) and gets eaten.

    The init is the same as the CustomAgent.
    '''

    def __init__(self, pos, model, wood=0):
        super().__init__(pos, model)
        self.tools = 0

    def get_portrayal(self):
        portrayal = {"Shape": "assets/build_full.png" if (self.tools > 0) else "assets/build.png",
                     "h": 1,
                     "w": 1,
                     "Color": "#aa6633",
                     "Layer": 2,
                     "Filled": "true"}

        if self.tools > 0:
            portrayal["Color"] = "#ff00ff"

        return portrayal


    def build_house(self):
        if self.tools > 0:
            clean_terrain = True
            contents = self.model.grid.get_cell_list_contents(self.pos)
            for obj in contents:
                if isinstance(obj, Wood):
                    clean_terrain = False
            if clean_terrain:
                (x,y) = self.pos
                self.tools -= 1
                house = House(self.pos,self.model)
                self.model.grid.place_agent(house, (x, y))

    def class_name(self):
        return "Builder"

    def get_n_tools(self):
        return self.tools

    def receive_tools(self):
        self.tools += 1

    def is_terrain_buildable(self):
        clean_terrain = True
        contents = self.model.grid.get_cell_list_contents(self.pos)
        for obj in contents:
            if isinstance(obj, Wood):
                clean_terrain = False
        return clean_terrain