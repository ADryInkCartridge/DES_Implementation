import secrets
import DES

if __name__ == '__main__':
    
    plaintext = input("Enter plaintext: ")

    print("SINGLE DES\n\n")
    key = secrets.token_hex(8)
    print("Key: ", key)
    ciphertext = DES.DES_Encrypt(plaintext, key)
    print("Ciphertext: ", ciphertext)

    decrypted = DES.DES_Decrypt(ciphertext, key)
    print("Decrypted: ", decrypted)
    print("TRIPLE DES\n\n")

    key1 = secrets.token_hex(8)
    key2 = secrets.token_hex(8)
    key3 = secrets.token_hex(8)

    print("Key1: ", key1)
    print("Key2: ", key2)
    print("Key3: ", key3)

    ciphertext1 = DES.DES_Encrypt(plaintext, key1)
    ciphertext2 = DES.DES_Decrypt(ciphertext1, key2)
    ciphertext3 = DES.DES_Encrypt(ciphertext2, key3)


    decrypted1 = DES.DES_Decrypt(ciphertext3, key3)
    decrypted2 = DES.DES_Encrypt(decrypted1, key2)
    decrypted3 = DES.DES_Decrypt(decrypted2, key1)

    print("Ciphertext1: ", ciphertext1)
    print("Ciphertext2: ", ciphertext2)
    print("Ciphertext3: ", ciphertext3)
    print("Decrypted1: ", decrypted1)
    print("Decrypted2: ", decrypted2)
    print("Decrypted3: ", decrypted3)
    






