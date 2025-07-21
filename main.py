from camellia.camellia_core import camellia_round

if __name__ == "__main__":
    L = 0x0123456789ABCDEF
    R = 0x1111222233334444
    K = 0x0F0E0D0C0B0A0908

    new_L, new_R = camellia_round(L, R, K)

    print("After 1 round:")
    print(f"Left  = {new_L:016X}")
    print(f"Right = {new_R:016X}")