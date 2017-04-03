import random

from mesa import Agent

from world_of_agents.custom_agent import CustomAgent


class Collector(CustomAgent):
    '''
    A sheep that walks around, reproduces (asexually) and gets eaten.

    The init is the same as the CustomAgent.
    '''

    wood = 0

    def __init__(self, pos, model, moore, wood=0):
        super().__init__(pos, model, moore=moore)
        self.wood = wood

    def step(self):
        '''
        A model step. Move, collect wood if there is any.
        '''
        self.random_move()
        living = True

        if self.model.wood:

            # If there is wood available, take it
            this_cell = self.model.grid.get_cell_list_contents([self.pos])
            wood_patch = [obj for obj in this_cell
                           if isinstance(obj, WoodPatch)][0]
            if wood_patch.fully_grown:
                self.wood += 1
                wood_patch.fully_grown = False






class WoodPatch(Agent):
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

    def step(self):
        if not self.fully_grown:
            if self.countdown <= 0:
                # Set as fully grown
                self.fully_grown = True
                self.countdown = self.model.wood_regrowth_time
            else:
                self.countdown -= 1
