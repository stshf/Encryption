import numpy as np


def enc(m, t):
    """
    ---parameters---
    m : plain text
    t : permutation rule
    """
    split_number = len(t)
    len_m = len(m)
    split_m_by_len_t = [np.array(list(m[i:i+split_number])) for i in range(0, len_m, split_number)]
    
    cipher_text = ""
    for m_element in split_m_by_len_t[:-1]:
        cipher_text += "".join(m_element[t])

    len_split_m_tail = len(split_m_by_len_t[-1])
    if len_split_m_tail < split_number:
        t_renew = list(filter(lambda x:x < len_split_m_tail, t))
        cipher_text += "".join(split_m_by_len_t[-1][t_renew])
    else:
        cipher_text += "".join(split_m_by_len_t[-1][t])
    
    
    print(cipher_text)





def main():
    print("---transposition cipher---\nPlain text")
    plain_text = input().split()
    plain_text = "".join(plain_text)
    
    print("transposition rule")
    permutation = list(map(int, input().split()))
    enc(plain_text, permutation)
    
if __name__ == "__main__":
    main()
