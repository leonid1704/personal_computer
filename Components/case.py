from Components.component import Component


class Case(Component):
    def __init__(self, brand, motherboard, graphic_card, drive, power_unit):
        super().__init__(brand)
        self.motherboard = motherboard
        self.graphic_card = graphic_card
        self.drive = drive
        self.power_unit = power_unit

    def __str__(self):
        return f'{super().__str__()}, {self.motherboard}, {self.graphic_card}, {self.drive}, {self.power_unit}'
