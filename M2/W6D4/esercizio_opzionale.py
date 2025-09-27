#! /usr/bin/env python3

# Si adatti il precedente esercizio in modo che acquisisca da tastiera il valore
# immesso dallʼutente, calcoli il perimetro e lʼarea di una figura geometrica 
# scelta dallʼutente, e utilizzi automaticamente il valore dellʼarea come 
# valore per calcolare il perimetro e lʼarea della prossima figura geometrica
# scelta nuovamente dallʼutente.
# Creare dunque una selezione multipla di figure da proporre allʼutente
# ad ogni nuovo calcolo. 
#
# - Il valore iniziale viene immesso dallʼutente solo la prima volta allo
#	start del software. 
# - Ogni volta che lʼutente seleziona una figura, questa viene tolta dalle
#	 prossime opzioni presentate. 
#
# Ripetere il procedimento per almeno 3 figure geometriche
# (es. quadrato, rettangolo, cerchio).

import math

intro = "Questo script calcolerà il perimetro e l'area di diverse figure geometriche utilizzando la lunghezza del segmento immesso dall'utente."
expl = "Adesso ti verranno proposte diverse figure geometriche che potrai selezionare per calcolarne il perimetro e l'area. Lascia vuota la scelta per uscire dal programma."

figures_list = ["Quadrato",
"Cerchio",
"Triangolo equilatero",
"Pentagono",
"Rettangolo (base = 2*altezza)"
]

def calcolo_perimetro(fig:int, seg:int):
	pi = math.pi
	dec = 2
	# la funzione accetta in input l'indice della figura (in base alla lista)
	# e la lunghezza del segmento inserita dall'utente.
	# ho arrotondato arbitrariamente a 2 cifre decimali.

	figl = figures_list[fig].lower()

	match figl:
		case "quadrato":
			# quadrato
			perimetro = 4 * seg
		case "cerchio":
			# cerchio
			perimetro = round(2 * pi * seg, dec)
		case "triangolo equilatero":
			# Triangolo equilatero
			perimetro = 3 * seg
		case "pentagono":
			# pentagono
			perimetro = 5 * seg
		case rettangolo:
			# rettangolo
			# arbitrariamente ho deciso che la base e 2 volte l'altezza
			h = seg
			b = 2 * seg
			perimetro = (2 * b) + (2 * h)

	return perimetro

def calcolo_area(fig:int, seg:int):
	pi = math.pi
	dec = 2
	# la funzione accetta in input l'indice della figura (in base alla lista)
	# e la lunghezza del segmento inserita dall'utente.
	# ho arrotondato arbitrariamente a 2 cifre decimali.

	figl = figures_list[fig].lower()

	match figl:
		case "quadrato":
			# quadrato
			area = seg ** 2
		case "cerchio":
			# cerchio
			area = round(pi * (seg ** 2), dec)
		case g if "triangolo" in g:
			# Triangolo equilatero
			area = round((math.sqrt(3) / 4) * (seg ** 2), dec)
		case "pentagono":
			# pentagono
			# dobbiamo calcolare l'apotema che non ho idea di cosa sia
			# (geometria questa sconosciuta)
			# ma per fortuna le formule si trovano online :)
			apotema = seg / (2 * math.tan(pi / 5))
			area = round(0.5 * (5 * seg) * apotema, dec)
		case g if "rettangolo" in g:
			# rettangolo
			# arbitrariamente ho deciso che la base e 2 volte l'altezza
			h = seg
			b = 2 * seg
			area = b * h

	return area


def main():
	print(intro)
	segmento = int(input(f"\nInserisci la lunghezza del segmento: "))

	print(expl)
	s = segmento
	while True:
		print(f"\n")
		for i, el in enumerate(figures_list, 1):
			print(f"{i}) {el}")

		figura = input(f"\nQuale figura geometrica vuoi calcolare? ")

		# selezioniamo la figura in base all'input dell'utente.
		# se non inserisce nulla, usciamo dal programma. Se inserisce un valore
		# inatteso, riproponiamo la domanda.
		if not figura:
			print("Esco dal programma.")
			break
		elif 1 <= int(figura) <= len(figures_list):
			figura_scelta = int(figura) - 1
			a = calcolo_area(figura_scelta, s)
			p = calcolo_perimetro(figura_scelta, s)
			print(f"\n\t**** {figures_list[figura_scelta]} with segment [{s}] ****")
			print(f"\tL'area della figura è {a}")
			print(f"\tIl perimetro della figura è {p}")
			# riassegno s al valore di a
			s = a
			print(f"\n\tsegment is now {a}")
			# rimuovo la figura dalla lista.
			figures_list.pop(figura_scelta)
			if figures_list:
				print(f"\n{'-' * 50}")
				print(f"\tRestano {len(figures_list)} figure.")
				print(f"{'-' * 50}")
			else:
				print(f"\n{'-' * 50}")
				print(f"\tHai esaurito le figure.")
				print(f"{'-' * 50}")
				break
		else:
			print("devi scegliere tra le figure proposte.")


if __name__ == '__main__':
	main()
