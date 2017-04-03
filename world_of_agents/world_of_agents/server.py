from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule

from world_of_agents.agents import Collector, WoodPatch
from world_of_agents.model import CollectorModel


def collector_portrayal(agent):
    if agent is None:
        return

    portrayal = {}

    if type(agent) is Collector:
        portrayal["Shape"] = "collector.png"
        # https://icons8.com/web-app/433/collector
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 1

    elif type(agent) is WoodPatch:
        if agent.fully_grown:

            portrayal["Shape"] = "wood.png"
        else:
            portrayal["Color"] = "#00bb00"
            portrayal["Shape"] = "rect"

        portrayal["Filled"] = "true"
        portrayal["Layer"] = 0
        portrayal["w"] = 1
        portrayal["h"] = 1

    return portrayal

canvas_element = CanvasGrid(collector_portrayal, 20, 20, 500, 500)
# chart_element = ChartModule([{"Label": "Wolves", "Color": "#AA0000"},
#                              {"Label": "Collector", "Color": "#666666"}])

server = ModularServer(CollectorModel, [canvas_element],
                       "WoodCollector", wood=True)
# server.launch()
