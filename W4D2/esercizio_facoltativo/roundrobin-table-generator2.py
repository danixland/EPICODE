#! /usr/bin/env python

# importo la libreria csv 
import csv

### le mie variabili
# dizionario dei processi
proclist = {}
# tempo di esecuzione per ogni ciclo
cycle = 12
# il ciclo parte da 0
cycle_start = 0

try:
	# leggo il file e lo processo
	with open("processes.txt") as procfile:
		reader = csv.reader(procfile, dialect='unix')
		# estraggo indice e contenuto di ogni riga
		for i, line in enumerate(reader):
			# creo il nome del processo
			pi = i + 1
			process = "P" + str(pi)
			# creo il contenuto delle variabili t0 e tx 
			arrival = line[0]
			exec_time = line[1]
			# popolo il dizionario con la lista dei processi
			proclist[process] = {}
			# e per ogni processo aggiungo t0 e tx e tr (time remaining)
			proclist[process].update({"t0": int(arrival)})
			proclist[process].update({"tx": int(exec_time)})
			proclist[process].update({"tr": int(exec_time)})
except:
	print("I was unable to open the file")
finally:
	# chiudo il file in lettura visto che non serve tenerlo in memoria
	procfile.close()

# tempo generale trascorso, questa variabile si aggiorna ad ogni ciclo ed è inizializzata al tempo 0
time_elapsed = cycle_start
# contatore per i cicli (parte da 1)
exec_cycle = 1

# stampo l'header della tabella
print(f'Ciclo\t| t0\t| end\t| proc')

while True:
	for proc in proclist:
		# estraiamo i tempi per facilità
		t0 = proclist[proc]["t0"]
		tx = proclist[proc]["tx"]
		tr = proclist[proc]["tr"]

		# se t0 è inferiore al tempo trascorso e il tempo rimanenete è maggiore di 0
		if t0 <= time_elapsed and 0 < tr:
			# verifichiamo quanto tempo ci rimane del processo corrente
			if 0 < tr >= cycle:
				tr = tr - cycle
				proclist[proc].update({"tr": int(tr)})
				print(f'{exec_cycle}\t| {time_elapsed}\t| {time_elapsed + cycle}\t| {proc}')
				time_elapsed = time_elapsed + cycle
			elif 0 < tr < cycle:
				proclist[proc].update({"tr": 0})
				print(f'{exec_cycle}\t| {time_elapsed}\t| {time_elapsed + tr}\t| {proc} -> END')
				time_elapsed = time_elapsed + tr
			# aumentiamo il contatore dei cicli
			exec_cycle = exec_cycle + 1

	# Controllo se tutti i valori di tr sono 0 ed eventualmente esco
	if all(p["tr"] == 0 for p in proclist.values()):
	    break

