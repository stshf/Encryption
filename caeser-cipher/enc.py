def Enc(m, n):
    """input
        m : plain text 
        type char

        n : key 1 ~ 25
        type int
        
        output
        c : cipher text
        type char
    """
    c = ""
    for m_ in m:
        ascii_m_ = ord(m_)
        if ord('a') <= ascii_m_ <= ord('z'):
            c += chr((ord(m_) - ord('a') + n) % 26  + ord('a'))
        elif ord('A') <= ascii_m_ <= ord('Z'):
            c += chr((ord(m_) - ord('A') + n) % 26 + ord('A'))
        else:
            c += m_
    return c




def main():
    print("input plain text (Alpahbet)")
    Plain_text_list = list(input().split())
    print("")

    print("input key")
    key = int(input())
    print("")

    Cipher_text_list = []
    for Plain_text in Plain_text_list:
        Cipher_text_list.append(Enc(Plain_text, key))
        
    print("Chiper text")
    print(" ".join(Cipher_text_list))
    

if __name__ == "__main__":
    main()
