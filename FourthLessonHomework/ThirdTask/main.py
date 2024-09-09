from car import Car

def main():
    my_car = Car(model="Tesla Model X", color="White", max_speed=250)

    print("Добро пожааловать в программу управления беспилотным автомобилем! \n Справка по ситеме управления: "
          "\n1.Двигаться"
          "\n2.Остановиться"
          "\n3.Повернуть"
          "\n4.Зарядить батарею"
          "\n5.Построить маршрут"
          "\n6.Выйти из программы")

    menu_item = input("Введите пункт меню: ")

    while menu_item != "6":
        if menu_item == "1":
            my_car.move()
        elif menu_item == "2":
            my_car.stop()
        elif menu_item == "3":
            direction = input("Введите направление: ")
            my_car.turn(direction)
        elif menu_item == "4":
            charge = int(input("Введите уровень заряда: "))
            my_car.update_battery(charge)
        elif menu_item == "5":
            destination = input("Введите точку маршрута: ")
            my_car.find_route(destination)
        else:
            print("Такого пункта не существует")

        menu_item = input("Введите пункт меню: ")

if __name__ == "__main__":
    main()