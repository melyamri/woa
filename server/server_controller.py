from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule, TextElement
from models.world import World
from models.tracer import Tracer

mapsize = 10
ncollectors = 1
nartisans = 1
nbuilders = 1
nmines = 3
def collector_portrayal(agent):
    if agent is None:
        return

    return agent.get_portrayal()


canvas_element = CanvasGrid(collector_portrayal, mapsize, mapsize, 600, 600)

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
                       iron=True,
                       height=mapsize,
                       width=mapsize,
                       nmines=nmines,
                       initial_collector=ncollectors,
                       initial_artisans=nartisans,
                       initial_builders=nbuilders,
                       wood_regrowth_time=1000)
