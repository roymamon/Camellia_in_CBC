from .constants import MASK128
def rotl128(x: int, shift: int) -> int:
    shift %= 128
    return ((x << shift) | (x >> (128 - shift))) & MASK128