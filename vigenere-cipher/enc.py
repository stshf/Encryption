import numpy as np

def enc(m, key):
    """
    ---parameters---
    m : plain text
    key : string
    """
    
    cipher = ""
    len_key = len(key)
    i = 0
    for m_ in m:
        ascii_m_ = ord(m_)
        if ord('a') <= ascii_m_ < ord('z'):
            cipher += chr((ascii_m_ - ord('a') + ord(key[i]) - ord('A')) % 26 + ord('A'))
        elif ord('A') <= ascii_m_ < ord('Z'):
            cipher += chr((ascii_m_ - ord('A') + ord(key[i]) - ord('A')) % 26 + ord('A'))
        else:
            cipher += m_
        
        i += 1
        i %= len_key
        
            
    return cipher
 

def main():
    print("---vigenere cipher---\nInput plain text")
    plain_text = input().split()
    plain_text = list("".join(plain_text))
    print("Input key")
    key = list(input().upper())
    print(enc(plain_text, key))
    
if __name__ == "__main__":
    main()
