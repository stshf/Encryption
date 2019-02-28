import numpy as np

def enc(m, t):
    """
    ---parameters---
    m : plain text
    t : permutation rule
    """
    
    cipher_text = ""
    
    for m_ in m:
        ascii_m_ = ord(m_)
        if ord('a') <= ascii_m_ <= ord('z'):
            cipher_text += chr(t[ord(m_) - ord('a')] + ord('a'))
        elif ord('A') <= ascii_m_ <= ord('z'):
            cipher_text += chr(t[ord(m_) - ord('A')] + ord('A'))
        else:
            cipher_text += m_

    return cipher_text
 

def main():
    print("---transposition cipher---\nPlain text")
    plain_text = input().split()
    plain_text = list("".join(plain_text))
    print("transposition rule")
    permutation = list(map(int, input().split()))
    print(permutation)
    cipher_text = enc(plain_text, permutation)
    print(cipher_text)
    
if __name__ == "__main__":
    main()
