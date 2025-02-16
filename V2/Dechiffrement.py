import base64

def decrypt_message():
    """Déchiffre un message avec la clé privée."""
    try:
        with open("monRSA.priv", "r") as priv_file:
            priv_file.readline()  # Skip the first line
            encoded_keys = priv_file.readline().strip()
            decoded_keys = base64.b64decode(encoded_keys).decode().split("\n")
            n = int(decoded_keys[0], 16)
            d = int(decoded_keys[1], 16)
            print(f"Clé privée lue : n = {n}, d = {d}")
    except FileNotFoundError:
        print("Erreur : Fichier de clé privée introuvable. Générer les clés d'abord.")
        return

    try:
        with open("encrypted_message.txt", "r") as enc_file:
            encrypted_message = enc_file.read()
            print(f"Message chiffré lu : {encrypted_message}")
    except FileNotFoundError:
        print("Erreur : Fichier de message chiffré introuvable.")
        return

    # Décoder le message Base64
    encrypted_blocks = base64.b64decode(encrypted_message).decode().split()
    print(f"Blocs chiffrés : {encrypted_blocks}")

    # Déchiffrer chaque bloc
    decrypted_blocks = [str(pow(int(block), d, n)).zfill(len(str(n)) - 1) for block in encrypted_blocks]
    print(f"Blocs déchiffrés : {decrypted_blocks}")

    # Convertir les blocs déchiffrés en caractères ASCII
    decrypted_message = ""
    for block in decrypted_blocks:
        for i in range(0, len(block), 3):
            char_code = int(block[i:i+3])
            if 32 <= char_code <= 126:  # Ignorer les zéros non significatifs et les caractères non imprimables
                decrypted_message += chr(char_code)
    print(f"Message déchiffré intermédiaire : {decrypted_message}")

    print("Message déchiffré :", decrypted_message)