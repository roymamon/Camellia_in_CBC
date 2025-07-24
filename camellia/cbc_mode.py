from .camellia_core import camellia_encrypt_block, camellia_decrypt_block


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

def unpad_pkcs7(padded: bytes, block_size: int = 16) -> bytes:
    pad_len = padded[-1]
    if not (1 <= pad_len <= block_size):
        raise ValueError("Invalid PKCS#7 padding")
    if padded[-pad_len:] != bytes([pad_len] * pad_len):
        raise ValueError("Invalid PKCS#7 padding content")
    return padded[:-pad_len]

def cbc_decrypt(ciphertext: bytes, key: int, iv: bytes) -> bytes:
    block_size = 16
    assert len(iv) == block_size, "IV must be 16 bytes"
    assert len(ciphertext) % block_size == 0, "Ciphertext must be a multiple of 16 bytes"

    plaintext = b''
    previous_block = int.from_bytes(iv, byteorder='big')

    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i+block_size]
        block_int = int.from_bytes(block, byteorder='big')

        decrypted = camellia_decrypt_block(block_int, key)
        plain_block_int = decrypted ^ previous_block
        plain_block = plain_block_int.to_bytes(block_size, byteorder='big')

        plaintext += plain_block
        previous_block = block_int

    return unpad_pkcs7(plaintext, block_size)
