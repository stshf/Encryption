import random

def random_alphabet():
    """
    === return ===
    random alphabet in lower cases
    """

    alphabet_list = [chr(i + ord('a')) for i in range(26)]
    return random.choice(alphabet_list)


def enc(text, key):
    # scytale encryption
    text_list = [c for c in text]

    len_text = len(text_list)
    quotient_key = -(-len_text // key)
    mod_key = len_text % key

    for i in range((key - mod_key)%key):
        text_list.append(random_alphabet())

    cipher = ""
    for i in range(key):
        for j in range(quotient_key):
            cipher += text_list[key*j + i]
    return cipher


def main():
    key = int(input("input number(int)\n"))
    text = input("input plain text\n")
    print(enc(text, key))

if __name__ == "__main__":
    main()
