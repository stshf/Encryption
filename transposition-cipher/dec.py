import numpy as np


def dec(c, t):
    """
    ---parameters---
    c : cipher text
    t : permutation rule
    """
    t_inverse = np.argsort(t)
    print(t_inverse)
    split_number = len(t_inverse)
    len_c = len(c)
    split_c_by_len_t_inverse = [np.array(list(c[i:i+split_number])) for i in range(0, len_c, split_number)]
    
    plain_text = ""
    for c_element in split_c_by_len_t_inverse[:-1]:
        plain_text += "".join(c_element[t_inverse])

    len_split_c_tail = len(split_c_by_len_t_inverse[-1])
    print(len_split_c_tail)
    if len_split_c_tail < split_number:
        t_renew = np.argsort(np.array(list(filter(lambda x:x < len_split_c_tail, t))))
        print(t_renew)
        plain_text += "".join(split_c_by_len_t_inverse[-1][t_renew])
    else:
        plain_text += "".join(split_c_by_len_t_inverse[-1][t_renew])
    
    
    print(plain_text)





def main():
    print("---transposition cipher---\ncipher text")
    cipher_text = input().split()
    cipher_text = "".join(cipher_text)
    
    print("transposition rule")
    permutation = list(map(int, input().split()))
    dec(cipher_text, permutation)
    
if __name__ == "__main__":
    main()
