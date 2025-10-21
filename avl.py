from graphviz import Graph

class Avl:
    def __init__(avl, nom):
        avl.nom = nom
        avl.fils_gauche = None
        avl.fils_droit = None
        avl.hauteur = 1

    

    

    

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
        
def rotation_gauche_gauche(avl):
    b = avl.fils_gauche
    avl.fils_gauche = b.fils_droit
    avl.hauteur = 1 + max(hauteur(avl.fils_droit), hauteur(avl.fils_gauche))
    b.fils_droit = avl
    b.hauteur = 1 + max(hauteur(b.fils_droit), hauteur(b.fils_gauche))
    return b

def rotation_droite_droite(avl):
    c = avl.fils_droit
    avl.fils_droit = c.fils_gauche
    avl.hauteur = 1 + max(hauteur(avl.fils_droit), hauteur(avl.fils_gauche))
    c.fils_gauche = avl
    c.hauteur = 1 + max(hauteur(c.fils_droit), hauteur(c.fils_gauche))
    return c

def rotation_droite_gauche(avl):
    avl.fils_gauche = rotation_droite_droite(avl.fils_gauche)
    avl.hauteur = 1 + max(hauteur(avl.fils_droit), hauteur(avl.fils_gauche))
    return rotation_gauche_gauche(avl)

def rotation_gauche_droite(avl):
    avl.fils_droit = rotation_gauche_gauche(avl.fils_droit)
    avl.hauteur = 1 + max(hauteur(avl.fils_droit), hauteur(avl.fils_gauche))
    return rotation_droite_droite(avl)

def hauteur(avl):
    return 0 if avl is None else avl.hauteur

def dico_hauteur(avl):
    if avl is None:
        return {}
    dico = {avl.nom: avl.hauteur}
    dico.update(dico_hauteur(avl.fils_gauche))
    dico.update(dico_hauteur(avl.fils_droit))
    return dico

def insert(avl, valeur):
    if valeur == avl.nom:
        return avl
    if valeur < avl.nom:
        if avl.fils_gauche is None:
            avl.fils_gauche = Avl(valeur)
        else:
            avl.fils_gauche = insert(avl.fils_gauche,valeur)
    else:
        if avl.fils_droit is None:
            avl.fils_droit = Avl(valeur)
        else:
            avl.fils_droit = insert(avl.fils_droit, valeur)
    avl.hauteur = 1 + max(hauteur(avl.fils_droit), hauteur(avl.fils_gauche))

    balance = hauteur(avl.fils_droit) - hauteur(avl.fils_gauche)
    if balance == -2:
        balance_gauche = hauteur(avl.fils_gauche.fils_droit) - hauteur(avl.fils_gauche.fils_gauche)
        if balance_gauche < 0:
            avl = rotation_gauche_gauche(avl)
        else:
            avl = rotation_droite_gauche(avl)
    if balance == 2:
        balance_droite = hauteur(avl.fils_droit.fils_droit) - hauteur(avl.fils_droit.fils_gauche)
        if balance_droite > 0:
            avl = rotation_droite_droite(avl)
        else:
            avl = rotation_gauche_droite(avl)

    avl.hauteur = 1 + max(hauteur(avl.fils_droit), hauteur(avl.fils_gauche))
    return avl
    

"""
a = Avl("a")
b = Avl("b")
c = Avl("c")
d = Avl("d")
e = Avl("e")
a.fils_gauche = b
a.fils_droit = c
c.fils_gauche = d
c.fils_droit = e

#affiche(a)
#affiche(rotation_gauche_gauche(a))
affiche(rotation_droite_droite(a))

a50 = Avl(50)
a20 = Avl(20)
a25 = Avl(25)
a10 = Avl(10)
a30 = Avl(30)
a40 = Avl(40)
a50 = Avl(50)
a70 = Avl(70)
a50.fils_gauche = a20
a50.fils_droit = a70
a20.fils_gauche = a10
a20.fils_droit = a30
a30.fils_gauche = a25
a30.fils_droit = a40
avl = a50
avl = rotation_droite_gauche(avl)
avl = rotation_gauche_droite(avl)
#avl = rotation_gauche_gauche(avl)
#avl = rotation_droite_droite(avl)
"""
avl = Avl(0)
for i in range(-1, -10, -1):
    avl = insert(avl, i)
affiche(avl)
print(dico_hauteur(avl))

