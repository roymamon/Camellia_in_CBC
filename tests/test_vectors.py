import unittest
from camellia.camellia_core import camellia_encrypt_block

class CamelliaVectorTest(unittest.TestCase):
    def test_rfc3713_vector(self):
        #test vector from RFC 3713
        key_hex = "0123456789abcdeffedcba9876543210"
        plaintext_hex = "0123456789abcdeffedcba9876543210"
        expected_ciphertext_hex = "67673138549669730857065648eabe43"

        key = int(key_hex, 16)
        plaintext = int(plaintext_hex, 16)
        expected_ciphertext = int(expected_ciphertext_hex, 16)

        ciphertext = camellia_encrypt_block(plaintext, key)
        self.assertEqual(ciphertext, expected_ciphertext, 
                         f"Expected {expected_ciphertext_hex}, got {ciphertext:032x}")

if __name__ == "__main__":
    unittest.main()