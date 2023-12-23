class Car:
    def __init__(self, motor):
        self.motor = motor


class Bus(Car):
    def __init__(self, motor, tank_capacity, leigth, place):
        super().__init__(motor)
        self.leight = leigth
        self.place = place
        self.tank_capacity = tank_capacity
        self. place = place

    def __str__(self):
        return print(f"Об'єм баку {self.tank_capacity}\nДовжина {self.leight}\n Мотор {self.motor}\nМісць {self.place}")
