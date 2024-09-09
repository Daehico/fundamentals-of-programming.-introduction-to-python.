def checkPasswor(password):
    has_upper = False
    has_lower = False
    has_number = False

    for ch in password:
        if ch >= "A" and ch <= "Z":
            has_upper = True
        elif ch >= "a" and ch <= "z":
            has_lower = True
        elif ch >= 0 and ch <= 9:
            has_number = True
    if len(password) >= 8 and has_upper == True and has_lower == True and has_number == True:
        return True
    else:
        return False


def main():
    password = input("Введите пароль: ")
    if(checkPasswor(password)):
        print("Ваш пароль надежен")
    else:
        print("Ваш пароль не надежен")

if __name__ == "__main__":
    main()