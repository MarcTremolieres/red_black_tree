from graphviz import Graph

class Avl:
    def __init__(avl, nom):
        avl.nom = nom
        avl.fils_gauche = None
        avl.fils_droit = None
        avl.hauteur = 1

    def feuille(self):
        return self.fils_gauche is None and self.fils_droit is None

def liste_aretes(avl):
    liste = []
    if avl.fils_gauche is not None:
        liste.append((str(avl.nom), str(avl.fils_gauche.nom)))
        liste += liste_aretes(avl.fils_gauche)
    if avl.fils_droit is not None:
        liste.append((str(avl.nom), str(avl.fils_droit.nom) ))
        liste += liste_aretes(avl.fils_droit)
    return liste

def affiche(avl):
    graph = Graph()
    graph.edges(liste_aretes(avl))
    graph.render(view=True)
        
def rotation_gauche(avl):
    b = avl.fils_gauche
    avl.fils_gauche = b.fils_droit
    maj(avl)
    b.fils_droit = avl
    maj(b)
    return b

def rotation_droite(avl):
    c = avl.fils_droit
    avl.fils_droit = c.fils_gauche
    maj(avl)
    c.fils_gauche = avl
    maj(c)
    return c

def hauteur(avl):
    return 0 if avl is None else avl.hauteur

def dico_hauteur(avl):
    if avl is None:
        return {}
    dico = {avl.nom: avl.hauteur}
    dico.update(dico_hauteur(avl.fils_gauche))
    dico.update(dico_hauteur(avl.fils_droit))
    return dico

def balance(avl):
    return hauteur(avl.fils_droit) - hauteur(avl.fils_gauche)

def maj(avl):
    avl.hauteur = 1 + max(hauteur(avl.fils_droit), hauteur(avl.fils_gauche))

def equilibre(avl):
    if balance(avl) == -2:
        if balance(avl.fils_gauche) > 0:
            avl.fils_gauche = rotation_droite(avl.fils_gauche)
        avl = rotation_gauche(avl)
    if balance(avl) == 2:
        if balance(avl.fils_droit) <0:
            avl.fils_droit = rotation_gauche(avl.fils_droit)
        avl = rotation_droite(avl)
    maj(avl)
    return avl

def insert(avl, valeur):
    if avl is None:
        return Avl(valeur)
    if valeur == avl.nom:
        return avl
    if valeur < avl.nom:
        avl.fils_gauche = insert(avl.fils_gauche, valeur)
    else:
        avl.fils_droit = insert(avl.fils_droit, valeur)
    maj(avl)
    return equilibre(avl)

def recherche(avl, valeur):
    "renvoie le sous arbre ayant valeur pour racine. Si il n'existe pas renvoie None"
    if avl is None:
        return avl
    if valeur == avl.nom:
        return avl
    if valeur < avl.nom:
        return recherche(avl.fils_gauche, valeur)
    else:
        return recherche(avl.fils_droit, valeur)

def successeur(avl):
    "renvoie le successeur inorder de la racine, None si il n'y a pas de fils droit"
    if avl.fils_droit is None:
        return None
    succ = avl.fils_droit
    while succ.fils_gauche is not None:
        succ = succ.fils_gauche
    return succ


def supprime(avl, valeur):
    if avl is None:
        return None
    if valeur < avl.nom:
        avl.fils_gauche = supprime(avl.fils_gauche, valeur)
    elif valeur > avl.nom:
        avl.fils_droit = supprime(avl.fils_droit, valeur)
    else:
        if avl.feuille():
            return None
        elif avl.fils_droit is None:
            return avl.fils_gauche
        elif avl.fils_gauche is None:
            return avl.fils_droit
        else:
            succ = successeur(avl)
            avl.nom = succ.nom
            avl.fils_droit = supprime(avl.fils_droit, avl.nom)
    maj(avl)
 
    return equilibre(avl)


avl = Avl(0)
for i in range(1, 50):
    avl = insert(avl, i)
affiche(avl)
input()
for i in range(1, 50,):
    print(i)
    avl = supprime(avl, i)
    affiche(avl)
    input()



