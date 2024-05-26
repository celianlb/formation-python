# Exercice : Ecrire les fonctions de calculs (addition, multiplication, soustraction, division, modulo) en utilisant un paramètre de fonction


dictionnaire = {
     "personnes": {
         "Alice": {"âge": 25, "ville": "Paris"},
         "Bob": {"âge": 30, "ville": "Lyon"},
         "Charlie": {"âge": 35, "ville": "Marseille"}
     }
}

# Extraire les âges des personnes et les afficher
for personne, age in dictionnaire["personnes"].items():
     print(f"L'âge de {personne} est de {age['âge']} ans.")

# # Affiche :
# # L'âge de Alice est de 25 ans.
# # L'âge de Bob est de 30 ans.