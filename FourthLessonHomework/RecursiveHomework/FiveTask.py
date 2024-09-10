def edit_distance(str1, str2, len1, len2):
    if len1 == 0:
        return len2
    if len2 == 0:
        return len1

    if str1[len1 - 1] == str2[len2 - 1]:
        return edit_distance(str1, str2, len1 - 1, len2 - 1)

    return 1 + min(
        edit_distance(str1, str2, len1, len2 - 1),
        edit_distance(str1, str2, len1 - 1, len2),
        edit_distance(str1, str2, len1 - 1, len2 - 1)
    )

def main():
    str1 = input("Введите первую строку: ").strip()
    str2 = input("Введите вторую строку: ").strip()

    distance = edit_distance(str1, str2, len(str1), len(str2))

    print(f"Редакционное расстояние между '{str1}' и '{str2}' равно {distance}")

if __name__ == "__main__":
    main()