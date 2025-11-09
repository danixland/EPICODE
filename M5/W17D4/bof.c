#include <stdio.h>
#include <string.h>

/*
	TEST SUL BUFFER OVERFLOW
	la variabile buffer viene inizializzata con un valore di 10 Bytes
	ma inserendo una stringa superiore a quella dimensione ci restituisce
	l'errore di segmentation fault.
*/
int main()
{
	/*
	aumentare la dimensione del buffer non ci protegge
	dal buffer overflow in quanto basterà inserire una stringa più lunga
	per ottenere lo stesso errore.
	*/
	char buffer [10];

	printf("Inserire il nome utente: ");
	/*
	Invece di utilizzare una funzione scanf() che non è sicura in quanto non 
	ci permette di specificare la lunghezza del buffer in ingresso, utilizziamo
	fgets() per limitare la lunghezza della stringa inserita.
	*/
	// scanf("%s", buffer);
	fgets(buffer, sizeof(buffer), stdin);

	/*
	Sanitizziamo la stringa inserita, rimuovendo il newline "\n" e sostituendolo
	con il null operator. In questo modo ci assicuriamo che al massimo 9 caratteri
	vengano inseriti nel buffer, e cioè uno meno della dimensione impostata. Evitiamo
	così il rischio di buffer overflow.
	*/
	size_t len = strlen(buffer);
	if (len > 0 && buffer[len - 1] == '\n') {
		buffer[len - 1] = '\0';
	}

	printf("Nome utente inserito: %s\n", buffer);
	return 0;
}
