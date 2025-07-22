from camellia.camellia_core import camellia_encrypt_block, camellia_decrypt_block
from camellia.cbc_mode import cbc_encrypt, cbc_decrypt

def get_bytes(prompt: str, expected_len: int = None) -> bytes:
    while True:
        user_input = input(prompt).strip()
        if user_input == "-1":
            exit()
        try:
            data = bytes.fromhex(user_input)
            if expected_len and len(data) != expected_len:
                print(f"❌ Input must be {expected_len} bytes ({expected_len*2} hex characters)")
                continue
            return data
        except ValueError:
            print("❌ Invalid hex input.")

def main():
    print("Camellia")
    print("Type -1 to exit.\n")

    while True:
        mode = input("Choose mode: [1] ECB (raw Camellia)  [2] CBC(Cipher Block Chaining): ").strip()
        if mode == "-1":
            break
        if mode not in {"1", "2"}:
            print("❌ Invalid mode.")
            continue

        action = input("Choose action: [E] Encrypt  [D] Decrypt: ").strip().lower()
        if action == "-1":
            break
        if action not in {"e", "d"}:
            print("❌ Invalid action.")
            continue

        key_bytes = get_bytes("Enter 128-bit key (32 hex chars): ", expected_len=16)
        key = int.from_bytes(key_bytes, "big")

        if mode == "1": 
            if action == "e":
                pt = get_bytes("Enter 128-bit plaintext (32 hex chars): ", expected_len=16)
                pt_int = int.from_bytes(pt, "big")
                ct_int = camellia_encrypt_block(pt_int, key)
                print("Ciphertext:", ct_int.to_bytes(16, "big").hex())

            else: 
                ct = get_bytes("Enter 128-bit ciphertext (32 hex chars): ", expected_len=16)
                ct_int = int.from_bytes(ct, "big")
                pt_int = camellia_decrypt_block(ct_int, key)
                print("Plaintext:", pt_int.to_bytes(16, "big").hex())

        elif mode == "2":
            iv = get_bytes("Enter 128-bit IV (32 hex chars): ", expected_len=16)

            if action == "e":
                plaintext = input("Enter plaintext string: ").encode()
                ciphertext = cbc_encrypt(plaintext, key, iv)
                print("Ciphertext (hex):", ciphertext.hex())

            else:
                ciphertext_hex = input("Enter ciphertext (hex): ").strip()
                if ciphertext_hex == "-1":
                    break
                try:
                    ciphertext = bytes.fromhex(ciphertext_hex)
                    plaintext = cbc_decrypt(ciphertext, key, iv)
                    print("Decrypted text:", plaintext.decode(errors="replace"))
                except Exception as e:
                    print(f"Decryption failed: {e}")

        print("\n---\n")

if __name__ == "__main__":
    main()