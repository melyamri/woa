from agents.custom_agent import CustomAgent

class Collector(CustomAgent):
    wood = 0
    iron = 0

    def __init__(self, pos, model):
        super().__init__(pos, model)
        self.wood = 0
        self.iron = 0

    def get_portrayal(self):
        return {
            "Shape": "assets/coll_full.png" if (self.wood > 0) else "assets/coll.png",
            "h": 1,
            "w": 1,
            "Color": "red" if (self.wood > 10) else "blue",
            "Layer": 2,
            "Filled": "true"
        }

    def class_name(self):
        return "Collector"

    def check_wood(self):
        return self.wood

    def give_wood(self):
        if self.wood > 0:
            self.wood -= 1
            return True
        else:
            return False

    def check_iron(self):
        return self.iron


    def give_iron(self):
        if self.iron >0:
            self.iron -=1
            return True
        else:
            return False