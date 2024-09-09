class Car(object):
    Name_class = "Автомобиль"

    def __int__(self, brand, weight, power):
        self.brand = brand
        self.weight = weight
        self.power = power

    def drive(self):
        print("Двигаемся прямо")

    def right(self):
        print("Двигаемся вправо")

    def left(self):
        print("Двигаемся влево")