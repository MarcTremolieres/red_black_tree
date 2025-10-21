from graphviz import Graph

class Avl:
    def __init__(self, nom):
        self.nom = nom
        self.fils_gauche = None
        self.fils_droit = None
        self.balance = 0

    def liste_aretes(self):
        liste = []
        if self.fils_gauche is not None:
            liste.append((str(self.nom) + " / " + str(self.balance), str(self.fils_gauche.nom) + " / " + str(self.fils_gauche.balance)))
            liste += self.fils_gauche.liste_aretes()
        if self.fils_droit is not None:
            liste.append((str(self.nom) + " / " + str(self.balance), str(self.fils_droit.nom) + " / " + str(self.fils_droit.balance) ))
            liste += self.fils_droit.liste_aretes()
        return liste

    def affiche(self):
        graph = Graph()
        graph.edges(self.liste_aretes())
        graph.render(view=True)

    def rotation_gauche_gauche(self):
        a = self
        b = self.fils_gauche
        c = self.fils_gauche.fils_gauche
        d = self.fils_gauche.fils_droit
        e = self.fils_droit
        self.fils_gauche = d
        b.fils_droit = self
        self = b
        self.affiche()

    def insert(self, valeur):
        if valeur == self.nom:
            return
        if valeur < self.nom:
            if self.fils_gauche is None:
                self.fils_gauche = Avl(valeur)
            else:
                self.fils_gauche.insert(valeur)
            self.balance -= 1
        else:
            if self.fils_droit is None:
                self.fils_droit = Avl(valeur)
            else:
                self.fils_droit.insert(valeur)
            self.balance += 1
        if self.balance == -2:
            if self.fils_gauche.balance < 0:
                self.rotation_gauche_gauche()
            else:
                self.rotation_droite_gauche()
        if self.balance == 2:
            if self.fils_droit.balance > 0:
                self.rotation_droite_droite()
            else:
                self.rotation_gauche_droite()

    
        
        
"""
a = Avl("a")
b = Avl("b")
c = Avl("c")
d = Avl("d")
e = Avl("e")
a.fils_gauche = b
a.fils_droit = e
b.fils_gauche = c
b.fils_droit = d

a.rotation_gauche_gauche()
#b.affiche()
"""
a = Avl(0)
for i in range(-1, -5, -1):
    a.insert(i)

