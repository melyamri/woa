from agents.active_agent import ActiveAgent
from agents.wood import Wood
from agents.house import House
from agents.mine import Mine

class Builder(ActiveAgent):
    '''
    A sheep that walks around, reproduces (asexually) and gets eaten.

    The init is the same as the CustomAgent.
    '''

    def __init__(self, pos, model, wood=0):
        super().__init__(pos, model)
        self.tools = 0

    def get_portrayal(self):
        portrayal = {"Shape": "assets/builder_full.gif" if (self.tools > 0) else "assets/builder.gif",
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
                if isinstance(obj, Wood) or isinstance(obj, House) or isinstance(obj, Mine):
                    clean_terrain = False
            if clean_terrain:
                (x,y) = self.pos
                self.tools -= 1
                house = House(self.pos,self.model)
                self.model.grid.place_agent(house, (x, y))
                self.model.schedule.add(house)

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