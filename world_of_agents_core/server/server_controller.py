from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule

from world_of_agents_core.agents.collector import Collector
from world_of_agents_core.agents.wood import WoodResource
from world_of_agents_core.model.collector_model import CollectorModel

mapsize = 40
ncollectors = 5

def collector_portrayal(agent):
    if agent is None:
        return

    return agent.get_portrayal()


canvas_element = CanvasGrid(collector_portrayal, mapsize, mapsize, 600, 600)
#chart_element = ChartModule([{"Label": "WoodResource", "Color": "#AA0000"},
#                              {"Label": "Collector", "Color": "#666666"}])


server = ModularServer(CollectorModel, [canvas_element],
                       "WoodCollector",
                       wood=True,
                       height=mapsize,
                       width=mapsize,
                       initial_collector=ncollectors,
                       collector_reproduce=0.04,
                       wood_regrowth_time=1000)
