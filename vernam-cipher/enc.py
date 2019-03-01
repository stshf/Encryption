import numpy as np
import secrets


def random_bit(n):
    """
    ---parameters---
    n (int): bit length
    """
    return np.array([secrets.randbelow(256) for _ in range(n)])


def encode(m):
    """
    ---parameters---
    m (list): plain text
    """
    
    
    binary_m =  np.array(list(map(int, map(ord, m))))
    return binary_m


def enc(m, key):
    """
    ---parameters---
    m (np.array): binary 
    key (np.array): {0, 1}^n 
    """
    
    cipher_text = np.bitwise_xor(m, key)
    cipher_text = ''.join([format(i , '08b') for i in cipher_text])
    return cipher_text


def main():
    print("---transposition cipher---\nplain text")
    plain_text = input()
    plain_text = list("".join(plain_text))
    binary_m = encode(plain_text)

    key = random_bit(len(plain_text))
    cipher_text = enc(binary_m, key)
    print("---secret key---")
    print(''.join([format(i , '08b') for i in key]))
    print("---cipher---")
    print(cipher_text)

if __name__ == "__main__":
    main()
