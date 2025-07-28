#include <stdio.h>
#define _USE_MATH_DEFINES
#include <math.h>

// Firme delle funzioni per calcolare le aree con risultato in float
float area_quadrato_f(int);
float area_cerchio_f(int);
float area_triangolo_f(int);

// Firme delle funzioni per calcolare le aree con risultato in int
int area_quadrato(int);
int area_cerchio(int);
int area_triangolo(int);


int main()
{
    int n;
    float somma = 0.0;
    float media;

    // Chiedere all'utente quanti numeri vuole inserire
    printf("Quanti numeri vuoi inserire? ");
    scanf("%d", &n);

    // Controllo se n è positivo
    if (n < 3) {
        printf("Minimo richiesto 3.\n");
        return 1;
    }

    // Ciclo per inserire i numeri e calcolare la somma
    for (int i = 1; i <= n; i++) {
        float numero;
        printf("Inserisci il numero %d: ", i);
        scanf("%f", &numero);
        somma += numero;
    }

    // Calcolare la media
    media = somma / n;
    int media_i = (int)media;

    // Stampare il risultato
    printf("La media aritmetica (float) è: %.2f\n", media);
    printf("La media aritmetica (int) è: %d\n", media_i);
    printf("\n");
    printf("L'area del quadrato (float) è: %.2f\n", area_quadrato_f(media));
    printf("L'area del cerchio (float) è: %.2f\n", area_cerchio_f(media));
    printf("L'area del triangolo equilatero (float) è: %.2f\n", area_triangolo_f(media));
    printf("\n");
    printf("L'area del quadrato (int) è: %d\n", area_quadrato(media));
    printf("L'area del cerchio (int) è: %d\n", area_cerchio(media));
    printf("L'area del triangolo equilatero (int) è: %d\n", area_triangolo(media));

    return 0;
}

// Area del quadrato (float)
float area_quadrato_f(int D)
{
	// return D * D;
	return pow(D, 2);
}

// Area del cerchio (float)
float area_cerchio_f(int D) 
{
	// return (D / 2) * (D / 2) * M_PI;
	int raggio = D / 2;
	return pow(raggio, 2) * M_PI;
}

// Area del triangolo equilatero (float)
float area_triangolo_f(int D)
{
	return sqrt(3) / 4 * pow(D, 2);
}

// Area del quadrato (int)
int area_quadrato(int D)
{
	// return D * D;
	return pow(D, 2);
}

// Area del cerchio (int)
int area_cerchio(int D)
{
	// return (D / 2) * (D / 2) * M_PI;
	int raggio = D / 2;
	return pow(raggio, 2) * M_PI;
}

// Area del triangolo equilatero (int)
int area_triangolo(int D)
{
	return sqrt(3) / 4 * pow(D, 2);
}
