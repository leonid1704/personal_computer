from Components.component import Component


class GraphicCard(Component):
    def __init__(self, brand, graphic_type, memory):
        super().__init__(brand)
        self.graphic_type = graphic_type
        self.memory = memory

    def __str__(self):
        return f'{super().__str__()}, {self.graphic_type}, {self.memory}'
