import random

MIN_NUMBER = 0
MAX_NUMBER = 101
FIFTY_PERCENT = 50
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
OLD_NUMBER_CHARACTERS_COUNT = 3
OLD_NUMBER_DIGITS_COUNT = 3
NEW_NUMBER_CHARACTERS_COUNT = 4
NEW_NUMBER_DIGITS_COUNT = 4

def checkFormat():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    if number <= FIFTY_PERCENT:
        return True
    else:
        return False

def generateCarNumber(characters_count, digits_count):
    car_number = []
    car_number += random.choices(UPCASE_CHARACTERS, k=characters_count)
    car_number += random.choices(DIGITS, k=digits_count)
    car_number = str(car_number)
    return car_number

def main():
    is_old_format = checkFormat()
    car_number = ""
    if is_old_format:
       car_number = generateCarNumber(OLD_NUMBER_CHARACTERS_COUNT, OLD_NUMBER_DIGITS_COUNT)
    else:
        car_number = generateCarNumber(NEW_NUMBER_CHARACTERS_COUNT, NEW_NUMBER_DIGITS_COUNT)
    print("Номер машины: ", car_number)


if __name__ == "__main__":
    main()