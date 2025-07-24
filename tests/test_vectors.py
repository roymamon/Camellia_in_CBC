import unittest
from camellia.camellia_core import camellia_encrypt_block, camellia_decrypt_block, camellia_encrypt_block_192, camellia_decrypt_block_192, camellia_encrypt_block_256, camellia_decrypt_block_256
from camellia.cbc_mode import cbc_encrypt, cbc_decrypt

#to run: python3 -m unittest tests.test_vectors

class CamelliaVectorTest(unittest.TestCase):

    def test_rfc3713_vector(self):
        key_hex = "0123456789abcdeffedcba9876543210"
        plaintext_hex = "0123456789abcdeffedcba9876543210"
        expected_ciphertext_hex = "67673138549669730857065648eabe43"

        key = int(key_hex, 16)
        plaintext = int(plaintext_hex, 16)
        expected_ciphertext = int(expected_ciphertext_hex, 16)

        ciphertext = camellia_encrypt_block(plaintext, key)
        self.assertEqual(ciphertext, expected_ciphertext,
                         f"Expected {expected_ciphertext_hex}, got {ciphertext:032x}")

    def test_rfc3713_vector_decrypt(self):
        key_hex = "0123456789abcdeffedcba9876543210"
        ciphertext_hex = "67673138549669730857065648eabe43"
        expected_plaintext_hex = "0123456789abcdeffedcba9876543210"

        key = int(key_hex, 16)
        ciphertext = int(ciphertext_hex, 16)
        expected_plaintext = int(expected_plaintext_hex, 16)

        decrypted = camellia_decrypt_block(ciphertext, key)
        self.assertEqual(decrypted, expected_plaintext,
                     f"Expected {expected_plaintext_hex}, got {decrypted:032x}")
    
    def test_rfc3713_vector_192(self):
        key_hex = "0123456789abcdeffedcba98765432100011223344556677"
        plaintext_hex = "0123456789abcdeffedcba9876543210"
        expected_ciphertext_hex = "b4993401b3e996f84ee5cee7d79b09b9"

        key = int(key_hex, 16)
        plaintext = int(plaintext_hex, 16)
        expected_ciphertext = int(expected_ciphertext_hex, 16)

        ciphertext = camellia_encrypt_block_192(plaintext, key)
        self.assertEqual(ciphertext, expected_ciphertext,
                      f"Expected {expected_ciphertext_hex}, got {ciphertext:032x}")
    
    def test_rfc3713_vector_192_decryption(self):
        key_hex = "0123456789abcdeffedcba98765432100011223344556677"
        plaintext_hex = "0123456789abcdeffedcba9876543210"
        expected_ciphertext_hex = "b4993401b3e996f84ee5cee7d79b09b9"

        key = int(key_hex, 16)
        expected_plaintext = int(plaintext_hex, 16)
        ciphertext = int(expected_ciphertext_hex, 16)

        decrypted = camellia_decrypt_block_192(ciphertext, key)

        self.assertEqual(decrypted, expected_plaintext,
            f"Expected {plaintext_hex}, got {decrypted:032x}")

    def test_rfc3713_vector_256(self):
        key_hex = (
            "0123456789abcdeffedcba9876543210"
            "00112233445566778899aabbccddeeff"
        )
        plaintext_hex = "0123456789abcdeffedcba9876543210"
        expected_ciphertext_hex = "9acc237dff16d76c20ef7c919e3a7509"

        key = int(key_hex, 16)
        plaintext = int(plaintext_hex, 16)
        expected_ciphertext = int(expected_ciphertext_hex, 16)

        ciphertext = camellia_encrypt_block_256(plaintext, key)
        self.assertEqual(ciphertext, expected_ciphertext,
                        f"Expected {expected_ciphertext_hex}, got {ciphertext:032x}")

    def test_rfc3713_vector_256_decrypt(self):
        key_hex = (
            "0123456789abcdeffedcba9876543210"
            "00112233445566778899aabbccddeeff"
        )
        ciphertext_hex = "9acc237dff16d76c20ef7c919e3a7509"
        expected_plaintext_hex = "0123456789abcdeffedcba9876543210"

        key = int(key_hex, 16)
        ciphertext = int(ciphertext_hex, 16)
        expected_plaintext = int(expected_plaintext_hex, 16)

        plaintext = camellia_decrypt_block_256(ciphertext, key)
        self.assertEqual(plaintext, expected_plaintext,
                        f"Expected {expected_plaintext_hex}, got {plaintext:032x}")

    #tests from: https://asecuritysite.com/hazmat/symcam

    def test_cbc_vector_hello_encrypt(self):
        key_hex = "f39fd9e02d78dc321ecc59692c22c3b3"
        iv_hex = "e88a6d70380f65346aeb79c39a20af88"
        expected_cipher_hex = "ad91a80f6385a3dca96b48aa533a88bf"

        key = int.from_bytes(bytes.fromhex(key_hex), 'big')
        iv = bytes.fromhex(iv_hex)
        plaintext = b"Hello"

        ciphertext = cbc_encrypt(plaintext, key, iv)
        self.assertEqual(ciphertext.hex(), expected_cipher_hex,
                         f"Expected {expected_cipher_hex}, got {ciphertext.hex()}")

    def test_cbc_vector_hello_decrypt(self):
        key_hex = "f39fd9e02d78dc321ecc59692c22c3b3"
        iv_hex = "e88a6d70380f65346aeb79c39a20af88"
        ciphertext_hex = "ad91a80f6385a3dca96b48aa533a88bf"
        expected_plaintext = b"Hello"

        key = int.from_bytes(bytes.fromhex(key_hex), 'big')
        iv = bytes.fromhex(iv_hex)
        ciphertext = bytes.fromhex(ciphertext_hex)

        decrypted = cbc_decrypt(ciphertext, key, iv)
        self.assertEqual(decrypted, expected_plaintext,
                         f"Expected {expected_plaintext}, got {decrypted}")

    def test_cbc_vector_roymamon_encrypt(self):
        key_hex = "e550f5ccfa9a19bcbe3e1ce9f1d9c5e7"
        iv_hex = "4f1cca5b4bcd5a4bb1114bef22f4d09b"
        expected_cipher_hex = "f2c0a611dc5eba72fb6fff55b75cf809"

        key = int.from_bytes(bytes.fromhex(key_hex), 'big')
        iv = bytes.fromhex(iv_hex)
        plaintext = b"RoyMamon"

        ciphertext = cbc_encrypt(plaintext, key, iv)
        self.assertEqual(ciphertext.hex(), expected_cipher_hex,
                         f"Expected {expected_cipher_hex}, got {ciphertext.hex()}")

    def test_cbc_vector_roymamon_decrypt(self):
        key_hex = "e550f5ccfa9a19bcbe3e1ce9f1d9c5e7"
        iv_hex = "4f1cca5b4bcd5a4bb1114bef22f4d09b"
        ciphertext_hex = "f2c0a611dc5eba72fb6fff55b75cf809"
        expected_plaintext = b"RoyMamon"

        key = int.from_bytes(bytes.fromhex(key_hex), 'big')
        iv = bytes.fromhex(iv_hex)
        ciphertext = bytes.fromhex(ciphertext_hex)

        decrypted = cbc_decrypt(ciphertext, key, iv)
        self.assertEqual(decrypted, expected_plaintext,
                         f"Expected {expected_plaintext}, got {decrypted}")


if __name__ == "__main__":
    unittest.main()