from agents.custom_agent import CustomAgent

class Collector(CustomAgent):
    wood = 0

    def __init__(self, pos, model, wood=0):
        super().__init__(pos, model)
        self.wood = wood

    def get_portrayal(self):
        return {
            "Shape": "assets/collector_full.png" if (self.wood > 10) else "assets/collector.png",
            "h": 1,
            "w": 1,
            "Color": "red" if (self.wood > 10) else "blue",
            "Layer": 2,
            "Filled": "true"
        }

    def class_name(self):
        return "Collector"
