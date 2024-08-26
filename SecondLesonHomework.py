#Task 6
LOAF_PRICE = 49
DISCOUNT = 60
ONE_HUNDRED_PERCENT = 100

loaf_count = int(input("Введите количество купленых буханок хлеба: "))
one_loaf_with_discount = LOAF_PRICE - (LOAF_PRICE / ONE_HUNDRED_PERCENT * DISCOUNT)
total_loaf_price_with_discount = one_loaf_with_discount * loaf_count

formated_price = "Цена одной буханки составляет: {}.\nЦена со скидкой составляет: {:.2f}.\nОбщая стоимость составляет: {:.2f}".format(LOAF_PRICE,one_loaf_with_discount, total_loaf_price_with_discount)