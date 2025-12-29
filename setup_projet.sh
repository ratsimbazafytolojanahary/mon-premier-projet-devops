#!/bin/bash
echo "Configuration de mon nouveau projet..."
mkdir projet_auto
cd projet_auto
git init
touch main.py
echo "print('Hello DevOps')" > main.py
git add .
git commit -m "Initialisation automatique"
echo "Le projet est prêt et git est initialisé !"

