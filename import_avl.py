from graphviz import Graph

avl = Graph()
aretes = []
f = open("avl.txt", "r")
for ligne in f.readlines():
    deb, fin = ligne[:-1].split(sep=",")
    avl.edge(deb, fin)
f.close()
avl.render(view=True)


