import numpy as np
import function as func

def main():
    # input
    print("---input secret key1---")
    key1 = list(map(int, input()))
    print("---input secret key2---")
    key2 = list(map(int, input()))
    print("---input secret key3---")
    key3 = list(map(int, input()))
    print("---input ciphertext---")
    ciphertext = list(map(int, input()))
    sub_key2 = func.sub_keygen_dec(key2)
    len_ciphertext = len(ciphertext)

    # dec
    plaintext_binary = []
    for i in range(0, len_ciphertext, 64):
       plaintext_binary.append(func.desx(ciphertext[i:i+64], key3, sub_key2, key1))

    # output
    print("---plaintext---")
    for p in plaintext_binary:
        print("".join(func.decode(p)), end="")
    print()


if __name__ == "__main__":
    main()
