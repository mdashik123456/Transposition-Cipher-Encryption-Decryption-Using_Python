def decode(cipher_text, key):
    
    sorted_key = key.copy()
    sorted_key.sort()
    
    num_columns = len(key)
    # Calculate the number of rows
    num_rows = -(-len(cipher_text) // num_columns)

    cipher_text = [(cipher_text[i:i+num_rows]) for i in range(0, len(cipher_text), num_rows)]
    
    #create dictionary with sorted key and cipher_text
    cipher_text_dict = {}
    for i in range(num_columns):
        cipher_text_dict[sorted_key[i]] = cipher_text[i]
        
    cipher_text_key_sorted = []
        
    for num in key:
        cipher_text_key_sorted.append(cipher_text_dict[num])
        
    plain_text = ""
    # print(cipher_text_key_sorted)
    
    while len(cipher_text_key_sorted[0]) > 0:
        indx = 0
        for strings in cipher_text_key_sorted:
            for char in strings:
                plain_text += char
                strings = strings[1:]
                cipher_text_key_sorted[indx] = strings
                break
            indx += 1
                
    plain_text = plain_text[::-1] #Reverse plain text
    
    alphabets = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    while True:
        if plain_text[0] == alphabets[0]:
            plain_text = plain_text[1:]
            alphabets = alphabets[1:]
        else:
            break
    
    print(f"Your Decrypted Text is: \"{plain_text[::-1]}\"") #Reverse print


# decode("oeneXfniiydlauiinlsZdrarYaitntftovW", [3, 7, 2, 9, 1, 5, 4])
