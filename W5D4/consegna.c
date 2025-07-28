#include <stdio.h>
#define _USE_MATH_DEFINES
#include <math.h>

// Firme delle funzioni per calcolare le aree
float area_quadrato(int);
float area_cerchio(int);
float area_triangolo(int);

int main()
{
	int D;
	printf("Inserisci un numero: ");
	scanf("%d", &D);

	printf("\nL'area del quadrato è: %.2f", area_quadrato(D) );
	printf("\nL'area del cerchio è: %.2f", area_cerchio(D) );
	printf("\nL'area del triangolo è: %.2f", area_triangolo(D) );

	printf("\n\n");

	return 0;
}

// Area del quadrato
float area_quadrato(int D)
{
	// return D * D;
	return pow(D, 2);
}

// Area del cerchio
float area_cerchio(int D) 
{
	// return (D / 2) * (D / 2) * M_PI;
	int raggio = D / 2;
	return pow(raggio, 2) * M_PI;
}

// Area del triangolo equilatero
float area_triangolo(int D)
{
	return sqrt(3) / 4 * pow(D, 2);
}
