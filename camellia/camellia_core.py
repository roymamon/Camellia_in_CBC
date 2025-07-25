from utils.constants import MASK64
from .f_functions import f_function, fl_function, flinv_function
from .key_schedule import generate_subkeys, generate_subkeys_192, generate_subkeys_256

def camellia_encrypt_block(plaintext: int, key: int) -> int:

    """128-bit plaintext M is divided into
    the left 64-bit D1 and the right
    64-bit D2"""
    D1 = plaintext >> 64
    D2 = plaintext & MASK64

    subkeys = generate_subkeys(key)
    kw = subkeys["kw"]
    k = subkeys["k"]
    ke = subkeys["ke"]


    """Encryption is performed using an
    18-round Feistel structure with FL-
    and FLINV-functions inserted every 6
    rounds"""
    D1 = D1 ^ kw[0]  #prewhitening  
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
    D2 = D2 ^ kw[2]  #postwhitening
    D1 = D1 ^ kw[3]

    """128-bit ciphertext C is constructed
    from D1 and D2 as follows"""
    ciphertext = (D2 << 64) | D1
    return ciphertext

def camellia_decrypt_block(ciphertext: int, key: int) -> int:
  
    """The decryption procedure can be done
    in the same way as the encryption
    procedure by reversing the order of
    the subkeys"""
    D2 = ciphertext >> 64
    D1 = ciphertext & MASK64

    subkeys = generate_subkeys(key)
    kw = subkeys["kw"]
    k = subkeys["k"]
    ke = subkeys["ke"]

    #reverse subkeys
    kw = [kw[2], kw[3], kw[0], kw[1]]
    k = k[::-1]
    ke = [ke[3], ke[2], ke[1], ke[0]]

    #prewhitening (using reversed kw3, kw4)
    D2 ^= kw[0]
    D1 ^= kw[1]

    #rounds (reverse order)
    D1 ^= f_function(D2, k[0])
    D2 ^= f_function(D1, k[1])
    D1 ^= f_function(D2, k[2])
    D2 ^= f_function(D1, k[3])
    D1 ^= f_function(D2, k[4])
    D2 ^= f_function(D1, k[5])
    D2 = fl_function(D2, ke[0])     
    D1 = flinv_function(D1, ke[1])  
    D1 ^= f_function(D2, k[6])
    D2 ^= f_function(D1, k[7])
    D1 ^= f_function(D2, k[8])
    D2 ^= f_function(D1, k[9])
    D1 ^= f_function(D2, k[10])
    D2 ^= f_function(D1, k[11])
    D2 = fl_function(D2, ke[2])     
    D1 = flinv_function(D1, ke[3])  
    D1 ^= f_function(D2, k[12])
    D2 ^= f_function(D1, k[13])
    D1 ^= f_function(D2, k[14])
    D2 ^= f_function(D1, k[15])
    D1 ^= f_function(D2, k[16])
    D2 ^= f_function(D1, k[17])

    #postwhitening (using reversed kw1, kw2)
    D1 ^= kw[2]
    D2 ^= kw[3]

    plaintext = (D1 << 64) | D2
    return plaintext

def camellia_encrypt_block_192(plaintext: int, key: int) -> int:
    D1 = plaintext >> 64
    D2 = plaintext & MASK64

    subkeys = generate_subkeys_192(key)
    kw = subkeys["kw"]
    k = subkeys["k"]
    ke = subkeys["ke"]

    """Encryption is performed using a
    24-round Feistel structure with FL-
    and FLINV-functions inserted every 6
    rounds"""
    D1 ^= kw[0]
    D2 ^= kw[1]

    D2 ^= f_function(D1, k[0])
    D1 ^= f_function(D2, k[1])
    D2 ^= f_function(D1, k[2])
    D1 ^= f_function(D2, k[3])
    D2 ^= f_function(D1, k[4])
    D1 ^= f_function(D2, k[5])

    D1 = fl_function(D1, ke[0])
    D2 = flinv_function(D2, ke[1])

    D2 ^= f_function(D1, k[6])
    D1 ^= f_function(D2, k[7])
    D2 ^= f_function(D1, k[8])
    D1 ^= f_function(D2, k[9])
    D2 ^= f_function(D1, k[10])
    D1 ^= f_function(D2, k[11])

    D1 = fl_function(D1, ke[2])
    D2 = flinv_function(D2, ke[3])

    D2 ^= f_function(D1, k[12])
    D1 ^= f_function(D2, k[13])
    D2 ^= f_function(D1, k[14])
    D1 ^= f_function(D2, k[15])
    D2 ^= f_function(D1, k[16])
    D1 ^= f_function(D2, k[17])

    D1 = fl_function(D1, ke[4])
    D2 = flinv_function(D2, ke[5])

    D2 ^= f_function(D1, k[18])
    D1 ^= f_function(D2, k[19])
    D2 ^= f_function(D1, k[20])
    D1 ^= f_function(D2, k[21])
    D2 ^= f_function(D1, k[22])
    D1 ^= f_function(D2, k[23])

    D2 ^= kw[2]
    D1 ^= kw[3]

    ciphertext = (D2 << 64) | D1
    return ciphertext

def camellia_decrypt_block_192(ciphertext: int, key: int) -> int:
    D2 = ciphertext >> 64
    D1 = ciphertext & MASK64

    subkeys = generate_subkeys_192(key)
    kw = subkeys["kw"]
    k = subkeys["k"]
    ke = subkeys["ke"]

    kw = [kw[2], kw[3], kw[0], kw[1]]  
    k = k[::-1]                        
    ke = [ke[5], ke[4], ke[3], ke[2], ke[1], ke[0]]  

    D2 ^= kw[0]
    D1 ^= kw[1]

    D1 ^= f_function(D2, k[0])
    D2 ^= f_function(D1, k[1])
    D1 ^= f_function(D2, k[2])
    D2 ^= f_function(D1, k[3])
    D1 ^= f_function(D2, k[4])
    D2 ^= f_function(D1, k[5])

    D2 = fl_function(D2, ke[0])
    D1 = flinv_function(D1, ke[1])

    D1 ^= f_function(D2, k[6])
    D2 ^= f_function(D1, k[7])
    D1 ^= f_function(D2, k[8])
    D2 ^= f_function(D1, k[9])
    D1 ^= f_function(D2, k[10])
    D2 ^= f_function(D1, k[11])

    D2 = fl_function(D2, ke[2])
    D1 = flinv_function(D1, ke[3])

    D1 ^= f_function(D2, k[12])
    D2 ^= f_function(D1, k[13])
    D1 ^= f_function(D2, k[14])
    D2 ^= f_function(D1, k[15])
    D1 ^= f_function(D2, k[16])
    D2 ^= f_function(D1, k[17])

    D2 = fl_function(D2, ke[4])
    D1 = flinv_function(D1, ke[5])

    D1 ^= f_function(D2, k[18])
    D2 ^= f_function(D1, k[19])
    D1 ^= f_function(D2, k[20])
    D2 ^= f_function(D1, k[21])
    D1 ^= f_function(D2, k[22])
    D2 ^= f_function(D1, k[23])

    D1 ^= kw[2]
    D2 ^= kw[3]

    plaintext = (D1 << 64) | D2
    return plaintext

def camellia_encrypt_block_256(plaintext: int, key: int) -> int:
    D1 = plaintext >> 64
    D2 = plaintext & MASK64

    subkeys = generate_subkeys_256(key)
    kw = subkeys["kw"]
    k = subkeys["k"]
    ke = subkeys["ke"]

    D1 ^= kw[0]
    D2 ^= kw[1]

    D2 ^= f_function(D1, k[0])
    D1 ^= f_function(D2, k[1])
    D2 ^= f_function(D1, k[2])
    D1 ^= f_function(D2, k[3])
    D2 ^= f_function(D1, k[4])
    D1 ^= f_function(D2, k[5])

    D1 = fl_function(D1, ke[0])
    D2 = flinv_function(D2, ke[1])

    D2 ^= f_function(D1, k[6])
    D1 ^= f_function(D2, k[7])
    D2 ^= f_function(D1, k[8])
    D1 ^= f_function(D2, k[9])
    D2 ^= f_function(D1, k[10])
    D1 ^= f_function(D2, k[11])

    # FL/FLINV 2
    D1 = fl_function(D1, ke[2])
    D2 = flinv_function(D2, ke[3])

    D2 ^= f_function(D1, k[12])
    D1 ^= f_function(D2, k[13])
    D2 ^= f_function(D1, k[14])
    D1 ^= f_function(D2, k[15])
    D2 ^= f_function(D1, k[16])
    D1 ^= f_function(D2, k[17])

    D1 = fl_function(D1, ke[4])
    D2 = flinv_function(D2, ke[5])

    D2 ^= f_function(D1, k[18])
    D1 ^= f_function(D2, k[19])
    D2 ^= f_function(D1, k[20])
    D1 ^= f_function(D2, k[21])
    D2 ^= f_function(D1, k[22])
    D1 ^= f_function(D2, k[23])

    D2 ^= kw[2]
    D1 ^= kw[3]

    ciphertext = (D2 << 64) | D1
    return ciphertext


def camellia_decrypt_block_256(ciphertext: int, key: int) -> int:
    D2 = ciphertext >> 64
    D1 = ciphertext & MASK64

    subkeys = generate_subkeys_256(key)
    kw = subkeys["kw"]
    k = subkeys["k"]
    ke = subkeys["ke"]

    kw = [kw[2], kw[3], kw[0], kw[1]]  
    k = k[::-1]                        
    ke = [ke[5], ke[4], ke[3], ke[2], ke[1], ke[0]]  

    D2 ^= kw[0]
    D1 ^= kw[1]

    D1 ^= f_function(D2, k[0])
    D2 ^= f_function(D1, k[1])
    D1 ^= f_function(D2, k[2])
    D2 ^= f_function(D1, k[3])
    D1 ^= f_function(D2, k[4])
    D2 ^= f_function(D1, k[5])

    D2 = fl_function(D2, ke[0])
    D1 = flinv_function(D1, ke[1])

    D1 ^= f_function(D2, k[6])
    D2 ^= f_function(D1, k[7])
    D1 ^= f_function(D2, k[8])
    D2 ^= f_function(D1, k[9])
    D1 ^= f_function(D2, k[10])
    D2 ^= f_function(D1, k[11])

    D2 = fl_function(D2, ke[2])
    D1 = flinv_function(D1, ke[3])

    D1 ^= f_function(D2, k[12])
    D2 ^= f_function(D1, k[13])
    D1 ^= f_function(D2, k[14])
    D2 ^= f_function(D1, k[15])
    D1 ^= f_function(D2, k[16])
    D2 ^= f_function(D1, k[17])

    D2 = fl_function(D2, ke[4])
    D1 = flinv_function(D1, ke[5])

    D1 ^= f_function(D2, k[18])
    D2 ^= f_function(D1, k[19])
    D1 ^= f_function(D2, k[20])
    D2 ^= f_function(D1, k[21])
    D1 ^= f_function(D2, k[22])
    D2 ^= f_function(D1, k[23])

    D1 ^= kw[2]
    D2 ^= kw[3]

    plaintext = (D1 << 64) | D2
    return plaintext