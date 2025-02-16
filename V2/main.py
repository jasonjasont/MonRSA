import sys
from chiffrement import generate_keys, encrypt_message
from dechiffrement import decrypt_message


def main():
    if len(sys.argv) < 2:
        print("Usage :")
        print("  python main.py generate_keys")
        print("  python main.py encrypt 'votre message'")
        print("  python main.py decrypt")
        sys.exit(1)

    command = sys.argv[1]

    if command == "generate_keys":
        generate_keys()
    elif command == "encrypt":
        if len(sys.argv) < 3:
            print("Erreur : spécifiez un message à chiffrer.")
            sys.exit(1)
        message = sys.argv[2]
        encrypt_message(message)
    elif command == "decrypt":
        decrypt_message()
    else:
        print("Commande inconnue :", command)
        sys.exit(1)


if __name__ == "__main__":
    main()