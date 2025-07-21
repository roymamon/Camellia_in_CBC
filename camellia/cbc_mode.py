from .camellia_core import camellia_encrypt_block

BLOCK_SIZE = 16  # 128 bits

def pkcs7_pad(data: bytes) -> bytes:
    padding_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + bytes([padding_len] * padding_len)

def xor_blocks(b1: bytes, b2: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(b1, b2))

def cbc_encrypt(plaintext: bytes, key: int, iv: int) -> bytes:
    plaintext = pkcs7_pad(plaintext)
    ciphertext = b""
    prev_block = iv.to_bytes(BLOCK_SIZE, byteorder='big')

    for i in range(0, len(plaintext), BLOCK_SIZE):
        block = plaintext[i:i + BLOCK_SIZE]
        xored = xor_blocks(block, prev_block)
        block_int = int.from_bytes(xored, byteorder='big')
        encrypted_int = camellia_encrypt_block(block_int, key)
        encrypted_block = encrypted_int.to_bytes(BLOCK_SIZE, byteorder='big')
        ciphertext += encrypted_block
        prev_block = encrypted_block

    return ciphertext