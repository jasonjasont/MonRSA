#!/bin/bash

# Vérifier le système d'exploitation
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Système d'exploitation détecté : Linux"
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip
elif [[ "$OSTYPE" == "msys" ]]; then
    echo "Système d'exploitation détecté : Windows"
    choco install python
else
    echo "Système d'exploitation non supporté"
    exit 1
fi

# Installer les dépendances Python
pip3 install -r requirements.txt

echo "Installation des dépendances terminée."
