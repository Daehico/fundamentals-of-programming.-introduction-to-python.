HEX_CHARACTERS = "0123456789ABCDEF"
SIXTEEN_NUMBER = 16
FIFTEEN_NUMBER = 15
ZERO = 0

def hex2int(character):
    if character in HEX_CHARACTERS:
        number = int(character, SIXTEEN_NUMBER)
        return number
    else:
        print("Ошибка: введенный символ не является допустимым шестнадцатеричным символом.")

def int2hex(number):
    if ZERO <= number <= FIFTEEN_NUMBER:
        return format(number, 'X')
    else:
        print("Ошибка: введенное число должно быть в диапазоне от 0 до 15.")

def main():
    input_string = str(input("Введите один символ: ")).upper()
    if len(input_string) != 1:
        print("Вы ввели больше одного символа!")
    else:
        number = hex2int(input_string)
        character = int2hex(number)
        print("Оригинальная буква: ", input_string)
        print("Число ", number)
        print("Буква: ", character)

if __name__ == "__main__":
    main()