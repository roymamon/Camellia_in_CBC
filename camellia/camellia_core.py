from .f_function import f_function

def camellia_round(left: int, right: int, subkey: int) -> tuple[int, int]:
    """
    Perform one Feistel round of the Camellia cipher.
    
    Args:
        left: Left 64-bit half of the block.
        right: Right 64-bit half of the block.
        subkey: 64-bit subkey for this round.

    Returns:
        Tuple of (new_left, new_right).
    """
    f_out = f_function(left, subkey)
    new_left = right ^ f_out
    new_right = left
    return new_left, new_right


# --- Simple test run (for dev testing) ---
if __name__ == "__main__":
    # Example 64-bit values (in hex)
    L = 0x0123456789ABCDEF
    R = 0x1111222233334444
    K = 0x0F0E0D0C0B0A0908

    print("Input:")
    print(f"Left  = {L:016X}")
    print(f"Right = {R:016X}")
    print(f"Key   = {K:016X}")

    new_L, new_R = camellia_round(L, R, K)

    print("\nAfter 1 round:")
    print(f"Left  = {new_L:016X}")
    print(f"Right = {new_R:016X}")