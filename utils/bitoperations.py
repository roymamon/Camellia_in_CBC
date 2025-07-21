def split_block(b: int) -> tuple[int, int]:
    return (b >> 64) & 0xFFFFFFFFFFFFFFFF, b & 0xFFFFFFFFFFFFFFFF

def join_block(l: int, r: int) -> int:
    return (l << 64) | r

def left_rotate128(x: int, n: int) -> int:
    return ((x << n) | (x >> (128 - n))) & ((1 << 128) - 1)

def apply_p_function(b: list[int]) -> int:
    return int.from_bytes([
        b[0], b[2], b[1], b[3],
        b[6], b[4], b[7], b[5]
    ], 'big')