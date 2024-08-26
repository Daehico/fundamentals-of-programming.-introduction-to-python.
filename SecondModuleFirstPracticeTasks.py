#Task 1
small_bottles_cost = 0.10
big_bottles_cost = 0.25

small_bottles_count = int(input("Введите количество бутылок объемом 1 литр и меньше : "))
big_bottles_count = int(input("Введите количество бутылок объемом больше 1 литра: "))

total_small_bottles_cost = small_bottles_cost * small_bottles_count
total_big_bottles_cost = big_bottles_cost * big_bottles_count

sum = total_small_bottles_cost + total_big_bottles_cost

formated_sum = "${:.2f}".format(sum)
print("За сдачу стеклотары вы получите" ,formated_sum)

#Task 2
number = int(input("Введите положительное число: "))

sum_of_positive_integers = number * (number + 1) / 2

print("Сумма первых ",number," положительных чисел равна ", sum_of_positive_integers)

#Task 3
s = int(input("Введите длинну стороны: "))
n = int(input("Введите количество сторон: "))

regular_polygon_area = (n * s**2) / (4 * math.tan(math.pi/n))

print("Площадь правильного многоугольника: ", regular_polygon_area)

#Task 4
seconds_per_day = 86400
seconds_per_hour = 3600
seconds_per_minute = 60

seconds_input = int(input("Введите количество секунд: "))

days = seconds_input // seconds_per_day
hours = (seconds_input % seconds_per_day) // seconds_per_hour
minutes = (seconds_input % seconds_per_hour) // seconds_per_minute
seconds = seconds_input % seconds_per_minute

formated_time = "{}d {}:{:.0f}:{:.0f}".format(days,hours,minutes,seconds)
print(formated_time)