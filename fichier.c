#include <stdio.h>
#include <stdlib.h>

int longueur(char * chaine) {
    int cpt = 0;
    while (*chaine != 0) {
        cpt += 1;
        chaine += 1;
    }
    return cpt;
}

int mylog2(int n) {
    if (n == 0) return 1;
    int q = n;
    int cpt = 0;
    while (q != 0) {
        q = q / 10;
        cpt += 1;
    }
    return cpt;
}

void itos(int i, char * buf) {
    if (i == 0) {
        *buf = 48;
        return;
    }
    int n = mylog2(i);
    int q = i;
    int r;
    int j = 0;
    while (q != 0) {
        r = q % 10;
        q = q / 10;
        buf[n - j - 1] =  r + 48;
        printf("%s\n", buf);
        j ++;
    }
}

int main() {
    char * chaine = "message";
    printf("%d\n", longueur(chaine));
    printf("%s\n", chaine);
    FILE * sortie = fopen("essai.txt", "w+");
    fwrite(chaine, longueur(chaine), 1, sortie);
    fwrite("\n", 1, 1, sortie);
    fwrite(chaine, longueur(chaine), 1, sortie);
    for (int i = 0; i < 11; i++) {
        //printf("%c\n", i + 48);
    }
    fclose(sortie);
    int i = 123987;
    int n = mylog2(i);
    char conversion[n + 1];
    conversion[n] = 0;
    itos(i, conversion);
    printf("%s\n", conversion);
    return 0;
}