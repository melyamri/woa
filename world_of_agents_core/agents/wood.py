import random

from world_of_agents_core.agents.custom_agent import CustomAgent

class WoodResource(CustomAgent):
    '''
    A patch of wood that grows at a fixed rate and it is collected by the collector
    '''

    def __init__(self, pos, model, fully_grown, countdown):
        '''
        Creates a new patch of wood

        Args:
            grown: (boolean) Whether the patch of wood is fully grown or not
            countdown: Time for the patch of wood to be fully grown again
        '''
        super().__init__(pos, model)
        self.fully_grown = fully_grown
        self.countdown = countdown
        self.spread_chance = [False,False,False,False,False,False,False,False]

    def step(self):
        if not self.fully_grown:
            if self.countdown <= 0:
                # Set as fully grown
                self.fully_grown = True
                self.countdown = self.model.wood_regrowth_time
                self.spread_chance = [False, False, False, False, False, False, False, False]
            else:
                self.countdown -= 1
        else:
            spread = random.choice(self.spread_chance)
            if (spread):
                self.spread_chance = [False, False, False, False, False, False, False, False]
                print('Agent ', self.pos, ' is trying to spread')
                spread_target = random.choice(self.model.grid.get_neighborhood(self.pos, self.moore, True))
                this_cell = self.model.grid.get_cell_list_contents(spread_target)
                theres_wood = False
                for obj in this_cell:
                    if isinstance(obj, WoodResource):
                        theres_wood = True
                if not (theres_wood):
                    patch = WoodResource(spread_target, self, False, self.model.wood_regrowth_time)
                    print('Agent ',self.pos,' is spreading into',spread_target)
                    self.model.grid.place_agent(patch, spread_target)
                    self.model.schedule.add(patch)
                else:
                    print('There\'s already wood in', spread_target)
            else:
                self.spread_chance.append(random.choice([True,False]))

    def get_portrayal(self):

        portrayal = {"Shape": "circle",
                     "r": 1,
                     "Color": "green",
                     "Layer": 1,
                     "Filled": "true"}

        if self.fully_grown:
            portrayal["r"] = "1"
        else:

            portrayal["r"] = "0.31"

        return portrayal