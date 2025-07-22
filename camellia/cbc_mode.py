from camellia.camellia_core import camellia_encrypt_block

def pad_pkcs7(data: bytes, block_size: int = 16) -> bytes:
    padding_len = block_size - (len(data) % block_size)
    return data + bytes([padding_len] * padding_len)

def cbc_encrypt(plaintext: bytes, key: int, iv: bytes) -> bytes:
    block_size = 16
    assert len(iv) == block_size, "IV must be 16 bytes (128 bits)"
    
    padded = pad_pkcs7(plaintext, block_size)
    ciphertext = b''
    previous_block = int.from_bytes(iv, byteorder='big')

    for i in range(0, len(padded), block_size):
        block = padded[i:i+block_size]
        block_int = int.from_bytes(block, byteorder='big')
        xor_block = block_int ^ previous_block
        encrypted_block = camellia_encrypt_block(xor_block, key)
        ciphertext += encrypted_block.to_bytes(block_size, byteorder='big')
        previous_block = encrypted_block

    return ciphertext