import secrets
import numpy as np

def keygen():
    """
    key generetor. key size = 64bit = str(8bit) * 8
    
    --input--
    None

    --output--
    key(array): 64 bit
    """
    key = [secrets.randbits(8) for i in range(8)]
    return key

def encode(m):
    """
    m -> binary 
    ---input---
    m(array): integer 0 <= , < 256
    
    ---output---
    binary(array): 64 bit
    """
    binary_string = ""
    for i in m:
        binary_string += np.binary_repr(i, width=8)
    return [int(i) for i in binary_string]

def decode(c):
    """
    1byte => ascii

    ---input---
    c(array): binary list

    ---output---
    ascii_list(list): ascii
    """
    ascii_list = []
    for i in range(0, 64, 8):
        ascii_list.append(chr(int("".join(map(str, c[i:i+8])), 2)))
    return ascii_list

def PC1(key):
    """
    64bit -> 56bit

    ---input---
    key(array): key 64bit

    ---output---
    PC1_key(array): 56bit
    """
    PC1 = [
        57, 49, 41, 33, 25, 17,  9,
        1, 58, 50, 42, 34, 26, 18,
        10,  2, 59, 51, 43, 35, 27,
        19, 11,  3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14,  6, 61, 53, 45, 37, 29,
        21, 13,  5, 28, 20, 12,  4]
    PC1_key = [key[i-1] for i in PC1]
    return PC1_key

def PC2(C, D):
    """
    56-bit -> 48-bit
    PC2(x) = PC2(x_1, ..., x_56) = (x_14, x_17, ..., x_29, x_32)

    ---input---
    C, D(array): Ci or Di 56bit

    ---output---
    key_i(array): key_i 48bit
    """
    PC2 = [
    14, 17, 11, 24,  1,  5,
    3, 28, 15,  6, 21, 10,
   23, 19, 12,  4, 26,  8,
   16,  7, 27, 20, 13,  2,
   41, 52, 31, 37, 47, 55,
   30, 40, 51, 45, 33, 48,
   44, 49, 39, 56, 34, 53,
   46, 42, 50, 36, 29, 32 
    ]
    CD =  np.concatenate((C, D), axis=0)
    key_i = [CD[i-1] for i in PC2]
    return key_i

def left_shift(binary_list, i):
    """
    binary shift  ex 1010 << 2 -> 101010
    if i = 1, 2, 9, 16: 1-bit shift
    else: 2-bit shift

    ---input---
    binary_list(array): binary list
    i(int): raund number

    ---output---
    shifted_list(array)
    """
    shift_number = [0, 1, 1, 2, 2, 2, 2, 2, 2, 1,
            2, 2, 2, 2, 2, 2, 1]
    shifted_list = np.roll(binary_list, -shift_number[i])
    
    return shifted_list

def right_shift(binary_list, i):
    """
    binary shift  ex 1010 >> 2 -> 0010
    if i = 1, 2, 9, 16: 1-bit shift
    else: 2-bit shift

    ---input---
    binary_list(array): binary list
    i(int): raund number

    ---output---
    shifted_list(array)
    """
    shift_number = [0, 0, 1, 2, 2, 2, 2, 2, 2, 1,
            2, 2, 2, 2, 2, 2, 1]
    
    shifted_list = np.roll(binary_list, shift_number[i])
    
    return shifted_list


def sub_keygen_enc():
    # Keygen
    # Step1: (C0, D0) = PC1(key)
    key = keygen()
    binary_key = encode(key)
    print("---secret key---")
    print("".join(map(str, binary_key)))
    PC1_key = PC1(binary_key)
    C0, D0 = PC1_key[:28], PC1_key[28:]
    # Step2: i=1
    i = 1
    # Step3: loop i <= 16
    Ci_1, Di_1 = C0, D0
    sub_key_list = []
    while i <= 16:
        # Step3-a Left shift
        Ci, Di = left_shift(Ci_1, i), left_shift(Di_1, i)
        # Step3-b 56-bit -> 48-bit
        k_i = PC2(Ci, Di)
        sub_key_list.append(k_i)
        Ci_1, Di_1 = Ci, Di
        i += 1
    return sub_key_list

def sub_keygen_dec(key):
    """
    keygen

    ---input---
    key(list): secret key

    ---output---
    sub_key_list(list)
    """
    # Step1: (C0, D0) = PC1(key)
    PC1_key = PC1(key)
    C0, D0 = PC1_key[:28], PC1_key[28:]
    # Step2: i=1
    i = 1
    # Step3: loop i <= 16
    Ci_1, Di_1 = C0, D0
    sub_key_list = []
    while i <= 16:
        # Step3-a Left shift
        Ci, Di = right_shift(Ci_1, i), right_shift(Di_1, i)
        # Step3-b 56-bit -> 48-bit
        k_i = PC2(Ci, Di)
        sub_key_list.append(k_i)
        Ci_1, Di_1 = Ci, Di
        i += 1
    return sub_key_list


def f(x, kn):
    """
    raund function x -> y

    ---input---
    x(array): 32-bit
    kn: sub key (48-bit)

    ---output---
    y(array): result (32-bit)
    """
    # 1. E(x) x:32 -> 48
    x1 = E(x)
    # 2. x1 xor key
    x2 = np.bitwise_xor(x1, kn)
    # 3. x3 = S(x2)
    x3 = S(x2)
    # 4. y = P(x3)
    y = P(x3)

    return y

def E(x):
    """
    transportation 32-bit -> 48-bit

    ---input---
    x(array): 32-bit

    ---output---
    E_x(array): 48-bit
    """
    E = [
    32,  1,  2,  3,  4,  5,  4,  5,
     6,  7,  8,  9,  8,  9, 10, 11,
    12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21,
    22, 23, 24, 25, 24, 25, 26, 27,
    28, 29, 28, 29, 30, 31, 32,  1]

    return np.array([x[i-1] for i in E])

def S(x):
    """
    x3 = Sn(x2) (n = 0, ...,7)

    ---input---
    x(array): 32-bit

    ---output---
    S_x(array): 32-bit
    """
    Sn = np.array([
        [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
        ])

    S_x = []
    for i in range(0, 48, 6):
        row = int('{}{}'.format(x[i], x[i+5]), 2)
        column = int('{}{}{}{}'.format(x[i+1], x[i+2], x[i+3], x[i+4]), 2)
        S_x += np.binary_repr(Sn[i//8][row][column], width=4)

    return [int(i) for i in S_x]

def P(x):
    """
    transportation 32-bit -> 32-bit
    
    ---input---
    x(array): 32-bit

    ---output---
    P_x(array): 32-bit
    """
    P = [
    16,  7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26,  5, 18, 31, 10,
     2,  8, 24, 14, 32, 27,  3,  9,
    19, 13, 30,  6, 22, 11,  4, 25]
    return np.array([x[i-1] for i in P])

def IP(m):
    """
    transportation 64-bit -> 64-bit

    ---input---
    m(array): 64-bit

    ---output---
    IP_x(array): 64-bit
    """
    IP = [
    58, 50, 42, 34, 26, 18, 10,  2,
    60, 52, 44, 36, 28, 20, 12,  4,
    62, 54, 46, 38, 30, 22, 14,  6,
    64, 56, 48, 40, 32, 24, 16,  8,
    57, 49, 41, 33, 25, 17,  9,  1,
    59, 51, 43, 35, 27, 19, 11,  3,
    61, 53, 45, 37, 29, 21, 13,  5,
    63, 55, 47, 39, 31, 23, 15,  7
          ]

    return np.array([m[i-1] for i in IP])

def IP_inv(x):
    """
    transportation 64-bit -> 64-bit

    ---input---
    x(array): 64-bit
    
    ---output---
    IP_inv_x(array): 64-bit
    """
    IP_inv = [
    40,  8, 48, 16, 56, 24, 64, 32,
    39,  7, 47, 15, 55, 23, 63, 31,
    38,  6, 46, 14, 54, 22, 62, 30,
    37,  5, 45, 13, 53, 21, 61, 29,
    36,  4, 44, 12, 52, 20, 60, 28,
    35,  3, 43, 11, 51, 19, 59, 27,
    34,  2, 42, 10, 50, 18, 58, 26,
    33,  1, 41,  9, 49, 17, 57, 25]

    return np.array([x[i-1] for i in IP_inv])

def des(m, sub_key_list):
    """
    encryption / decryption phase

    ---input---
    m(array): plain/cipher text 64-bit
    sub_key_list(array): sub-key-list

    ---output---
    cipher/plain text(array)
    """
    # 1. n = 1
    n = 1
    # 2. IP(m)
    IPm = IP(m)
    # 3. L0 <- 32, 32 -> R0
    L0, R0 = IPm[:32], IPm[32:]
    Ln_1, Rn_1 = L0[:], R0[:]
    # 4. for 1 to 16
    while n <= 16:
        # 4.a y = f(Rn_1, kn)
        y = f(Rn_1, sub_key_list[n-1])
        # 4.b Ln_1 xor y = Ln
        Ln = np.bitwise_xor(Ln_1, y)
        Rn = Rn_1[:]
        # 4.c  if n != 16: swap(Ln, Rn) 
        if n == 16:
            pass
        else:
            Ln, Rn = Rn[:], Ln[:]
            Ln_1 , Rn_1 = Ln[:], Rn[:]
        # 4.d n = n+1
        n += 1
    # 5 c = IP^(-1)(L16 + R16)
    text = IP_inv(np.concatenate((Ln, Rn), axis=None))
    return text

