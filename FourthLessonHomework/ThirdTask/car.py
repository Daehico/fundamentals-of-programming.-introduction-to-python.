class Car:
    ONE_HUNDRED_PERCENT = 100

    def __init__(self, model, color, max_speed, has_gps=True):
        self.model = model
        self.color = color
        self.max_speed = max_speed
        self.has_gps = has_gps
        self.battery_level = 100
        self.is_moving = False

    def move(self):
        if self.battery_level > 0:
            self.is_moving = True
            print(f"{self.model} начинает движение.")
        else:
            print(f"{self.model} не может двигаться. Заряд батареи низкий.")

    def stop(self):
        self.is_moving = False
        print(f"{self.model} остановился.")

    def turn(self, direction):
        if self.is_moving:
            print(f"{self.model} поворачивает {direction}.")
        else:
            print(f"{self.model} не может повернуть, так как он стоит.")

    def update_battery(self, charge):
        self.battery_level += charge
        if self.battery_level > 100:
            self.battery_level = 100
        print(f"Уровень заряда батареи для {self.model}: {self.battery_level}%.")

    def find_route(self, destination):
        if self.has_gps:
            print(f"{self.model} строит маршрут до {destination}.")
        else:
            print(f"{self.model} не может построить маршрут без GPS.")