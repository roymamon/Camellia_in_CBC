from .sbox import SBOX1, SBOX2, SBOX3, SBOX4

def apply_sboxes(value: int) -> list[int]:
    bytes_in = [(value >> (8 * i)) & 0xFF for i in reversed(range(8))]
    return [
        SBOX1[bytes_in[0]],
        SBOX2[bytes_in[1]],
        SBOX3[bytes_in[2]],
        SBOX4[bytes_in[3]],
        SBOX2[bytes_in[4]],
        SBOX3[bytes_in[5]],
        SBOX4[bytes_in[6]],
        SBOX1[bytes_in[7]],
    ]

def p_function(sboxed_bytes: list[int]) -> int:
    y = [0] * 8
    y[0] = sboxed_bytes[0] ^ sboxed_bytes[2] ^ sboxed_bytes[3] ^ sboxed_bytes[5] ^ sboxed_bytes[6] ^ sboxed_bytes[7]
    y[1] = sboxed_bytes[0] ^ sboxed_bytes[1] ^ sboxed_bytes[3] ^ sboxed_bytes[4] ^ sboxed_bytes[6] ^ sboxed_bytes[7]
    y[2] = sboxed_bytes[0] ^ sboxed_bytes[1] ^ sboxed_bytes[2] ^ sboxed_bytes[4] ^ sboxed_bytes[5] ^ sboxed_bytes[7]
    y[3] = sboxed_bytes[1] ^ sboxed_bytes[2] ^ sboxed_bytes[3] ^ sboxed_bytes[4] ^ sboxed_bytes[5] ^ sboxed_bytes[6]
    y[4] = sboxed_bytes[0] ^ sboxed_bytes[1] ^ sboxed_bytes[5] ^ sboxed_bytes[6] ^ sboxed_bytes[7]
    y[5] = sboxed_bytes[1] ^ sboxed_bytes[2] ^ sboxed_bytes[4] ^ sboxed_bytes[6] ^ sboxed_bytes[7]
    y[6] = sboxed_bytes[2] ^ sboxed_bytes[3] ^ sboxed_bytes[4] ^ sboxed_bytes[5] ^ sboxed_bytes[7]
    y[7] = sboxed_bytes[0] ^ sboxed_bytes[3] ^ sboxed_bytes[4] ^ sboxed_bytes[5] ^ sboxed_bytes[6]

    result = 0
    for byte in y:
        result = (result << 8) | byte
    return result

def f_function(input64: int, subkey64: int) -> int:
    xored = input64 ^ subkey64
    return p_function(apply_sboxes(xored))