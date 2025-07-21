def rotl128(x: int, shift: int) -> int:
    shift %= 128
    return ((x << shift) | (x >> (128 - shift))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF