from camellia.camellia_core import camellia_encrypt_block

key = int("0123456789abcdeffedcba9876543210", 16)
plaintext = int("0123456789abcdeffedcba9876543210", 16)
expected = "67673138549669730857065648eabe43"

cipher = camellia_encrypt_block(plaintext, key)
print("Ciphertext:", f"{cipher:032x}")
print("Match:", expected == f"{cipher:032x}")