from camellia.camellia_core import camellia_encrypt_block

def main():
    # Test vector from RFC 3713 for Camellia-128
    key_hex = "0123456789abcdeffedcba9876543210"
    plaintext_hex = "0123456789abcdeffedcba9876543210"
    expected_ciphertext_hex = "67673138549669730857065648eabe43"

    key = int(key_hex, 16)
    plaintext = int(plaintext_hex, 16)
    expected_ciphertext = int(expected_ciphertext_hex, 16)

    # Encrypt
    ciphertext = camellia_encrypt_block(plaintext, key)

    # Results
    print(f"Key:              {key_hex}")
    print(f"Plaintext:        {plaintext_hex}")
    print(f"Expected Cipher:  {expected_ciphertext_hex}")
    print(f"Computed Cipher:  {ciphertext:032x}")

    if ciphertext == expected_ciphertext:
        print("\n✅ Test Passed: Ciphertext matches expected output.")
    else:
        print("\n❌ Test Failed: Ciphertext does not match expected output.")

if __name__ == "__main__":
    main()