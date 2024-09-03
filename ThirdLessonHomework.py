# Task 1
PUPPY_AGE = 2

HUMAN_AGE_TO_PUPPY_AGE = 10.5
HUMAN_AGE_TO_ADULT_DOG_AGE = 4

human_age = float(input("Введите возраст человека: "))
dog_age = 0

if human_age > HUMAN_AGE_TO_PUPPY_AGE * PUPPY_AGE:
    dog_age += (human_age - HUMAN_AGE_TO_PUPPY_AGE * PUPPY_AGE) / HUMAN_AGE_TO_PUPPY_AGE
    human_age -= HUMAN_AGE_TO_PUPPY_AGE * PUPPY_AGE
    dog_age += human_age / HUMAN_AGE_TO_ADULT_DOG_AGE
else:
    dog_age += human_age / HUMAN_AGE_TO_PUPPY_AGE

print("Ваш возраст в собачих годах: ", dog_age)

# Task 2
cell_input = input("Введите кординаты клетки: ")
column = cell_input[0].lower()
row = int(cell_input[1])
column_value = ord(column) - ord('a') + 1
cell_sum = column_value + row

if cell_sum % 2 == 0:
    print("Клетка ", cell_input," - черная")
else:
    print("Клетка ", cell_input," - белая")

# Task 3
MIN_VALUE = 1
MAX_VALUE = 101

for number in range(MIN_VALUE, MAX_VALUE):
    str = ''
    if number % 3 == 0:
        str += 'Fizz '
    if number % 5 == 0:
        str += "Buzz"
    if str == '':
        str = number
    print(str,)

# Task 4
input_word = input("Введите слово (для выхода введите пустую строку): ")
words = []

while input_word != "":
    if input_word not in words:
        words.append(input_word)
    input_word = input("Введите слово (для выхода введите пустую строку): ")

for word in words:
    print(word)

# Task 5
number = float(input("Введите число (для выхода введите пустую строку): "))
nums = []

numbers_less_than_the_average = []
numbers_greater_than_the_average = []
numbers_equal_to_the_mean = []

while number != "":
    nums.append(number)
    number = input("Введите число (для выхода введите пустую строку): ")
    if number != "":
        number = float(number)

average = sum(nums) / len(nums)

for num in nums:
    if num > average:
        numbers_greater_than_the_average.append(num)
    elif num == average:
        numbers_equal_to_the_mean.append(num)
    else:
        numbers_less_than_the_average.append(num)

print("Среднее значение: ", average)
print("Список чисел ниже среднего значения: ", numbers_less_than_the_average, end=" ")
if len(numbers_equal_to_the_mean) != 0:
    print("Список чисел равный среднему значению: ", numbers_equal_to_the_mean, end=" ")
print("Список чисел выше среднего значения: ", numbers_greater_than_the_average, end=" ")

#Task 6
number_input = int(input("Введите число, до которого нужно вывести простые числа: "))

prime_numbers = list(range(number_input + 1))
prime_numbers[1] = 0

for number in prime_numbers:
    if number > 1:
        for j in range(2 * number, len(prime_numbers), number):
            prime_numbers[j] = 0

for prime_number in prime_numbers:
    if prime_number != 0:
        print(prime_number, end=" ")

# Task 7
points = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1,
    'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
    'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1,
    'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
    'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4,
    'Z': 10
}

word = input("Введите слово: ")
score = 0

for letter in word.upper():
    if letter in points:
        score += points[letter]

print("Ваш счет:", score)
