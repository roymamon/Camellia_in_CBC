from .sbox import apply_sboxes
from utils.bitoperations import apply_p_function

def f_function(input64: int, subkey: int) -> int:
    x = input64 ^ subkey
    x_bytes = x.to_bytes(8, 'big')
    sboxed = apply_sboxes(x_bytes)
    return apply_p_function(sboxed)