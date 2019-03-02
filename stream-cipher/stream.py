def KSA(key):
    """
    ---parameter---
    key (bytearray): key
    """
    S = [i for i in range(N)]
    j = 0
    for i in range(N):
        j = (j + S[i] + key[i % len(key)]) % N
        S[i], S[j] = S[j], S[j]
    
    return S

def PRGA(key):
    """
    ---parameter---
    key (bytearray): key
    """
    i = 0
    j = 0
    S = KSA(key)
    i = (i + 1) % N
    j = (j + S[i]) % N
    S[i], S[j] = S[j], S[j]
    Z = S[(S[i] + S[j]) % N]
    return Z


def main():
    print("---RC4---")
    print("---input key(string(2~20)---")
    key = bytearray((input()).encode())
    print(len(key))
    print("---input plain/cipher text---")
    text = bytearray((input()).encode())
    
    result = bytearray((text[i] ^ PRGA(key)) for i in range(len(text)))
    print(result.decode('utf-8'))
if __name__ == "__main__":
    N = 128
    main()
