#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <unistd.h>
#include <string.h>


#ifndef DEFAULT_NAME
#define DEFAULT_NAME "~~~NOT SET~~~"
#endif

int game(char *user);

int main()
{

	char *intro = "Questo gioco consiste in una serie di domande a risposta multipla\nBuon divertimento!!\n";
	char *top_menu = "Cosa vuoi fare?\n\tA) Iniziare una nuova partita.\n\tB) Uscire dal gioco.";
	char scelta;
	char *user = DEFAULT_NAME;
	int score = 0;

	printf("%s\n", intro);

	while(true) {
		printf("%s\n", top_menu);
		printf("\nCosa scegli? ");
		scanf("%c", &scelta);
		// debug scelta
		// printf("%c\n", scelta);

		switch(tolower(scelta)) {
			case 'a':
				printf("Hai scelto di iniziare una nuova partita.\n");
				if (strcmp(user, DEFAULT_NAME)  == 0) {
					printf("Dimmi il tuo nome: ");
					user = malloc(512);
					scanf("%s", user);
					// debug user
					// printf("%s\n", user);
				}
				score += game(user);
				// Stampa il punteggio finale
				printf("PUNTEGGIO:\t%s => %d punti!\n", user, score);
				break;

			case 'b':
				printf("Hai scelto di uscire dal gioco con %d punti. Alla prossima!!\n", score);
				return 0;

			default:
				printf("Scelta non valida. Riprova.\n");
				// Esce con un errore se la scelta non è valida
				return 1;
		}
		// Pulisce il buffer di input, questo ciclo while vuoto onsuma i caratteri rimanenti nel buffer
		while(getchar() != '\n');

	}


	return 0;
}


int game(char *user)
{
	int score = 0;

	printf("Benvenuto nel gioco %s!\n", user);
	printf("Iniziamo...\n");
    // Array di domande
    char *domande[] = {
        "Qual è la funzione principale di un antivirus?\n\tA) Navigare in internet\n\tB) Proteggere il computer da virus e malware\n\tC) Creare documenti\n\tD) Riprodurre video",
        "Cosa significa \"phishing\"?\n\tA) Un tipo di attacco informatico per rubare dati sensibili\n\tB) Un software per migliorare la sicurezza\n\tC) Un metodo di crittografia\n\tD) Un programma di gestione delle password",
        "Quale di queste è una buona pratica per creare una password sicura?\n\tA) Usare la data di nascita\n\tB) Usare una combinazione di lettere, numeri e simboli\n\tC) Usare la stessa password per tutti i siti\n\tD) Usare la data di nascita del proprio cane",
        "Cosa dovresti fare se ricevi un'email sospetta da un mittente sconosciuto?\n\tA) Aprire l'email e cliccare su tutti i link\n\tB) Ignorare l'email e cancellarla\n\tC) Rispondere all'email per chiedere chiarimenti\n\tD) Inoltrare l'email a tutti i tuoi contatti",
        "Che cosa intendiamo con il termine \"firewall\"?A) Un programma per modificare immagini\n\tB) Un sistema di sicurezza che controlla il traffico di rete\n\tC) Un tipo di virus informatico\n\tD) Un'app per la gestione delle email"
    };

    // Array di risposte corrette (opzionale, per gestire le risposte)
    char *risposteCorrette[] = {
        "B",
        "A",
        "B",
        "B",
        "B" 
    };

    // Ciclo per iterare tra le domande. Parto da 0 come l'indice dell'array
    for (int i = 0; i < 4; ++i)
    {
        printf("\n%s\n", domande[i]);
        char risposta[2];
        printf("Inserisci la tua risposta (A, B, C, D): ");
        scanf("%1s", risposta); // Leggo solo un carattere

        // Controllo se la risposta è corretta
        if (toupper(risposta[0]) == risposteCorrette[i][0])
        {
            printf("Risposta corretta!\n");
			// Aggiungo punti per la risposta corretta
            score += 2;
        }
        else
        {
            printf("Risposta sbagliata. La risposta corretta era %s.\n", risposteCorrette[i]);
             // Tolgo un punto per la risposta sbagliata.
            score -= 1;
        }
    }

	return score;
}
