from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule, TextElement

from agents.collector import Collector
from agents.wood import Wood
from models.world import World
from models.tracer import Tracer

mapsize = 20
ncollectors = 5
nartisans = 3
nbuilders = 2

def collector_portrayal(agent):
    if agent is None:
        return

    return agent.get_portrayal()


canvas_element = CanvasGrid(collector_portrayal, mapsize, mapsize, 600, 600)
#chart_element = ChartModule([{"Label": "Wood", "Color": "#AA0000"},
#                              {"Label": "Collector", "Color": "#666666"}])

tracer = Tracer("log")

chart = ChartModule([{"Label": "Wood", "Color": "green"},
                      {"Label": "Collectors", "Color": "blue"},
                      {"Label": "Artisans", "Color": "red"},
                      {"Label": "Builders", "Color": "yellow"},
                      {"Label": "Houses", "Color": "black"}],
                        data_collector_name='datacollector')

server = ModularServer(World, [canvas_element, tracer, chart],
                       "",
                       wood=True,
                       height=mapsize,
                       width=mapsize,
                       initial_collector=ncollectors,
                       initial_artisans=nartisans,
                       initial_builders=nbuilders,
                       wood_regrowth_time=1000)
