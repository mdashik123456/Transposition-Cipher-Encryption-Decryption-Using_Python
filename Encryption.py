import math

global alphabets
alphabets = ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']


def encode(plaintext, key):

    key_len = len(key)
# ---------------------------------------------------------------
# From here Add extra Char from alphabets for fill the empty cells
    total_characters = len(plaintext)
    num_rows = math.ceil(total_characters / key_len)

    if num_rows * key_len != total_characters:
        deff = (num_rows * key_len) - total_characters
        for i in range(deff - 1, -1, -1):
            plaintext += alphabets[i]
    # ---------------------------------------------------------------

    # ---------------------------------------------------------------
    # Seperate string by column
    ciphertext_list = ['']*key_len

    for column in range(key_len):
        pointer = column

        while pointer < len(plaintext):
            ciphertext_list[column] += plaintext[pointer]
            pointer += key_len

    # print(ciphertext_list)

    # ---------------------------------------------------------------

    # Create a dictionary using two list
    ciphered_dict = {}
    for i in range(key_len):
        ciphered_dict[key[i]] = ciphertext_list[i]
    # print(ciphered_dict)

    # sort key
    sorted_key = key.copy()
    sorted_key.sort()

    # Create Encrypted String
    ciphertext = ""
    for i in sorted_key:
        ciphertext += ciphered_dict[i]

    print(f"Encrypted Text is: {ciphertext}")
