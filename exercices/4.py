# Exercice : Créer une classe Personne avec des attributs et des méthodes, puis une sous-classe Etudiant.

# Créer une classe Personne avec des attributs et des méthodes, puis une sous-classe Etudiant.
class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def afficher(self):
        print(f"Nom : {self.nom}, Prénom : {self.prenom}, Age : {self.age}")

class Etudiant(Personne):
    def __init__(self, nom, prenom, age, classe):
        super().__init__(nom, prenom, age)
        self.classe = classe

    def afficher(self):
        super().afficher()
        print(f"Classe : {self.classe}")

# Créer une instance de la classe Personne
personne = Personne("Dupont", "Jean", 30)
personne.afficher()

# Créer une instance de la classe Etudiant
etudiant = Etudiant("Durand", "Alice", 25, "3ème")
etudiant.afficher()
