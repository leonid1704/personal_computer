from Components.component import Component


class RAM(Component):
    def __init__(self, brand, memory_type, capacity):
        super().__init__(brand)
        self.memory_type = memory_type
        self.capacity = capacity

    def __str__(self):
        return f'Оператива {super().__str__()}, {self.capacity}'
