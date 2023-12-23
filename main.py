class Car:
    def __init__(self, motor = '8v', tank_capacity = 24, leigth = 240, place = 5):
        self.motor = motor
        self.tank_capacity = tank_capacity
        self.leight = leigth
        self.place = place


class Bus(Car):
    def __init__(self):
        super().__init__()
        self.tank_capacity = 48
        self.leight = 330
        self.place = 20

    def __str__(self):
        return f"Об'єм баку-{self.tank_capacity}\nДовжина-{self.leight}\nМотор-{self.motor}\nМісць-{self.place}"

bus = Bus()
print(bus)
