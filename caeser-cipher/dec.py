def Dec(c, n):
    """
    === input ===
    c(string) : cipher text
    n(itn)    : key (1~25)

    === return ===
    m(string) : plain text
    """
    m = ""
    for c_ in c:
        ascii_c_ = ord(c_)
        if ord('a') <= ascii_c_ <= ord('z'):
            m += chr((ord(c_) - ord('a') - n) % 26  + ord('a'))
        elif ord('A') <= ascii_c_ <= ord('Z'):
            m += chr((ord(c_) - ord('A') - n) % 26 + ord('A'))
        else:
            m += c_
    return m




def main():
    print("input cipher text (Alpahbet)")
    Cipher_text_list = list(input().split())
    print("")

    print("input key")
    key = int(input())
    print("")

    Plain_text_list = []
    for Cipher_text in Cipher_text_list:
        Plain_text_list.append(Dec(Cipher_text, key))
    print("Plain text")
    print(" ".join(Plain_text_list))

if __name__ == "__main__":
    main()
