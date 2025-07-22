from utils.constants import MASK64
from .f_functions import f_function, fl_function, flinv_function
from .key_schedule import generate_subkeys

def camellia_encrypt_block(plaintext: int, key: int) -> int:

    #split to left and right
    D1 = plaintext >> 64
    D2 = plaintext & MASK64

    subkeys = generate_subkeys(key)
    kw = subkeys["kw"]
    k = subkeys["k"]
    ke = subkeys["ke"]

    #Prewhitening
    D1 = D1 ^ kw[0]   
    D2 = D2 ^ kw[1]
    D2 = D2 ^ f_function(D1,k[0])  #round 1
    D1 = D1 ^ f_function(D2,k[1])  #round 2
    D2 = D2 ^ f_function(D1,k[2])  #round 3
    D1 = D1 ^ f_function(D2,k[3])  #round 4
    D2 = D2 ^ f_function(D1,k[4])  #round 5
    D1 = D1 ^ f_function(D2,k[5])  #round 6
    D1 = fl_function(D1,ke[0])  #FL
    D2 = flinv_function(D2,ke[1])  #FLINV
    D2 = D2 ^ f_function(D1,k[6])  #round 7
    D1 = D1 ^ f_function(D2,k[7])  #round 8
    D2 = D2 ^ f_function(D1,k[8])  #round 9
    D1 = D1 ^ f_function(D2,k[9])  #round 10
    D2 = D2 ^ f_function(D1,k[10])  #round 11
    D1 = D1 ^ f_function(D2,k[11])  #round 12
    D1 = fl_function(D1,ke[2])  #FL
    D2 = flinv_function(D2,ke[3])  #FLINV
    D2 = D2 ^ f_function(D1,k[12])  #round 13
    D1 = D1 ^ f_function(D2,k[13])  #round 14
    D2 = D2 ^ f_function(D1,k[14])  #round 15
    D1 = D1 ^ f_function(D2,k[15])  #round 16
    D2 = D2 ^ f_function(D1,k[16])  #round 17
    D1 = D1 ^ f_function(D2,k[17])  #round 18
    #Postwhitening
    D2 = D2 ^ kw[2]  
    D1 = D1 ^ kw[3]

    ciphertext = (D2 << 64) | D1
    return ciphertext

def camellia_decrypt_block(ciphertext: int, key: int) -> int:
    D2 = ciphertext >> 64
    D1 = ciphertext & MASK64

    subkeys = generate_subkeys(key)
    kw = subkeys["kw"]
    k = subkeys["k"]
    ke = subkeys["ke"]

    # Reverse subkeys
    kw = [kw[2], kw[3], kw[0], kw[1]]
    k = k[::-1]
    ke = [ke[3], ke[2], ke[1], ke[0]]

    # Prewhitening (using reversed kw3, kw4)
    D2 ^= kw[0]
    D1 ^= kw[1]

    # Rounds (reverse order)
    D1 ^= f_function(D2, k[0])
    D2 ^= f_function(D1, k[1])
    D1 ^= f_function(D2, k[2])
    D2 ^= f_function(D1, k[3])
    D1 ^= f_function(D2, k[4])
    D2 ^= f_function(D1, k[5])
    D2 = fl_function(D2, ke[0])     # FL
    D1 = flinv_function(D1, ke[1])  # FLINV
    D1 ^= f_function(D2, k[6])
    D2 ^= f_function(D1, k[7])
    D1 ^= f_function(D2, k[8])
    D2 ^= f_function(D1, k[9])
    D1 ^= f_function(D2, k[10])
    D2 ^= f_function(D1, k[11])
    D2 = fl_function(D2, ke[2])     # FL
    D1 = flinv_function(D1, ke[3])  # FLINV
    D1 ^= f_function(D2, k[12])
    D2 ^= f_function(D1, k[13])
    D1 ^= f_function(D2, k[14])
    D2 ^= f_function(D1, k[15])
    D1 ^= f_function(D2, k[16])
    D2 ^= f_function(D1, k[17])

    # Postwhitening (using reversed kw1, kw2)
    D1 ^= kw[2]
    D2 ^= kw[3]

    plaintext = (D1 << 64) | D2
    return plaintext