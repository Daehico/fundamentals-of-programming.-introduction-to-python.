from random import randint

# Task 1
SHORTEST = 7
LONGEST = 10
MIN_ASCII = 36
MAX_ASCII = 126

def randomPassword():
    randomLength = randint(SHORTEST, LONGEST)
    result = ""
    for i in range(randomLength):
        randomChar = chr(randint(MIN_ASCII, MAX_ASCII))
        result += randomChar

    return result

def main():
    print("Ващ случайный пароль:", randomPassword())

if __name__ == "__main__":
    main()