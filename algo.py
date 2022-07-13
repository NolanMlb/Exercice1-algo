import random

# Création des constantes
longueur = 8
min = 0
max = 20

# Création de la liste avec 8 nombres aléatoires compris entre 0 et 20
L = random.sample(range(min,max), longueur)

# Tri de la liste
LL = sorted(L)


# Affichage
print(L)
print(LL)