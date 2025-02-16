import base64

def base64_decode(data):
    return base64.b64decode(data)

def ascii_encode(data):
    return ''.join(chr(b) for b in data)

def decrypt_block(C, d, n):
    return pow(C, d, n)

def split_blocks(data, block_size):
    return [data[i:i + block_size] for i in range(0, len(data), block_size)]

def decrypt_message(encrypted_message, d, n):
    # Etape 1: Décoder le message
    decoded_message = base64_decode(encrypted_message)
    ascii_encoded_message = ascii_encode(decoded_message)
    
    # Etape 2: Diviser le message en blocs
    block_size = len(str(n)) - 1
    blocks = split_blocks(ascii_encoded_message, block_size)
    
    # Etape 3 : Déchiffrer les blocs
    decrypted_blocks = [decrypt_block(int(block), d, n) for block in blocks]
    
    # Etape 4: Reconstruire le message
    decrypted_message = ''.join(chr(int(str(block)[i:i+3])) for block in decrypted_blocks for i in range(0, len(str(block)), 3))
    
    return decrypted_message

# Example usage
n = 3233  # Example modulus
d = 2753  # Example private exponent
encrypted_message = "SGVsbG8gd29ybGQ="  # Example Base64 encoded message

decrypted_message = decrypt_message(encrypted_message, d, n)
print("Decrypted message:", decrypted_message)