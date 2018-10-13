eleves = 17                   # variable
print(eleves)                 # utilise la fonction print pour afficher la variable "eleves"
 
eleves = eleves + 1       # ajoute 1 à la variable eleves
print(eleves)
 
def ajouter_eleves(n):      # définition d'une fonction avec un paramètre
    global eleves
    eleves = eleves + n
    print(eleves)

ajouter_eleves(5)
ajouter_eleves(8)
 
liste_eleves = []
liste_eleves.append("Martine")
liste_eleves.append("Nicolas")
liste_eleves.append("Pimprenelle")
 
for eleve in liste_eleves:        # On parcourt la liste des élèves et on affiche chaque eleve
    print(eleve)