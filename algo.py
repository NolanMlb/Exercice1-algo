import random

def nb_list_tri():
# Création des constantes
    longueur = 8
    min = 0
    max = 20

# Création de la liste avec 8 nombres aléatoires compris entre 0 et 20
    L = random.sample(range(min,max), longueur)

# Tri de la liste
    LL = sorted(L)

# Affichage
    print(LL)

# On génére le nombre aléatoire, on l'ajoute au tableau et on le trie
    random_nb = random.randint(min,max)
    print(random_nb)

    def DPMR(LL,random_nb):
        if LL[0] == random_nb :
          return 0
        else:
         return 1 + DPMR(LL[1:], random_nb)

    # LL.append(random_nb)
    # LL.sort()

# Affichage
    print(LL)
    # print("Index : ", index)

nb_list_tri()
