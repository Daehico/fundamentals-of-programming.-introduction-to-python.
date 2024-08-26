import math

#Task 1
input_name = input("Ввудите ваше имя: ")
print("Привет, ", input_name)

#Task 2
SOUVENIR_WEIGHT = 75
TRINKET_WEIGHT = 112

souvenir_count = int(input("Введите количество купленых сувениров: "))
trinket_count = int(input("Введите количество купленных безделушек: "))

total_weight = (SOUVENIR_WEIGHT * souvenir_count) + (TRINKET_WEIGHT * trinket_count)
print("Общий вес посылки: ", total_weight)

#Task 3
DEPOSIT_PERCENT = 4
ONE_HUNDRED_PERCENT = 100
TWO_YERS = 2
THREE_YERS = 3

deposit_amount = float(input("Введите сумму депозита: "))
first_year_deposit_ammount = deposit_amount * (1 + DEPOSIT_PERCENT / ONE_HUNDRED_PERCENT)
second_year_deposit_ammount = deposit_amount * (1 + DEPOSIT_PERCENT / ONE_HUNDRED_PERCENT) ** TWO_YERS
third_year_deposit_ammount = deposit_amount * (1 + DEPOSIT_PERCENT / ONE_HUNDRED_PERCENT) ** THREE_YERS

formated_deposit_print = "Сумма депозита после первого года: {:.2f} \nСумма депозита после второго года: {:.2f} \n10Сумма депозита после трех лет: {:.2f}".format(first_year_deposit_ammount, second_year_deposit_ammount, third_year_deposit_ammount)
print(formated_deposit_print)

#Task 4
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))

sum_of_a_and_b = a + b
difference_between_a_and_b = a - b
product_of_a_and_b = a * b
quotient_of_a_divided_by_b = a // b
the_remainder_from_dividing_a_by_b = a % b
decimal_logarithm_of_a = math.log10(a)
the_result_of_raising_a_to_the_power_of_b = a ** b

print("Сумма чисел а и b: ", sum_of_a_and_b,
      "\nРазница между числами а и b: ", difference_between_a_and_b,
      "\nПроизведение между числами а и b: ", product_of_a_and_b,
      "\nЧастное от деления a на b: ", quotient_of_a_divided_by_b,
      "\nОстаток от деления a на b: ",the_remainder_from_dividing_a_by_b,
      "\nДесятичный логарифм числа a: ",decimal_logarithm_of_a,
      "\nРезультат возведения числа a в степень b: ", the_result_of_raising_a_to_the_power_of_b)

#Task 5
change_in_cents = int(input("Введите количество копеек: "))

five_rub = change_in_cents // 500
change_in_cents %= 500
    
two_rub = change_in_cents // 200
change_in_cents %= 200
    
one_rub = change_in_cents // 100
change_in_cents %= 100
    
fifty_cop = change_in_cents // 50
change_in_cents %= 50
    
ten_cop = change_in_cents // 10
change_in_cents %= 10
    
five_cop = change_in_cents // 5
change_in_cents %= 5
    
one_cop = change_in_cents // 1

print("Сдача составлят: \n",
      five_rub," пяти рублевых монет,\n",
      two_rub, " двух рублевых монет, \n",
      one_rub, " однорублевых монет, \n",
      fifty_cop, " пятидесятикопеечных монет, \n",
      ten_cop, " десятикопеечных монет, \n",
      five_cop, " пятикопеечных монет, \n",
      one_cop, " однокопеечных монет.")