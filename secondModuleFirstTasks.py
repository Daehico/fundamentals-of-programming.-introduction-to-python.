#Task 1
smallBottlesCost = 0.10
bigBottlesCost = 0.25

smallBottlesCount = int(input("Введите количество бутылок объемом 1 литр и меньше : "))
bigBottlesCount = int(input("Введите количество бутылок объемом больше 1 литра: "))

totalSmallBottlesCost = smallBottlesCost * smallBottlesCount
totalBigBottlesCost = bigBottlesCost * bigBottlesCount

sum = totalSmallBottlesCost + totalBigBottlesCost

formatedSum = "${:.2f}".format(sum)
print("За сдачу стелотары вы получите" ,formatedSum)

#Task 2
number = int(input("Введите положительное число: "))

sumOfPositiveIntegers = number * (number + 1) / 2

print("Сумма первых ",number," положительных чисел равна ", sumOfPositiveIntegers)