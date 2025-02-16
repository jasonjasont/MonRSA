import SpawnKey
import base64

def encrypt_block(block, e, n):
    return pow(block, e, n)

# décimal vers ascii
def encrypt_message(message, e, n):
    block_size = len(str(n)) - 1
    ascii_message = int(''.join(f'{ord(c):03}' for c in message))
    blocks = []

    while ascii_message > 0:
        blocks.append(ascii_message % (10 ** block_size))
        ascii_message //= 10 ** block_size

    blocks.reverse()
    encrypted_blocks = [encrypt_block(block, e, n) for block in blocks]
    encrypted_message = ''.join(f'{block:0{block_size}d}' for block in encrypted_blocks)
    
    ascii_encoded = ''.join(chr(int(encrypted_message[i:i+3])) for i in range(0, len(encrypted_message), 3))
    base64_encoded = base64.b64encode(ascii_encoded.encode()).decode()
    
    return base64_encoded

#Récupération des clef et chiffrement de la clé publique
def chiffrement():
    public_key, private_key = SpawnKey.spawn_key()
    e, n = public_key
    print("Clé publique : ", public_key)
    print("Clé privée : ", private_key)

    message = "initialisation"
    encrypted_message = encrypt_message(message, e, n)
    print(f"Message chiffré : {encrypted_message}")
    
    return encrypted_message

