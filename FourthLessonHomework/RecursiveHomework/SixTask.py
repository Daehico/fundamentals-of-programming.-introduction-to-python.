def can_make_amount(coins, num_coins, target_amount):
    if target_amount == 0 and num_coins == 0:
        return True

    if target_amount == 0:
        return False

    if num_coins == 0:
        return False

    for coin in coins:

        if target_amount - coin >= 0 and can_make_amount(coins, num_coins - 1, target_amount - coin):
            return True
    return False


def main():
    target_amount = int(input("Введите сумму в центах (например, 100 для $1.00): "))
    num_coins = int(input("Введите количество монет: "))

    coins = [1, 5, 10, 25]

    if can_make_amount(coins, num_coins, target_amount):
        print("Сумму можно собрать.")
    else:
        print("Сумму невозможно собрать.")

if __name__ == "__main__":
    main()
