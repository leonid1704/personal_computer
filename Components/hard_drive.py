from Components.component import Component


class HardDrive(Component):
    def __init__(self, brand, capacity):
        super().__init__(brand)
        self.capacity = capacity

    def __str__(self):
        return f'{super().__str__()}, {self.capacity}'


class HDD(HardDrive):
    def __init__(self, brand, capacity, rotational_speed):
        super().__init__(brand, capacity)
        self.rotational_speed = rotational_speed

    def __str__(self):
        return super().__str__()


class SSD(HardDrive):
    def __init__(self, brand, capacity, read_speed, write_speed):
        super().__init__(brand, capacity)
        self.read_speed = read_speed
        self.write_speed = write_speed

    def __str__(self):
        return super().__str__()
