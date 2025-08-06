#! /usr/bin/env python3

# W6D4 - esercizio

# Si scriva un programma in Python che in base alla scelta dellʼutente 
# permetta di calcolare il perimetro di diverse figure geometriche
# (scegliete pure quelle che volete voi). 
# Per la risoluzione dellʼesercizio abbiamo scelto:
# 	- Quadrato (perimetro = lato*4
# 	- Cerchio (circonferenza = 2*pi greco*r)
# 	- Rettangolo (perimetro= base*2 + altezza*2

import math

intro = """Questo script calcolerà il perimetro di diverse figure geometriche
utilizzando la lunghezza del segmento immesso dall'utente.
"""
print(intro)
scelta = int(input(f"\nInserisci la lunghezza del segmento: "))

def perimetro_quadrato(lato:int) -> int:
	return 4 * lato

def perimetro_cerchio(lato:int) -> float:
	# definiamo quanti decimali vogliamo in ritorno
	dec = 2
	pi = math.pi
	return round(pi * float(lato) * 2.0, dec)

def perimetro_rettangolo(lato:int) -> int:
	# per il rettangolo ipotizziamo che la base sia 2*altezza
	b = lato
	h = 2*b

	return (2 * b) + (2 * h)

print(f"il perimetro del Quadrato è: {perimetro_quadrato(scelta)} cm")
print(f"il perimetro del Cerchio è: {perimetro_cerchio(scelta)} cm")
print(f"il perimetro del Rettangolo è: {perimetro_rettangolo(scelta)} cm")
