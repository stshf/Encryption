import secrets
import numpy as np
import function as func

def main():
    # input
    print("---input plaintext---")
    plaintext = input()
    len_plaintext = len(plaintext)
    # ZeroBytePadding
    plaintext += '\0' * (8 - len_plaintext // 8)
    plaintext_ascii = [ord(i) for i in plaintext]
    # keygen
    key1, key2, key3 = func.keygen(), func.keygen(), func.keygen()
    key1 = func.encode(key1)
    key2 = func.encode(key2)
    key3 = func.encode(key3)

    sub_key2 = func.sub_keygen_enc(key2)
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
        ciphertext.append(func.desx(plaintext_binary[i:i+64], key1, sub_key2, key3))

    # output
    print("---ciphertext---")
    for c in ciphertext:
        print("".join(map(str, c)), end="")
    print()

if __name__ == "__main__":
    main()

