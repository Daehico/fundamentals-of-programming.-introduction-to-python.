def euclidean_gcd(a, b):
    if b == 0:
        return a
    else:
        return euclidean_gcd(b, a % b)

def main():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    gcd = euclidean_gcd(num1, num2)
    print("Наибольший общий делитель - ", gcd)

if __name__ == "__main__":
    main()
