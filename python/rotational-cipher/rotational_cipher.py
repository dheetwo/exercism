def rotate(text, key):
    text_ascii_values = [ord(item) for item in text]
    # print(text_ascii_values)
    ciphertext_ascii_values = []
    for item in text_ascii_values:
        if 65 <= item <= 90:  # A - Z
            value = item + key
            if value > 90:
                value -= 26
            ciphertext_ascii_values.append(value)
        elif 97 <= item <= 122:  # a - z
            value = item + key
            if value > 122:
                value -= 26
            ciphertext_ascii_values.append(value)
        else:
            ciphertext_ascii_values.append(item)
    print(ciphertext_ascii_values)
    ciphertext = [chr(item) for item in ciphertext_ascii_values]
    return ''.join(ciphertext)
