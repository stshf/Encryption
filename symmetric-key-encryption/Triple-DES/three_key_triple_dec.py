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
    sub_key1 = func.sub_keygen_dec(key1)
    sub_key2 = func.sub_keygen_dec(key2)
    sub_key3 = func.sub_keygen_dec(key3)
    len_ciphertext = len(ciphertext)

    # dec
    plaintext_binary = []
    for i in range(0, len_ciphertext, 64):
        # dec(ciphertext, key1)
        text1 = func.des(ciphertext[i:i+64], sub_key3)
        # enc(text1, key2)
        text2 = func.des(text1, sub_key2)
        # enc(c2, key2)
        text3 = func.des(text2, sub_key1)
        plaintext_binary.append(text3)

    # output
    print("---plaintext---")
    for p in plaintext_binary:
        print("".join(func.decode(p)), end="")
    print()


if __name__ == "__main__":
    main()
