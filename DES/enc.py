import secrets
import numpy as np
import function as func


def main():
    # input
    print("---input plaintext---")
    plaintext = input()
    len_plaintext = len(plaintext)
    print(len_plaintext)
    plaintext += ' ' * (8 - len_plaintext // 8)
    print(plaintext)
    plaintext_ascii = [ord(i) for i in plaintext]
    # keygen
    sub_key_list = func.sub_keygen_enc()
    # enc
    plaintext_binary = func.encode(plaintext_ascii)
    ciphertext = []
    for i in range(0, 64*-(-len_plaintext //8), 64):
        ciphertext.append(func.crypto(plaintext_binary[i:i+64], sub_key_list))

    # output
    print("---ciphertext---")
    for c in ciphertext:
        print("".join(map(str, c)), end="")
    print()

if __name__ == "__main__":
    main()

