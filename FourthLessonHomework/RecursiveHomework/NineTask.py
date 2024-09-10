def encode(sequence):
    def recursive_encode(index):
        if index >= len(sequence):
            return []

        current_element = sequence[index]
        count = 1

        while index + 1 < len(sequence) and sequence[index + 1] == current_element:
            count += 1
            index += 1

        return [current_element, count] + recursive_encode(index + 1)

    return recursive_encode(0)


def main():
    user_input = input("Введите строку для кодирования: ")
    encoded_list = encode(user_input)
    print("Закодированный список:", encoded_list)

if __name__ == "__main__":
    main()
