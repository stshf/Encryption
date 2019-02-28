import numpy as np

def dec(c, key):
    """
    ---parameters---
    c : cipher text
    key : string
    """
    
    plain_text = ""
    len_key = len(key)
    i = 0
    for c_ in c:
        ascii_c_ = ord(c_)
        if ord('a') <= ascii_c_ <= ord('z'):
            plain_text += chr((ascii_c_ - ord('a') - (ord(key[i]) - ord('A'))) % 26 + ord('a'))
        elif ord('A') <= ascii_c_ <= ord('Z'):
            plain_text += chr((ascii_c_ - ord('A') - (ord(key[i]) - ord('A'))) % 26 + ord('a'))
        else:
            plain_text += c_
        i += 1
        i %= len_key

    return plain_text
 

def main():
    print("---transposition cipher---\ncipher text")
    cipher_text = input().split()
    cipher_text = list("".join(cipher_text))
    print("transposition rule")
    key = list(input().upper())
    plain_text = dec(cipher_text, key)
    print("plain text")
    print(plain_text)
    
if __name__ == "__main__":
    main()
