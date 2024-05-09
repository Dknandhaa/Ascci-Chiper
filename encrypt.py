def encrypt(plain_text):
    """Encrypts the given plain text using a custom encryption algorithm."""
    length = len(plain_text)
    encrypt_text = ""
    new_encrypt_text_1 = ""
    new_encrypt_text_2 = ""

    # Level one encryption
    for i in range(length - 1, -1, -1):
        encrypt_text += chr(ord(plain_text[i]) - length)

    # Level two encryption
    for j in range(length):
        if j < length // 2:
            new_encrypt_text_1 += encrypt_text[length - 1 - j]
        else:
            new_encrypt_text_1 += encrypt_text[j - length // 2]

    # Level three encryption
    for k in range(length-1):
        ele = list(new_encrypt_text_1)
        ele[k], ele[k + 1] = ele[k + 1], ele[k]
        new_encrypt_text_2 += "".join(ele)

    return new_encrypt_text_2