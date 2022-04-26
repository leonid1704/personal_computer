from Components.component import Component


class CPU(Component):
    def __init__(self, brand, socket, model, frequency):
        super().__init__(brand)
        self.socket = socket
        self.model = model
        self.frequency = frequency

    def __str__(self):
        return f'Процессор {super().__str__()}, {self.model}'

