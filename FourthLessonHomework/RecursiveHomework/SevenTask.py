def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):  # Если элемент является списком
            result.extend(flatten(item))  # Рекursivelyflatten it and extend the result
        else:
            result.append(item)  # Если элемент не список, добавляем его в результат
    return result

def main():
    nested_example = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
    flattened_example = flatten(nested_example)
    nested_example2 = [1, [2, 3, 4], [4, [5, [6, 7, 9]]], [[[8], 9], [10]]]
    flattened_example2 = flatten(nested_example2)

    print("Выровненный список:", flattened_example)
    print("Второй выровненный список: ", flattened_example2)

if __name__ == "__main__":
    main()