from camellia.camellia_core import camellia_encrypt_block

def main():
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

if __name__ == "__main__":
    main()