import secrets
import numpy as np
import function as func

def main():
    # input
    print("---input plaintext---")
    plaintext = input()
    len_plaintext = len(plaintext)
    plaintext += ' ' * (8 - len_plaintext // 8)
    plaintext_ascii = [ord(i) for i in plaintext]
    # keygen
    key1, key2, key3 = func.keygen(), func.keygen(), func.keygen()
    key1 = func.encode(key1)
    key2 = func.encode(key2)
    key3 = func.encode(key3)

    sub_key1 = func.sub_keygen_enc(key1)
    sub_key2 = func.sub_keygen_enc(key2)
    sub_key3 = func.sub_keygen_enc(key3)
    print("---secret key1---")
    print("".join(map(str, key1)))
    print("---secret key2---")
    print("".join(map(str, key2)))
    print("---secret key3---")
    print("".join(map(str, key3)))
    # enc
    plaintext_binary = func.encode(plaintext_ascii)
    ciphertext = []
    for i in range(0, 64*-(-len_plaintext //8), 64):
        # enc (m, sub_key1)
        cipher1 = func.des(plaintext_binary[i:i+64], sub_key1)
        # dec (cipher1, sub_key2)
        cipher2 = func.des(cipher1, sub_key2)
        # enc (cipher2, sub_key1)
        cipher3 = func.des(cipher2, sub_key3)
        ciphertext.append(cipher3)

    # output
    print("---ciphertext---")
    for c in ciphertext:
        print("".join(map(str, c)), end="")
    print()

if __name__ == "__main__":
    main()

