from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule

from agents.collector import Collector
from agents.wood import Wood
from models.world import World

mapsize = 20
ncollectors = 1
nartisans = 1

def collector_portrayal(agent):
    if agent is None:
        return

    return agent.get_portrayal()


canvas_element = CanvasGrid(collector_portrayal, mapsize, mapsize, 500, 500)
#chart_element = ChartModule([{"Label": "Wood", "Color": "#AA0000"},
#                              {"Label": "Collector", "Color": "#666666"}])


server = ModularServer(World, [canvas_element],
                       "WoodCollector",
                       wood=True,
                       height=mapsize,
                       width=mapsize,
                       initial_collector=ncollectors,
                       initial_artisans=nartisans,
                       wood_regrowth_time=1000)
