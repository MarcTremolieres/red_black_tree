from graphviz import Graph
from math import inf

class Nil:
    def __init__(self):
        self.parent = None
        self.couleur = "black"
        self.nil = True
        self.valeur = "NIL"

class Node:
    def __init__(self, valeur):
        self.valeur = valeur
        self.fils_gauche = Nil()
        self.fils_droit = Nil()
        self.fils_gauche.parent = self
        self.fils_droit.parent = self
        self.parent = None
        self.couleur = "red"
        self.nil = False

    def set_fils_gauche(self, noeud):
        self.fils_gauche = noeud
        noeud.parent = self

    def set_fils_droit(self, noeud):
        self.fils_droit = noeud
        noeud.parent = self

    def get_node(self, valeur):
        if valeur == self.valeur:
            return self
        if valeur < self.valeur:
            if self.fils_gauche.nil:
                return None
            return self.fils_gauche.get_node(valeur)
        if self.fils_droit.nil:
            return None
        return self.fils_droit.get_node(valeur)

    def topologie(self):
        liste_nodes = []
        liste_aretes = []
        liste_nodes.append((str(self.valeur), self.couleur))
        if not self.fils_gauche.nil:
            arete = (str(self.valeur), str(self.fils_gauche.valeur))
            if not(arete in liste_aretes):
                liste_aretes.append(arete)
            liste_n, liste_a = self.fils_gauche.topologie()
            liste_nodes = liste_nodes + liste_n
            liste_aretes = liste_aretes + liste_a
        if not self.fils_droit.nil:
            arete = (str(self.valeur), str(self.fils_droit.valeur))
            if not(arete in liste_aretes) and not((arete[1], arete[0]) in liste_aretes):
                liste_aretes.append(arete)
            liste_n, liste_a = self.fils_droit.topologie()
            liste_nodes = liste_nodes + liste_n
            liste_aretes = liste_aretes + liste_a
        return liste_nodes, liste_aretes

    def affiche(self, nom):
        graph = Graph()
        liste_nodes, liste_aretes = self.topologie()
        for node in liste_nodes:
            graph.node(node[0], color=node[1])
        for arete in liste_aretes:
            graph.edge(arete[0], arete[1])
        graph.render(str(nom), view=True, format='png')

    def hauteur(self):
        if (self.fils_gauche == None) and (self.fils_droit == None):
            return 1
        if self.fils_gauche.nil:
            return 1 + self.fils_droit.hauteur()
        if self.fils_droit.nil:
            return 1 + self.fils_gauche.hauteur()
        return 1 + max(self.fils_gauche.hauteur(), self.fils_droit.hauteur())

    def taille(self):
        if self.fils_gauche.nil and self.fils_droit.nil:
            return 1
        if self.fils_gauche.nil:
            return 1 + self.fils_droit.taille()
        if self.fils_droit.nil:
            return 1 + self.fils_gauche.taille()
        return 1 + self.fils_gauche.taille() + self.fils_droit.taille()

    def noeud_minimum(self):
        if self.fils_gauche.nil:
            return self
        return self.fils_gauche.noeud_minimum()

    def noeud_maximum(self):
        if self.fils_droit.nil:
            return self
        return self.fils_droit.noeud_maximum()

    def recherche(self, valeur):
        if self.valeur == valeur:
            return True
        if valeur < self.valeur:
            if not self.fils_gauche.nil:
                return self.fils_gauche.recherche(valeur)
            return False
        else:
            if not self.fils_droit.nil:
                return self.fils_droit.recherche(valeur)
        return False

    def rotation_droite(self, arbre):
        print("rotation droite ", arbre.valeur)
        if not arbre.fils_gauche.nil:
            pere = arbre.parent
            if pere.valeur < arbre.valeur:
                pere.set_fils_droit(arbre.fils_gauche)
                arbre.set_fils_gauche(pere.fils_droit.fils_droit)
                pere.fils_droit.set_fils_droit(arbre)
            else:
                pere.set_fils_gauche(arbre.fils_gauche)
                arbre.set_fils_gauche(pere.fils_gauche.fils_droit)
                pere.fils_gauche.set_fils_droit(arbre)

    def rotation_gauche(self, arbre):
        print("rotation gauche ", arbre.valeur)
        if not arbre.fils_droit.nil:
            pere = arbre.parent
            if pere.valeur < arbre.valeur:
                pere.set_fils_droit(arbre.fils_droit)
                arbre.set_fils_droit(pere.fils_droit.fils_gauche)
                pere.fils_droit.set_fils_gauche(arbre)
            else:
                pere.set_fils_gauche(arbre.fils_droit)
                arbre.set_fils_droit(pere.fils_gauche.fils_gauche)
                pere.fils_gauche.set_fils_gauche(arbre)

    def insertion(self, noeud):
        if self.valeur == noeud.valeur:
            return
        if self.valeur > noeud.valeur:
            if self.fils_gauche.nil:
                self.set_fils_gauche(noeud)
            else:
                self.fils_gauche.insertion(noeud)
        if self.valeur < noeud.valeur:
            if self.fils_droit.nil:
                self.set_fils_droit(noeud)
            else:
                self.fils_droit.insertion(noeud)


class Red_black_tree:
    def __init__(self, valeur):
        self.root = Node(valeur)
        self.root.couleur = "black"
        self.fils_gauche = None
        self.fils_droit = None

    def set_fils_gauche(self, noeud):
        self.root.set_fils_gauche(noeud)

    def set_fils_droit(self, noeud):
        self.root.set_fils_droit(noeud)

    def rotation_droite(self, noeud):
        if noeud != self.root:
            self.root.rotation_droite(noeud)
        else:
            tmp_root = Node(inf)
            tmp_root.set_fils_gauche(self.root)
            tmp_root.rotation_droite(self.root)
            self.root = tmp_root.fils_gauche

    def rotation_gauche(self, noeud):
        if noeud != self.root:
            self.root.rotation_gauche(noeud)
        else:
            tmp_root = Node(inf)
            tmp_root.set_fils_gauche(self.root)
            tmp_root.rotation_gauche(self.root)
            self.root = tmp_root.fils_gauche

    def fix_tree(self, noeud):
        print("fixing ", noeud.valeur)
        def oncle(noeud):
            pere = noeud.parent
            papy = pere.parent
            if papy.valeur > pere.valeur:
                return papy.fils_droit
            else:
                return papy.fils_gauche
        if noeud == self.root:
            noeud.couleur = "black"
            return
        pere = noeud.parent
        if pere.couleur == "black":
            return
        if pere != self.root:
            papy = pere.parent
            tonton = oncle(noeud)
            if tonton.couleur == "red":
                pere.couleur = "black"
                tonton.couleur = "black"
                papy.couleur = "red"
                self.fix_tree(papy)
            else:
                if noeud.valeur < pere.valeur:
                    if pere.valeur < papy.valeur:
                        pere.couleur = "black"
                        papy.couleur = "red"
                        self.rotation_droite(papy)
                    else:
                        noeud.couleur = "black"
                        papy.couleur = "red"
                        self.rotation_droite(pere)
                        self.rotation_gauche(papy)
                else:
                    if papy.valeur < pere.valeur:
                        pere.couleur = "black"
                        papy.couleur = "red"
                        self.rotation_gauche(papy)
                    else:
                        noeud.couleur = "black"
                        papy.couleur = "red"
                        self.rotation_gauche(pere)
                        self.rotation_droite(papy)

    def insert(self, valeur):
        noeud = Node(valeur)
        if self.root is None:
            self.root = noeud
            self.root.couleur = "black"
        else:
            self.root.insertion(noeud)
#            self.affiche('self')
            self.fix_tree(noeud)

    def affiche(self, nb):
        self.root.affiche(nb)

    '''def transplante(self, valeur_a_supprimer, valeur_remplacante):
        noeud_a_supprimer = self.root.get_node(valeur_a_supprimer)
        noeud_remplacant = self.root.get_node(valeur_remplacante)
        if noeud_a_supprimer == self.root:
            self.root = noeud_remplacant
        elif noeud_a_supprimer == noeud_a_supprimer.parent.fils_gauche:
            noeud_a_supprimer.parent.fils_gauche = noeud_remplacant
        else:
            noeud_a_supprimer.parent.fils_droit = noeud_remplacant
        if noeud_remplacant == noeud_remplacant.parent.fils_gauche:
            noeud_remplacant.parent.fils_gauche = None
        else:
            noeud_remplacant.parent.fils_droit = None
        noeud_remplacant.parent = noeud_a_supprimer.parent'''


    def echange_valeurs(self, valeur1, valeur2):
        noeud1 = self.root.get_node(valeur1)
        noeud2 = self.root.get_node(valeur2)
        noeud1.valeur, noeud2.valeur = noeud2.valeur, noeud1.valeur


    def echange_noeuds(self, noeud1, noeud2):
        noeud1.valeur, noeud2.valeur = noeud2.valeur, noeud1.valeur

    def supprime_valeur(self, valeur):
        noeud = self.root.get_node(valeur)
        self.supprime(noeud)


    def remove_root(self):
        print("removing ROOT valeur ", self.root.valeur)
        if self.root.fils_gauche.nil:
            if self.root.fils_droit.nil:
                self.root.valeur = None
                return
            else:
                self.root = self.root.fils_droit
                return
        elif self.root.fils_droit.nil:
            self.root = self.root.fils_droit
            return
        else:
            remplacant = self.root.fils_droit.noeud_minimum()
            self.echange_noeuds(self.root, remplacant)
            self.supprime(remplacant)


    def supprime(self, noeud: Node):
        print("removing ", noeud.valeur, noeud.couleur)
        couleur = noeud.couleur
        if noeud == self.root:
            self.remove_root()
            return
        parent = noeud.parent
        gauche = (parent.fils_gauche == noeud)

        if noeud.fils_gauche.nil:
            if gauche:
                parent.fils_gauche = noeud.fils_droit
                parent.fils_gauche.parent = parent
                if (parent.fils_gauche.couleur == "black") and (couleur == "black"):
                    self.fix_remove(parent.fils_gauche)
                else:
                    parent.fils_gauche.couleur = "black"

            else:
                parent.fils_droit = noeud.fils_droit
                parent.fils_droit.parent = parent
                if (parent.fils_gauche.couleur == "black") and (couleur == "black"):
                    self.fix_remove(parent.fils_droit)
                else:
                    parent.fils_droit.couleur = "black"


        elif noeud.fils_droit.nil:
            if gauche:
                parent.fils_gauche = noeud.fils_gauche
                parent.fils_gauche.parent = parent
                if (couleur == "black") and (parent.fils_gauche.couleur == "black"):
                    self.fix_remove(parent.fils_gauche)
                parent.fils_gauche.couleur = "black"
            else:
                parent.fils_droit = noeud.fils_gauche
                parent.fils_droit.parent = parent
                if (couleur == "black") and (parent.fils_droit.couleur == "black"):
                    self.fix_remove(parent.fils_droit)
                parent.fils_droit.couleur = "black"
        else:       #Le noeud à supprimer possède deux fils
            remplacant = noeud.fils_droit.noeud_minimum()
            self.echange_noeuds(noeud, remplacant)
            self.supprime(remplacant)       #On rappelle supprime avec un noeud qui a au plus un fils

    def fix_remove(self, noeud):
        print("fixing noeud ", noeud.valeur)
        arbre.affiche("fixing " + str(noeud.valeur))
        if noeud == self.root:
            return
        if noeud.couleur == "red":
            return
        parent = noeud.parent
        gauche = (parent.fils_gauche == noeud)
        if gauche:
            frere = parent.fils_droit
        else:
            frere = parent.fils_gauche
        if frere.couleur == "red":      #Le frere est red
            if gauche:
                print("rotation")
                parent.couleur = "red"
                frere.couleur = "black"
                self.rotation_gauche(parent)
                self.fix_remove(noeud)
            else:
                print("rotation droite")
                parent.couleur = "red"
                frere.couleur = "black"
                self.rotation_droite(parent)
                self.fix_remove(noeud)
            return

        if frere.couleur == "black":    #Le frère est black
            if (frere.fils_gauche.couleur == "black" and frere.fils_droit.couleur == "black"):
                if parent.couleur == "red":  # Le parent est rouge
                    parent.couleur = "black"
                    if not frere.nil:
                        frere.couleur = "red"
                    return
                # Le parent est black
                else:
                    if not frere.nil:
                        frere.couleur = "red"
                    self.fix_remove(parent)
                    return
            #Un des neveux est rouge, il y a 6 cas !
            if gauche:
                if frere.fils_droit.couleur == "black":  # Neveu exterieur black
                    frere.fils_gauche.couleur = "black"
                    frere.couleur = "red"
                    self.rotation_droite(frere)
                    self.fix_remove(noeud)
                    return
                else:           #Neveu exterieur red
                    frere.couleur = parent.couleur
                    parent.couleur = "black"
                    frere.fils_droit.couleur = "black"
                    self.rotation_gauche(parent)
                    return
            else:
                if frere.fils_gauche.couleur == "black":  # Neveu exterieur black
                    frere.fils_droit.couleur = "black"
                    frere.couleur = "red"
                    self.rotation_gauche(frere)
                    self.fix_remove(noeud)
                    return
                if frere.fils_gauche.couleur == "red":
                    frere.couleur = parent.couleur
                    parent.couleur = "black"
                    frere.fils_gauche.couleur = "black"
                    self.rotation_droite(parent)
                    return



if __name__ == "__main__":
    arbre = Red_black_tree(0)
    for nombre in range(40, 0, -1):
        arbre.insert(3 * nombre)
        arbre.insert(-3 * nombre)
    arbre.insert(25)
    arbre.insert(56)
    arbre.insert(26)
    arbre.insert(55)

    arbre.affiche(1)
    print("arbre construit")

    arbre.supprime_valeur(69)
    arbre.affiche(2)

#    arbre.supprime_valeur(26)
#    arbre.affiche(3)

