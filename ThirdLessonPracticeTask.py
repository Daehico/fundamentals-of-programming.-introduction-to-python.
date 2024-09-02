import random

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

#Task 2
entered_numbers = []

user_input = int(input("Введите числа для добавления в список: (для выхода введите 0): "))

while user_input != 0:
    entered_numbers.append(user_input)
    user_input = int(input("Введите числа для добавления в список: (для выхода введите 0): "))

entered_numbers.sort()
print(entered_numbers)

#Task 3
MIN_NUMBER = 1
MAX_NUMBER = 49
MAX_LOTTERY_NUMBERS = 6

ticket_numbers = set()
i = 0

while len(ticket_numbers) < MAX_LOTTERY_NUMBERS:
    ticket_numbers.add(random.randrange(MIN_NUMBER, MAX_NUMBER + 1))
    i += 1

ticket_numbers = sorted(ticket_numbers)

print("Номер лотерейного биллета: ", end=" ")

for ticket_number in ticket_numbers:
    print(ticket_number, end=" ")
