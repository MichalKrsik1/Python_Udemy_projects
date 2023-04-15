ALPHABET_START = 97
ALPHABET_END = 123
ALPHABET_LENGTH = 26


def create_alphabet():
    return list(map(chr, range(ALPHABET_START, ALPHABET_END)))


def check_shift(shift):
    if shift < 0 or shift > 25:
        raise ValueError("Incorrect shift value")


def shift_letter(letter, alphabet, shift):
    return alphabet[alphabet.index(letter) - (ALPHABET_LENGTH - shift)]


def process_vigenere(message, key, alphabet, operation):
    result = ""
    index = 0
    key = (key * (len(message) // len(key) + 1))[:len(message)]

    for letter in message:
        shift = alphabet.index(key[index])
        if operation == "decipher":
            shift = ALPHABET_LENGTH - shift
        result += shift_letter(letter, alphabet, shift)
        index += 1

    return result


def cipher_caesar(message, shift):
    message = message.lower()
    alphabet = create_alphabet()
    check_shift(shift)
    return ''.join(shift_letter(letter, alphabet, shift) for letter in message)


def decipher_caesar(message, shift):
    return cipher_caesar(message, 26 - shift)


def cipher_vigenere(message, key):
    message = message.lower()
    key = key.lower()
    alphabet = create_alphabet()
    return process_vigenere(message, key, alphabet, "cipher")


def decipher_vigenere(message, key):
    message = message.lower()
    key = key.lower()
    alphabet = create_alphabet()
    return process_vigenere(message, key, alphabet, "decipher")


def cipher_vernam(message, key):
    message = message.upper()
    key = key.upper()

    if len(message) != len(key):
        raise ValueError("Message and key length do not match")

    result = []
    for i, letter in enumerate(message):
        xor = (ord(letter) - ALPHABET_START) ^ (ord(key[i]) - ALPHABET_START)
        result.append(chr(ALPHABET_START + (xor % ALPHABET_LENGTH)))

    return ''.join(result)


def decipher_vernam(message, key):
    return cipher_vernam(message, key)
