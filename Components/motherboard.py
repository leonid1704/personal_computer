from Components.cpu import CPU
from Components.component import Component


class Motherboard(Component):
    def __init__(self, brand, cpu, form_factor, ram, quantity_ram):
        super().__init__(brand)
        self.cpu = cpu
        self.form_factor = form_factor
        self.ram = ram
        self.quantity_ram = quantity_ram

    def __str__(self):
        return f'{super().__str__()}, {self.cpu}, {self.ram}'
