import sys
import os
import glob
from chiffrement import generate_keys, encrypt_message
from dechiffrement import decrypt_message

def reset_files():
    """Supprime les fichiers de clés et de messages chiffrés."""
    files_to_delete = glob.glob("*.pub") + glob.glob("*.priv") + glob.glob("*.txt")
    for file in files_to_delete:
        try:
            os.remove(file)
            print(f"Fichier '{file}' supprimé.")
        except FileNotFoundError:
            print(f"Fichier '{file}' introuvable.")
        except Exception as e:
            print(f"Erreur lors de la suppression du fichier '{file}': {e}")

def main():
    while True:
        print("\nMenu :")
        print("1. Générer une clé")
        print("2. Chiffrer un message")
        print("3. Déchiffrer un message")
        print("4. Réinitialiser (supprimer les clés et les messages chiffrés)")
        print("5. Quitter")
        
        choice = input("Choisissez une option (1-5) : ")

        if choice == "1":
            generate_keys()
        elif choice == "2":
            message = input("Entrez le message à chiffrer : ")
            encrypt_message(message)
        elif choice == "3":
            decrypt_message()
        elif choice == "4":
            reset_files()
        elif choice == "5":
            print("Au revoir!")
            sys.exit(0)
        else:
            print("Option invalide. Veuillez choisir une option entre 1 et 5.")

if __name__ == "__main__":
    main()