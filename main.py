import SpawnKey
import Chiffrement

def main():
    SpawnKey.spawn_key()
    encrypted_message = Chiffrement.chiffrement()

 # Enregistrement de la clé publique
    with open('clé_public', 'w') as file:
        file.write(encrypted_message)


if __name__ == "__main__":
    main()