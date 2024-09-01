# Task 1
BABY_LIMIT = 2
CHILD_LIMIT = 12
ADULT_LIMIT = 64

BABY_PRICE = 0.0
CHILD_PRICE = 140
ADULT_PRICE = 230
SENIOR_PRICE = 180

total_price = 0
line = input("Введите возвраст посетителя (пустая строка для выхода: ")
while line != "":
    age = float(line)
    if age <= BABY_LIMIT:
        total_price += BABY_PRICE
    elif age <= CHILD_LIMIT:
        total_price += CHILD_PRICE
    elif age <= ADULT_LIMIT:
        total_price += ADULT_PRICE
    else:
        total_price += SENIOR_PRICE

    line = input("Введите возвраст посетителя (пустая строка для выхода: ")

print("Итоговая цена: ", total_price)
