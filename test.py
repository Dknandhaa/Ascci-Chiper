import encrypt
import decrypt

plain_text = input()
encrypted_text = encrypt.encrypt(plain_text)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt.decrypt(encrypted_text)
print("Decrypted text:", decrypted_text)