ROMAN_NUMERALS = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def roman_to_decimal(roman):
    if not roman:
        return 0

    first_char = roman[0]
    first_value = ROMAN_NUMERALS[first_char]

    if len(roman) > 1:
        second_char = roman[1]
        second_value = ROMAN_NUMERALS[second_char]

        if first_value < second_value:
            return -first_value + roman_to_decimal(roman[1:])
        else:
            return first_value + roman_to_decimal(roman[1:])
    else:
        return first_value

def main():
    roman_input = input("Введите римское число: ").strip().upper()
    decimal_output = roman_to_decimal(roman_input)
    print(f"Десятичное значение: {decimal_output}")

if __name__ == "__main__":
    main()
