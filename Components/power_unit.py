from Components.component import Component


class PowerUnit(Component):
    def __init__(self, brand, capacity):
        super().__init__(brand)
        self.capacity = capacity

    def __str__(self):
        return f'{super().__str__()}, {self.capacity}'
