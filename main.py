from camellia.camellia_core import camellia_encrypt_block, camellia_decrypt_block
from camellia.cbc_mode import cbc_encrypt


def main():
    """""
    print("Camellia-128 Block Encryption (ECB mode)")

    # Input: Key and Plaintext (as hex strings)
    key_hex = input("Enter 128-bit key (32 hex digits): ").strip()
    plaintext_hex = input("Enter 128-bit plaintext (32 hex digits): ").strip()

    # Validate lengths
    if len(key_hex) != 32 or len(plaintext_hex) != 32:
        print("❌ Error: Both key and plaintext must be 32 hex digits (128 bits).")
        return

    try:
        key = int(key_hex, 16)
        plaintext = int(plaintext_hex, 16)
    except ValueError:
        print("❌ Error: Invalid hex input.")
        return

    # Encrypt
    ciphertext = camellia_encrypt_block(plaintext, key)

    # Output
    print(f"Ciphertext: {ciphertext:032x}")
"""
    key_hex = "f39fd9e02d78dc321ecc59692c22c3b3"
    iv_hex = "e88a6d70380f65346aeb79c39a20af88"
    expected_cipher_hex = "ad91a80f6385a3dca96b48aa533a88bf"

    key = int.from_bytes(bytes.fromhex(key_hex), 'big')
    iv = bytes.fromhex(iv_hex)
    plaintext = b"Hello"

    cipher = cbc_encrypt(plaintext, key, iv)
    actual_cipher_hex = cipher.hex()

    print("Camellia CBC Encryption Test")
    print(f"Key:        {key_hex}")
    print(f"IV:         {iv_hex}")
    print(f"Plaintext:  {plaintext}")
    print(f"Ciphertext: {actual_cipher_hex}")
    print(f"Expected:   {expected_cipher_hex}")

    if actual_cipher_hex == expected_cipher_hex:
        print("✅ Match! Encryption is correct.")
    else:
        print("❌ Mismatch! Check padding, IV, or core cipher.")

if __name__ == "__main__":
    main()