import numpy as np

def dec(c, t):
    """
    ---parameters---
    c : cipher text
    t : permutation rule
    """
    
    plain_text = ""
    
    for c_ in c:
        ascii_c_ = ord(c_)
        if ord('a') <= ascii_c_ <= ord('z'):
            plain_text += chr(t[ord(c_) - ord('a')] + ord('a'))
        elif ord('A') <= ascii_c_ <= ord('z'):
            plain_text += chr(t[ord(c_) - ord('A')] + ord('A'))
        else:
            plain_text += c_

    return plain_text
 

def main():
    print("---transposition cipher---\ncipher text")
    cipher_text = input().split()
    cipher_text = list("".join(cipher_text))
    print("transposition rule")
    permutation = np.array(list(map(int, input().split())))
    permutation = np.argsort(permutation)
    plain_text = dec(cipher_text, permutation)
    print("plain text")
    print(plain_text)
    
if __name__ == "__main__":
    main()
