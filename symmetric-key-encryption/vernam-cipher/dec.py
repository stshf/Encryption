import numpy as np
import secrets


def dec(c, key):
    """
    ---parameters---
    c (np.array): cipher text
    key (np.array): {0, 1}^n 
    """
    
    plaintext = c ^ key
    plaintext = list(map(str, plaintext))
    plaintext = [chr(int(''.join(plaintext[i:i+8]), 2)) for i in range(0, len(c), 8)]
    return ''.join(plaintext)


def main():
    print("---transposition cipher---\nciphertext")
    ciphertext = list(input())

    print("---input key---")
    key = list(input())
    
    ciphertext = np.array(list(map(int, ciphertext)))
    key = np.array(list(map(int, key)))
    print(dec(ciphertext, key))
    
if __name__ == "__main__":
    main()
