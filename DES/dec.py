import numpy as np
import function as func

def main():
    # input
    print("---input secret key---")
    key = list(map(int, input()))
    print("---input ciphertext---")
    ciphertext = list(map(int, input()))
    sub_key_list = func.sub_keygen_dec(key)
    len_ciphertext = len(ciphertext)
    
    # dec
    plaintext_binary = []
    for i in range(0, len_ciphertext, 64):
        plaintext_binary.append(func.crypto(ciphertext[i:i+64], sub_key_list))
    
    # output
    print("---plaintext---")
    for p in plaintext_binary:
        print("".join(func.decode(p)), end="")
    print()


if __name__ == "__main__":
    main()
