from camellia.camellia_core import feistel_encrypt_rounds

if __name__ == "__main__":
    L = 0x0123456789ABCDEF
    R = 0x1111222233334444

    fake_key = 0x0F0E0D0C0B0A0908

    round_keys = [fake_key] * 18

    L_out, R_out = feistel_encrypt_rounds(L, R, round_keys, 18)

    print(f"After 18 rounds:")
    print(f"Left  = {L_out:016X}")
    print(f"Right = {R_out:016X}")