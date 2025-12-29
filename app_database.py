import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('devops.db')
cursor = conn.cursor()

print("--- Liste des outils DevOps en base ---")
cursor.execute("SELECT * FROM outils")
for row in cursor.fetchall():
    print(f"ID: {row[0]} | Outil: {row[1]} | Catégorie: {row[2]}")

conn.close()
