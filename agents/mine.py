from agents.inert_agent import InertAgent

class Mine(InertAgent):
    '''Mina que da recursos, una vez se recogen todos los que puede generar, desaparece'''


    empty = False

    def __init__(self, pos, model, empty):
        '''Creamos una nueva mina

        Args:
            empty: (boolean) Si la mina esta llena, empty = false
        '''
        super().__init__(pos, model)
        self.empty = empty
        self.resources = 100

    def get_portrayal(self):
        return {
            "Shape": "assets/mine.gif" if not self.empty else "assets/mine.gif",
            "Color": "green",
            "Layer": 1,
            "Filled": "true",
            "r" : "1"
        }

    def class_name(self):
        return "Mine"
