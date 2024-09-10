def decode(encoded_list):
    def recursive_decode(index):
        if index >= len(encoded_list):
            return []

        current_element = encoded_list[index]
        count = encoded_list[index + 1]

        return [current_element] * count + recursive_decode(index + 2)

    return recursive_decode(0)


def main():
    encoded_list = ["A", 12, "B", 4, "A", 6, "B", 1]
    decoded_list = decode(encoded_list)
    print(
        decoded_list)

if __name__ == "__main__":
    main()
