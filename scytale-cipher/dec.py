def dec(cipher, key):
    """ Encrypts a 'text' using the scytale cipher with specified key """
    cipher_list = [c for c in cipher]

    len_text = len(cipher_list)
    quotient_key = -(-len_text // key)

    plain_text = ""
    for i in range(quotient_key):
        for j in range(key):
            plain_text += cipher_list[quotient_key * j + i]
    
    return plain_text


def main():

    key = int(input("input number(int)\n"))
    cipher = input("input cipher\n")

    print("plain text\n")
    print(dec(cipher, key))
    

if __name__ == "__main__":
    main()
