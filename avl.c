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
}

struct Noeud * clean(struct Noeud * root) {
    if (root->gauche != NULL) {
        clean(root->gauche);
    }
    if (root->droit != NULL) {
        clean(root->droit);
    }
    free(root);
    return NULL;
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
    //printf("noeud %i hauteur %i balance %i \n", noeud->val, hauteur(noeud), b);
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
    root = equilibre(root);
    return root;
}

int successeur(struct Noeud * root) {
    struct Noeud * noeud = root;
    while (noeud->gauche != NULL) noeud = noeud->gauche;
    return noeud->val;
}

struct Noeud * supprime(struct Noeud * root, int val) {
    if (val < root->val) {
        root->gauche = supprime(root->gauche, val);
        printf("supprime à gauche root = %d\n", root->val);
        infixe(root);
        printf("\n");
        maj(root);
        return equilibre(root);
    }
    else {
        if (val > root->val) {
        root->droit = supprime(root->droit, val);
        printf("supprime à droite root = %d\n", root->val);

        infixe(root);
            printf("\n");
        maj(root);
        return equilibre(root);
        }   
        else {
            //root->val = val : Le noeud à supprimer
            printf("supprime  %d\n", root->val);

            if ((root->gauche == NULL) & (root->droit == NULL)) {
                printf("feuille\n");
                free(root);
                return NULL;      //feuille
            }
            if (root->gauche == NULL) {
                printf("pas de gauche\n");
                struct Noeud * tmp = root->droit;
                free(root);
                return tmp;
            }   //un seul fils droit
            if (root->droit == NULL) {
                printf("pas de droit\n");
                struct Noeud * tmp = root->gauche;
                free(root);
                return tmp;
            }    //un seul fils gauche
            //cas général
            printf("cas general\n");
            int succ = successeur(root);
            root->val = succ;
            root->droit = supprime(root->droit, succ);
            printf("succ = %d\n", succ);
            infixe(root);
            printf("\n");
            maj(root);
            return equilibre(root);
            }
        }
    }


int main() {
    struct Noeud * root = (struct Noeud *) malloc(sizeof(struct Noeud));
    root->val = 0;
    root->gauche = NULL;
    root->droit = NULL;
    for (int i = 1; i < 8; i++) {
        root = insere(root, i);
    }
    infixe(root);
    printf("balance %i\n", balance(root));
    for (int i = 1; i < 2; i++) {
        printf("i = %i\n", i);
        root = supprime(root, i);
        infixe(root);
        printf("\n");
        printf("balance %i\n", balance(root));
    }
    
    clean(root);
    //free(root);
    return 0;
}
