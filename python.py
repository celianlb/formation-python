# Les variables en python sont des objets qui peuvent contenir des valeurs de différents types.
# Les variables sont typés dynamiquement, c'est à dire qu'on ne spécifie pas le type de la variable lors de sa déclaration.
# Les types de variables les plus courants sont les suivants:

nombre = 10 # integer (nombre)
nom = "John" # string (chaine de caractère)
liste = [1, 2, 3] # liste (ensemble de valeurs)
dictionnaire = {"nom": "John", "age": 30} # dictionnaire (ensemble de clés/valeurs)
dictionnaire = {
    "personnes": {
        "John": {"âge": 25, "ville": "Paris"},
        "Alice": {"âge": 30, "ville": "Lyon"}
    }
} # dictionnaire imbriqué
tuple = (1, "brique", 3) # tuple (ensemble de valeurs immuable)
ensemble = {1, 2, 3} # ensemble (ensemble de valeurs uniques)
flottant = 10.5 # float (nombre à virgule flottante)
booleen = True # boolean (vrai/faux)


# Opérateurs arithmétiques
# Les opérateurs arithmétiques de base sont les suivants:

# Addition
addition = 5 + 2 # 7
# Soustraction
soustraction = 5 - 2 # 3
# Multiplication
multiplication = 5 * 2 # 10
# Division
division = 5 / 2 # 2.5
# Division entière
division_entiere = 5 // 2 # 2
# Modulo
modulo = 5 % 2 # 1
# Puissance
puissance = 5 ** 2 # 25


# Opérateurs de comparaison
# Les opérateurs de comparaison permettent de comparer des valeurs et renvoient un booléen (True ou False) en fonction du résultat de la comparaison.

# Égalité
egalite = 5 == 2 # False
# Différence
difference = 5 != 2 # True
# Supérieur
superieur = 5 > 2 # True
# Inférieur
inferieur = 5 < 2 # False
# Supérieur ou égal
superieur_egal = 5 >= 2 # True
# Inférieur ou égal
inferieur_egal = 5 <= 2 # False


# Opérateurs logiques
# Les opérateurs logiques permettent de combiner des expressions booléennes.

# ET logique
et = True and False # False
# OU logique
ou = True or False # True
# NON logique
non = not True # False


# Structures de contrôle
# Les structures de contrôle permettent de contrôler le flux d'exécution du programme.

# Condition if
if 5 > 2:
    print("5 est supérieur à 2")
# Condition if/else
if 5 < 2:
    print("5 est inférieur à 2")
else:
    print("5 n'est pas inférieur à 2")
# Condition if/elif/else
if 5 < 2:
    print("5 est inférieur à 2")
elif 5 == 2:
    print("5 est égal à 2")
else:
    print("5 n'est ni inférieur ni égal à 2")
# Boucle for
for i in range(5):
    print(i)
# Boucle while
i = 0

while i < 5:
    print(i)
    i += 1


# Fonctions
# Les fonctions permettent de regrouper des instructions et de les réutiliser à différents endroits du programme.

def addition(a, b):
    res = a + b
    print(res)
    return res

resultat = addition(5, 2) # 7
print(resultat)