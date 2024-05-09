def decrypt(encrypted_text):
    """Decrypts the given encrypted text using a custom decryption algorithm."""
    length = len(encrypted_text)
    new_decrypt_text_1 = ""
    new_decrypt_text_2 = ""

    # Level three decryption
    for k in range(length - 1, -1, -1):
        ele = list(encrypted_text)
        ele[k], ele[k - 1] = ele[k - 1], ele[k]
        new_decrypt_text_1 += "".join(ele)

    # Level two decryption
    for j in range(length):
        if j < length // 2:
            new_decrypt_text_2 += new_decrypt_text_1[length - 1 - j]
        else:
            new_decrypt_text_2 += new_decrypt_text_1[j - length // 2]

    # Level one decryption
    plain_text = ""
    for i in range(length - 1, -1, -1):
        plain_text += chr(ord(new_decrypt_text_2[i]) + length)

    return plain_text