#include <stdio.h>
#include <stdlib.h>

struct Noeud {
    int val ;
    struct Noeud * gauche ;
    struct Noeud * droit ;
    int hauteur;
};

void infixe(struct Noeud * root) {
    int * parcours;
    if (root->gauche != NULL) {
        infixe(root->gauche);
    }
    printf("%i ( %i ) ", root->val, root->hauteur);
    if (root->droit != NULL) {
        infixe(root->droit);
    }
    free(root);
}

int hauteur(struct Noeud * noeud) {
    return (noeud == NULL ? 0: noeud->hauteur);
}

void maj(struct Noeud * noeud) {
    if (hauteur(noeud->gauche) > hauteur(noeud->droit)) {
        noeud->hauteur = 1 + hauteur(noeud->gauche);
    }
    else {
        noeud->hauteur = 1 + hauteur(noeud->droit);
    }
}


int balance(struct Noeud * noeud) {
    return hauteur(noeud->droit) - hauteur(noeud->gauche);
}


struct Noeud * rotation_droite(struct Noeud * noeud) {
    if (noeud->droit == NULL) return noeud;
    struct Noeud * tmp = noeud->droit;
    noeud->droit = tmp->gauche;
    maj(noeud);
    tmp->gauche = noeud;
    maj(tmp);
    return tmp;
}

struct Noeud * rotation_gauche(struct Noeud * noeud) {
    if (noeud->gauche == NULL) return noeud;
    struct Noeud * tmp = noeud->gauche;
    noeud->gauche = tmp->droit;
    maj(noeud);
    tmp->droit = noeud;
    maj(tmp);
    return tmp;
}


struct Noeud * equilibre(struct Noeud * noeud) {
    int b = balance(noeud);
    if (b == -2) {
        if (balance(noeud->gauche) > 0) {
            noeud->gauche = rotation_droite(noeud->gauche);
            maj(noeud->gauche);
        }
        noeud = rotation_gauche(noeud);
        maj(noeud);
    }
    if (b == 2) {
        if (balance(noeud->droit) < 0) {
            noeud->droit = rotation_gauche(noeud->droit);
            maj(noeud->droit);
        }
        noeud = rotation_droite(noeud);
        maj(noeud);
    }
    return noeud;
}

struct Noeud * insere(struct Noeud * root, int val) {
    if (root == NULL) {
        struct Noeud * feuille = (struct Noeud *) malloc(sizeof(struct Noeud));
        feuille->val = val;
        feuille->gauche = NULL;
        feuille->droit = NULL;
        feuille->hauteur = 1;
        return feuille;
    }
    if (val < root->val) {
        root->gauche = insere(root->gauche, val);
    }
    else if (val > root->val) {
        root->droit = insere(root->droit, val);
    }
    maj(root);
//    return equilibre(root);
    return root;
}

int main() {
    /*
    struct Noeud n1 = {1, NULL, NULL};
    struct Noeud n6 = {6, NULL, NULL};
    struct Noeud n2 = {2, &n1, &n6};
    struct Noeud n5 = {5, NULL, NULL};
    struct Noeud n4 = {4, NULL, &n5};
    struct Noeud n3 = {3, &n2, &n4};

    infixe(&n3);
    printf("\n");
    */
    struct Noeud * root = (struct Noeud *) malloc(sizeof(struct Noeud));
    root->val = -5;
    root->gauche = NULL;
    root->droit = NULL;
    for (int i = 0; i < 2; i++) {
        root = insere(root, i);
//        root = insere(root, -i);
    }
    infixe(root);
    printf("\n");
    struct Noeud * root2 = (struct Noeud *) malloc(sizeof(struct Noeud));
    root2->val = -5;
    root2->gauche = NULL;
    root2->droit = NULL;
    for (int i = 0; i < 2; i++) {
        root2 = insere(root2, i);
    }
    root2 = rotation_droite(root2);
    infixe(root2);
    printf("\n");
    return 0;
}