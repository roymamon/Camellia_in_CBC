import unittest
from camellia.camellia_core import camellia_encrypt_block
from camellia.cbc_mode import cbc_encrypt

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

    def test_cbc_vector(self):
    #from https://asecuritysite.com/hazmat/symcam
        key_hex = "f39fd9e02d78dc321ecc59692c22c3b3"
        iv_hex = "e88a6d70380f65346aeb79c39a20af88"
        expected_cipher_hex = "ad91a80f6385a3dca96b48aa533a88bf"

        key = int.from_bytes(bytes.fromhex(key_hex), 'big')
        iv = bytes.fromhex(iv_hex)
        plaintext = b"Hello"

        ciphertext = cbc_encrypt(plaintext, key, iv)
        actual_cipher_hex = ciphertext.hex()

        self.assertEqual(actual_cipher_hex, expected_cipher_hex,
                         f"Expected {expected_cipher_hex}, got {actual_cipher_hex}")

if __name__ == "__main__":
    unittest.main()