PHONETIC_ALPHABET = {
    'A': 'Alpha',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliet',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'Xray',
    'Y': 'Yankee',
    'Z': 'Zulu'
}

def phonetic_alphabet_conversion(string):
    string = string.replace(" ", "").upper()

    if not string:
        return []

    first_char = string[0]
    rest_of_string = string[1:]

    if first_char in PHONETIC_ALPHABET:
        return [PHONETIC_ALPHABET[first_char]] + phonetic_alphabet_conversion(rest_of_string)
    else:
        return [f"'{first_char}' не является буквой англ. алфавита"] + phonetic_alphabet_conversion(rest_of_string)

def main():
    input_string = input("Введите слово: ")
    phonetic_alphabet_string = phonetic_alphabet_conversion(input_string)
    print(phonetic_alphabet_string)


if __name__ == "__main__":
    main()
