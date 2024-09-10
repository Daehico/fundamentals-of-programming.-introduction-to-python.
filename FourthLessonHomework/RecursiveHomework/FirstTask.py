def number_summation():
    num = input("Введите число (для выхода введите пустую строку):")
    sum = 0
    if num == "":
        return sum
    else:
        sum += float(num) + number_summation()
        return sum

def main():
    sum_of_nums = number_summation()
    print("Сумма введеных чисел - ", sum_of_nums)

if __name__ == "__main__":
    main()
