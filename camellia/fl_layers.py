def fl_layer_encrypt(l: int, r: int, ke1: int, ke2: int) -> tuple[int, int]:
    l1 = l & ke1
    r ^= ((l1 << 1) | (l1 >> 63)) & 0xFFFFFFFFFFFFFFFF
    r1 = r | ke2
    l ^= ((r1 >> 1) | (r1 << 63)) & 0xFFFFFFFFFFFFFFFF
    return l, r