#! /usr/bin/env python

"""
wordlen.py 		Script che riceve un numero sulla riga di comando e restituisce una lista di parole casuali
				e la loro relativa lunghezza.
				Usa il dizionario /usr/share/dict/words per generare la lista di parole oppure, se questo non è presente
				nel sistema, usa una lista di 10 parole predefinite. 
				L'argomento n può essere qualsiasi numero intero > 0 se il file è presente, altrimenti dovrà essere <= 10.
"""

import argparse
import os
from random import randint, seed, choice
from time import time

worddict = "/usr/share/dict/words"
my_words = ["epicode", "is", "the", "best", "Danilo", "very", "smart", "CyberSecurity", "hacker", "ethical"]

def list_words(n):
	# words è la lista che restituiremo alla fine
	words = []
	if not os.path.isfile(worddict):   # se il file non esiste
		if 10 <= n:
			n = 10

		print("Il file di dizionario non è presente nel sistema, utilizzerò 10 parole che conosco. :)")
		while len(words) < n:
			word = choice(my_words)
			if word not in words:
				words.append(word)
	else:
		with open(worddict, 'r') as f:
			lines = f.readlines()  # readlines legge tutto il file in memoria
			lines = [line.strip() for line in lines]  # rimuovo i \n con strip

		# uso il tempo attuale in millisecondi come seed per la funzione random, in questo modo le
		# parole selezionate saranno sempre diverse ad ogni esecuzione del programma. 
		seed(int(time() * 1000))
		while len(words) < n:
			# randint restituisce un numero random tra 2 estremi, in questo caso 0 e la lunghezza massima del file
			i = randint(0, len(lines) - 1)
			# 
			if lines[i] not in words:
				words.append(lines[i])

	return words
    
def main():
	parser = argparse.ArgumentParser(description="Genera una lista di parole casuali prese dal file /usr/share/dict/words se presente, altrimenti utilizzerà una lista di 10 parole predefinite.", usage="wordlen.py [-h] <numero di parole>")
	parser.add_argument('n', type=int, help="Numero di parole da utilizzare")
	args = parser.parse_args()
	count = args.n
	if not os.path.isfile(worddict):   # check if file exists
		if 10 <= count:
			count = 10

	result = list_words(count)
	lengths = [len(word) for word in result]  # calculate length of each word

	print(f"La lista di parole selezionata è:\n{result}")
	print(f"La lunghezza di ogni parola è\n{lengths}")

	print("\t### Visualizzazione Alternativa ###")

	for i in range(count):
		print("{} -->\t {} caratteri".format(result[i], lengths[i]))

if __name__ == "__main__":
	main()
