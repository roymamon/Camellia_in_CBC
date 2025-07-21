from .key_schedule import generate_subkeys
from .f_function import f_function
from .fl_layers import fl_layer_encrypt
from utils.bitoperations import split_block, join_block

def camellia_encrypt_block(plaintext: int, key: int) -> int:
    keys = generate_subkeys(key)
    L, R = split_block(plaintext)

    L ^= keys['kw'][0]
    R ^= keys['kw'][1]

    for i in range(18):
        F = f_function(R, keys['rk'][i])
        L, R = R, L ^ F
        if i == 5:
            L, R = fl_layer_encrypt(L, R, keys['fl'][0], keys['fl'][1])
        elif i == 11:
            L, R = fl_layer_encrypt(L, R, keys['fl'][2], keys['fl'][3])

    L, R = R, L
    L ^= keys['kw'][2]
    R ^= keys['kw'][3]
    return join_block(L, R)