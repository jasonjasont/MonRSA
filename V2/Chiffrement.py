import random
import math
import base64
from math import gcd

def is_prime(n):
    """Vérifie si un nombre est premier."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_large_prime():
    """Génère un grand nombre premier de 10 chiffres."""
    attempts = 0
    max_attempts = 1000  # Limite le nombre de tentatives pour trouver un nombre premier
    while attempts < max_attempts:
        num = random.randint(10**9, 10**10 - 1)
        if is_prime(num):
            return num
        attempts += 1
    raise Exception("Impossible de générer un grand nombre premier après plusieurs tentatives.")

def extended_gcd(a, b):
    """Algorithme d'Euclide étendu pour trouver l'inverse modulaire."""
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def mod_inverse(a, m):
    """Calcule l'inverse modulaire de 'a' modulo 'm'."""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError("Aucun inverse modulaire trouvé")
    return x % m

def generate_keys():
    """Génère une paire de clés RSA."""
    print("Génération des clés RSA...")
    p = generate_large_prime()
    print(f"Nombre premier p généré : {p}")
    q = generate_large_prime()
    print(f"Nombre premier q généré : {q}")

    while p == q:
        q = generate_large_prime()
        print(f"Nombre premier q régénéré : {q}")

    n = p * q
    phi = (p - 1) * (q - 1)
    print(f"Calcul de n = p * q : {n}")
    print(f"Calcul de phi = (p - 1) * (q - 1) : {phi}")

    # Utiliser des valeurs couramment utilisées pour e
    common_es = [3, 5, 17, 257, 65537]
    e, d = None, None

    for potential_e in common_es:
        if potential_e < phi and gcd(potential_e, phi) == 1:
            try:
                potential_d = mod_inverse(potential_e, phi)
                if potential_e != potential_d and (potential_e * potential_d) % phi == 1:
                    e, d = potential_e, potential_d
                    e_hex = hex(e)[2:]
                    d_hex = hex(d)[2:]
                    if len(e_hex) == len(d_hex):  # Vérifier que e et d ont la même longueur
                        print(f"Valeurs trouvées : e = {e}, d = {d}")
                        break
            except ValueError:
                continue

    if e is None or d is None:
        raise Exception("Impossible de trouver e et d.")

    # Convertir les clés en hexadécimal
    e_hex = hex(e)[2:]
    d_hex = hex(d)[2:]
    n_hex = hex(n)[2:]

    # Demander à l'utilisateur le nom des fichiers de clé
    pub_key_filename = input("Entrez le nom du fichier pour la clé publique (par défaut 'monRSA.pub') : ") or "monRSA.pub"
    priv_key_filename = input("Entrez le nom du fichier pour la clé privée (par défaut 'monRSA.priv') : ") or "monRSA.priv"

    # Sauvegarder les clés dans des fichiers
    with open(pub_key_filename, "w") as pub_file:
        pub_file.write(f"---begin monRSA public key---\n")
        pub_file.write(base64.b64encode(f"0x{n_hex}\n0x{e_hex}".encode()).decode() + "\n")
        pub_file.write(f"---end monRSA key---\n")
        print(f"Clé publique sauvegardée dans '{pub_key_filename}'")

    with open(priv_key_filename, "w") as priv_file:
        priv_file.write(f"---begin monRSA private key---\n")
        priv_file.write(base64.b64encode(f"0x{n_hex}\n0x{d_hex}".encode()).decode() + "\n")
        priv_file.write(f"---end monRSA key---\n")
        print(f"Clé privée sauvegardée dans '{priv_key_filename}'")

    # Afficher les valeurs pour validation
    print(f"p: {p}")
    print(f"q: {q}")
    print(f"n: {n}")
    print(f"nPrime: {phi}")
    print(f"e: {e}")
    print(f"d: {d}")

    print("Clés générées avec succès !")
    print(f"Clé publique : (e={e_hex}, n={n_hex})")
    print(f"Clé privée : (d={d_hex}, n={n_hex})")

def encrypt_message(message):
    """Chiffre un message avec la clé publique."""
    try:
        with open("monRSA.pub", "r") as pub_file:
            pub_file.readline()  # Skip the first line
            encoded_keys = pub_file.readline().strip()
            decoded_keys = base64.b64decode(encoded_keys).decode().split("\n")
            n = int(decoded_keys[0], 16)
            e = int(decoded_keys[1], 16)
            print(f"Clé publique lue : n = {n}, e = {e}")
    except FileNotFoundError:
        print("Erreur : Fichier de clé publique introuvable. Générer les clés d'abord.")
        return

    # Convertir le message en ASCII
    ascii_values = [ord(char) for char in message]
    print(f"Valeurs ASCII : {ascii_values}")

    # Créer des blocs de taille 3 caractères ASCII, chaque bloc commence et finit par '0'
    blocks = []
    for i in range(0, len(ascii_values), 3):
        block = "0"
        for j in range(3):
            if i + j < len(ascii_values):
                block += str(ascii_values[i + j]).zfill(3)
        block += "0"
        blocks.append(block)
    print(f"Blocs à chiffrer : {blocks}")

    # Chiffrer chaque bloc
    encrypted_blocks = [str(pow(int(block), e, n)) for block in blocks]
    print(f"Blocs chiffrés : {encrypted_blocks}")

    # Convertir les blocs chiffrés en Base64
    encrypted_message = base64.b64encode(" ".join(encrypted_blocks).encode()).decode()
    print(f"Message chiffré en Base64 : {encrypted_message}")

    with open("encrypted_message.txt", "w") as enc_file:
        enc_file.write(encrypted_message)

    print("Message chiffré et sauvegardé dans 'encrypted_message.txt'.")