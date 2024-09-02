# # Task 1
# PUPPY_AGE = 2
#
# HUMAN_AGE_TO_PUPPY_AGE = 10.5
# HUMAN_AGE_TO_ADULT_DOG_AGE = 4
#
# human_age = float(input("Введите возраст человека: "))
# dog_age = 0
#
# if human_age > HUMAN_AGE_TO_PUPPY_AGE * PUPPY_AGE:
#     dog_age += (human_age - HUMAN_AGE_TO_PUPPY_AGE * PUPPY_AGE) / HUMAN_AGE_TO_PUPPY_AGE
#     human_age -= HUMAN_AGE_TO_PUPPY_AGE * PUPPY_AGE
#     dog_age += human_age / HUMAN_AGE_TO_ADULT_DOG_AGE
# else:
#     dog_age += human_age / HUMAN_AGE_TO_PUPPY_AGE
#
# print("Ваш возраст в собачих годах: ", dog_age)

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
