#! /bin/bash

# \ \        / ___|   __ \ _ |                   |                   |           |                  _)             
#  \ \  \   /  __ \   |   |  |                   __ \    _` |   __|  __ \        __ \    _` |   __|  |   __|   __| 
#   \ \  \ /     ) |  |   |  |      _____|       |   |  (   | \__ \  | | |       |   |  (   | \__ \  |  (    \__ \ 
#    \_/\_/   ____/  ____/  _|                  _.__/  \__._| ____/ _| |_|      _.__/  \__._| ____/ _| \___| ____/ 

# W5D1 - dimostrazione base di bash scripting

# Vogliamo ottenere un albero di directory simile a questo:
# W5D1_bash-demo
#	├── dos
#	├── studenti
#	│	├── anna
#	│	│	└── casa
#	│	├── matteo
#	│	│	└── amici
#	│	└── nicola
#	│		├── lavoro
#	│		└── scuola
#	│			├── compito.doc
#	│			└── relazione.doc
#	├── tmp
#	│	└── risultati.doc
#	└── windows
# 
# Su cui poi andremo ad operare per spostare files, modificarli o eliminarli
# utilizzando diversi comandi di base della shell linux.

# CODICI DI USCITA
USER_ABORT=101
UNKNOWN_INPUT=102

# COLORI DI OUTPUT
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BOLD_RED='\033[1;31m'
BOLD_GREEN='\033[1;32m'
BOLD_YELLOW='\033[1;33m'
BOLD='\033[1m'
BRIGHT='\033[1;99m'
RESET='\033[0m'
CLEAR='\033[2J\033[H'


# LE VARIABILI
# Definiamo la nostra directory di lavoro.
WORKDIR="${HOME}/W5D1_bash-demo"
ECHO="echo -e"
LS="ls -l --color=auto"
LSA="ls -al --color=auto"



# mostriamo un titolo, ma prima puliamo lo schermo :)
$ECHO "${CLEAR}"
$ECHO " \ \        / ___|   __ \ _ |                   |                   |           |                  _)             "
$ECHO "  \ \  \   /  __ \   |   |  |                   __ \    _\` |   __|  __ \        __ \    _\` |   __|  |   __|   __| "
$ECHO "   \ \  \ /     ) |  |   |  |      _____|       |   |  (   | \__ \  | | |       |   |  (   | \__ \  |  (    \__ \ "
$ECHO "    \_/\_/   ____/  ____/  _|                  _.__/  \__._| ____/ _| |_|      _.__/  \__._| ____/ _| \___| ____/ "

# abbiamo tree installato?
TREE=$(which tree 2>/dev/null)

if [ "$TREE" ]; then
	$ECHO "${GREEN}utilizzeremo il comando tree${RESET}"
else
	$ECHO "${RED}tree non è installato nel sistema.${RESET}"
fi

# Verifichiamo che la nostra workdir non esista e la creiamo da zero,
# oppure se esiste la svuotiamo e andiamo a lavorarci all'interno.
$ECHO "Opereremo nella directory di lavoro: ${BOLD}\"${WORKDIR}\"${RESET}."
$ECHO "Verifichiamo se esiste oppure la creiamo da zero."
$ECHO "${BOLD_RED}ATTENZIONE: ${RED}se la directory esiste già andremo ad eliminarne il contenuto.${RESET}"

if [[ -d "$WORKDIR" && "$(ls -A ${WORKDIR})" ]]; then
	$ECHO "La directory ${BOLD}\"${WORKDIR}\" ${RED}esiste già e non è vuota.${RESET}"
	read -p "Vuoi svuotarla? [s/N]: " RISP
	case "$RISP" in
	    [sS]) 
	    	$ECHO "${BOLD_GREEN}svuoto la directory \"${WORKDIR}\".${RESET}"
			rm -rf ${WORKDIR}/*
	        ;;
	    [nN]|"") 
	        $ECHO "${YELLOW}Operazione annullata.${RESET}"
	        exit $USER_ABORT
	        ;;
	    *) 
	        $ECHO "${BOLD_RED}Non ho capito. Per  sicurezza annullo l'operazione.${RESET}"
	        exit $UNKNOWN_INPUT
	        ;;
	esac
elif [ -d "$WORKDIR" ]; then
		$ECHO "${GREEN}La directory ${WORKDIR} esiste già ma è vuota."
		$ECHO "possiamo procedere.${RESET}"
else
	$ECHO "${GREEN}Creiamo la directory ${WORKDIR}.${RESET}"
	mkdir -p ${WORKDIR}
fi

# se siamo arrivati a questo punto vuol dire che abbiamo una workdir vuota.
# ci spostiamo al suo interno e procediamo.
cd ${WORKDIR}

# Per creare le directory richieste, ho deciso di iniziare creando il primo livello 
# e poi di procedere per sottolivelli in modo da inglobare in un unico comando
# la creazione di più directory.
echo
$ECHO "${BRIGHT}\t # creiamo le directories di primo livello${RESET}"
$ECHO "${GREEN}mkdir -p dos studenti tmp windows${RESET}"
mkdir -p dos studenti tmp windows
$ECHO "${BRIGHT}\t # Procediamo con i livelli successivi${RESET}"
$ECHO "${GREEN}mkdir -p studenti/{anna,matteo,nicola}${RESET}"
mkdir -p studenti/{anna,matteo,nicola}
$ECHO "${GREEN}mkdir -p studenti/anna/casa${RESET}"
mkdir -p studenti/anna/casa
$ECHO "${GREEN}mkdir -p studenti/matteo/amici${RESET}"
mkdir -p studenti/matteo/amici
$ECHO "${GREEN}mkdir -p studenti/nicola/{lavoro,scuola}${RESET}"
mkdir -p studenti/nicola/{lavoro,scuola}
# separiamo l'output
echo
# andiamo a creare i files
$ECHO "${BRIGHT}\t # Creiamo i files richiesti${RESET}"
$ECHO "${GREEN}touch studenti/nicola/scuola/{compito,relazione}.doc${RESET}"
touch studenti/nicola/scuola/{compito,relazione}.doc
$ECHO "${GREEN}touch tmp/risultati.doc${RESET}"
touch tmp/risultati.doc
# separiamo l'output
echo
# mostriamo il risultato delle operazioni
$ECHO "${BOLD_GREEN}\t\t~~~ QUESTO E' LO STATO ATTUALE. ~~~${RESET}"
$ECHO "${BOLD}${WORKDIR}${RESET}"
$TREE -a

# separiamo l'output
echo
# interrompiamo per un breve break :)
# se l'utente decide di procedere, puliamo lo schermo e andiamo avanti.
read -p "Continuiamo? [S/n]: " ANDIAMO
case "$ANDIAMO" in
	[sS]|"" ) 
		$ECHO "${CLEAR}"
		;;
	[nN]) 
		$ECHO "${YELLOW}Operazione annullata.${RESET}"
		exit $USER_ABORT
		;;
	*) 
		$ECHO "${BOLD_RED}Non ho capito. Per sicurezza annullo l'operazione.${RESET}"
		exit $UNKNOWN_INPUT
		;;
esac

# Adesso andiamo ad operare sui files e directories creati.
$ECHO "${BRIGHT}\tL'esercizio richiede che partiamo all'interno della directory lavoro sotto nicola.${RESET}"
$ECHO "${GREEN}cd studenti/nicola/lavoro${RESET}"
cd studenti/nicola/lavoro
# separiamo l'output
echo
$ECHO "${BRIGHT}\tda quì ci spostiamo nella directory casa, sotto anna.${RESET}"
$ECHO "${BRIGHT}\tpossiamo farlo specificando un path relativo o assoluto.${RESET}"
$ECHO "${BRIGHT}\tcd \"../../anna/casa\" oppure cd \"${WORKDIR}/studenti/anna/casa\"${RESET}"
$ECHO "${GREEN}cd ../../anna/casa${RESET}"
cd "../../anna/casa"
$ECHO "${BRIGHT}\tora siamo nella directory casa sotto anna.${RESET}"
# separiamo l'output
echo
$ECHO "${BRIGHT}\tA) dobbiamo copiare il file compito.doc dalla directory scuola sotto nicola${RESET}"
$ECHO "${BRIGHT}\talla posizione attuale.${RESET}"
$ECHO "${GREEN}cp ${WORKDIR}/studenti/nicola/scuola/compito.doc .${RESET}"
cp "${WORKDIR}/studenti/nicola/scuola/compito.doc" .
$ECHO "${BRIGHT}\til punto alla fine del comando precedente indica che la destinazione${RESET}"
$ECHO "${BRIGHT}\tdel comando cp è la directory corrente.${RESET}"
# separiamo l'output
echo
$ECHO "${BRIGHT}\tB) Procediamo adesso spostando il file relazione.doc nella cartella corrente.${RESET}"
$ECHO "${GREEN}mv ${WORKDIR}/studenti/nicola/scuola/relazione.doc .${RESET}"
mv "${WORKDIR}/studenti/nicola/scuola/relazione.doc" .
# separiamo l'output
echo
# mostriamo il risultato delle operazioni
$ECHO "${BOLD_GREEN}\t\t~~~ QUESTO E' LO STATO ATTUALE. ~~~${RESET}"
$ECHO "${BOLD}${WORKDIR}${RESET}"
$TREE -a $WORKDIR

# separiamo l'output
echo
# interrompiamo per un breve break :)
# se l'utente decide di procedere, puliamo lo schermo e andiamo avanti.
read -p "Continuiamo? [S/n]: " ANDIAMO
case "$ANDIAMO" in
	[sS]|"" ) 
		$ECHO "${CLEAR}"
		;;
	[nN]) 
		$ECHO "${YELLOW}Operazione annullata.${RESET}"
		exit $USER_ABORT
		;;
	*) 
		$ECHO "${BOLD_RED}Non ho capito. Per sicurezza annullo l'operazione.${RESET}"
		exit $UNKNOWN_INPUT
		;;
esac

# separiamo l'output
echo
$ECHO "${BRIGHT}\tC) Adesso dobbiamo rimuovere la cartella tmp.${RESET}"
$ECHO "${GREEN}rm -rf ${WORKDIR}/tmp${RESET}"
rm -rf ${WORKDIR}/tmp

# separiamo l'output
echo
$ECHO "${BRIGHT}\tD) Ora dobbiamo creare il file pippo.txt nella cartella Lavoro sotto Nicola.${RESET}"
$ECHO "${GREEN}touch ${WORKDIR}/studenti/nicola/lavoro/pippo.txt${RESET}"
# up piccolo easter egg :)
echo "Il corso \"Cybersecurity PT\" è molto interessante." > ${WORKDIR}/studenti/nicola/lavoro/pippo.txt

# separiamo l'output
echo
$ECHO "${BRIGHT}\tE) Dovremmo adesso modificare gli attributi del file pippo.txt${RESET}"
$ECHO "${BRIGHT}\te renderlo leggibile e scrivibile solo dal proprietario, mentre rimane solo${RESET}"
$ECHO "${BRIGHT}\tleggibile per tutti gli altri.${RESET}"
$ECHO "${BRIGHT}\tQuesto si può fare con il comando chmod, che permette di specificare${RESET}"
$ECHO "${BRIGHT}\ti permessi, sia in notazione ottale che in maniera più descrittiva:${RESET}"
$ECHO "${GREEN}chmod 644 ${WORKDIR}/studenti/nicola/lavoro/pippo.txt${RESET}"
$ECHO "${BRIGHT}\tse vogliamo utilizzare la notazione ottale, altrimenti:${RESET}"
$ECHO "${GREEN}chmod u=rw,g=r,o=r ${WORKDIR}/studenti/nicola/lavoro/pippo.txt${RESET}"
$ECHO "${BRIGHT}\tper specificare i permessi in maniera più \"umana\".${RESET}"
chmod 644 ${WORKDIR}/studenti/nicola/lavoro/pippo.txt
$ECHO "${BRIGHT}\tda notare che 644 è la maschera di default per i files creati, quindi${RESET}"
$ECHO "${BRIGHT}\til nostro file avrà già i permessi corretti.${RESET}"
# separiamo l'output
echo
$LS ${WORKDIR}/studenti/nicola/lavoro/pippo.txt

# separiamo l'output
echo
# mostriamo il risultato delle operazioni
$ECHO "${BOLD_GREEN}\t\t~~~ QUESTO E' LO STATO ATTUALE. ~~~${RESET}"
$ECHO "${BOLD}${WORKDIR}${RESET}"
$TREE -a $WORKDIR

# separiamo l'output
echo
# interrompiamo per un breve break :)
# se l'utente decide di procedere, puliamo lo schermo e andiamo avanti.
read -p "Continuiamo? [S/n]: " ANDIAMO
case "$ANDIAMO" in
	[sS]|"" ) 
		$ECHO "${CLEAR}"
		;;
	[nN]) 
		$ECHO "${YELLOW}Operazione annullata.${RESET}"
		exit $USER_ABORT
		;;
	*) 
		$ECHO "${BOLD_RED}Non ho capito. Per sicurezza annullo l'operazione.${RESET}"
		exit $UNKNOWN_INPUT
		;;
esac

# separiamo l'output
echo
$ECHO "${BRIGHT}\tF) Il prossimo task è quello di nascondere il contenuto${RESET}"
$ECHO "${BRIGHT}\tdella cartella anna.${RESET}"
$ECHO "${BRIGHT}\tQuesto si può fare anteponendo un punto \".\" al nome del file${RESET}"
$ECHO "${BRIGHT}\to directory che vogliamo nascondere.${RESET}"
$ECHO "${BRIGHT}\tPer modificare il nome di un file utilizzeremo mv.${RESET}"
$ECHO "${GREEN}mv ${WORKDIR}/studenti/anna/casa ${WORKDIR}/studenti/anna/.casa${RESET}"
mv ${WORKDIR}/studenti/anna/casa ${WORKDIR}/studenti/anna/.casa
# separiamo l'output
echo
$ECHO "${BRIGHT}\tUn semplice \"ls -l\" non visualizzerà nulla.${RESET}"
$LS ${WORKDIR}/studenti/anna
# separiamo l'output
echo
$ECHO "${BRIGHT}\tMentre \"ls -al\" visualizzerà il contenuto nascosto.${RESET}"
$LSA ${WORKDIR}/studenti/anna

# separiamo l'output
echo
$ECHO "${BRIGHT}\tG) Ora dobbiamo spostarci nella cartella lavoro sotto nicola${RESET}"
$ECHO "${BRIGHT}\te visualizzare il contenuto del file pippo.txt.${RESET}"
$ECHO "${BRIGHT}\tRicordando che siamo ancora nella cartella casa sotto anna,${RESET}"
$ECHO "${BRIGHT}\tpossiamo nuovamente passare all'altra cartella con un percorso.${RESET}"
$ECHO "${BRIGHT}\trelativo o assoluto.${RESET}"
$ECHO "${BRIGHT}\t\"cd ../../nicola/lavoro\" oppure \"cd ${WORKDIR}/studenti/nicola/lavoro\"${RESET}"
$ECHO "${GREEN}cd ../../nicola/lavoro${RESET}"
cd ../../nicola/lavoro
$ECHO "${BRIGHT}\tora siamo nella directory lavoro sotto nicola.${RESET}"
$ECHO "${BRIGHT}\tPer visualizzare il contenuto di un file, possiamo usare \"cat\".${RESET}"
$ECHO "${GREEN}cat pippo.txt${RESET}"
cat pippo.txt

# separiamo l'output
echo
# mostriamo il risultato delle operazioni
$ECHO "${BOLD_GREEN}\t\t~~~ QUESTO E' LO STATO ATTUALE. ~~~${RESET}"
$ECHO "${BOLD}${WORKDIR}${RESET}"
$TREE -a $WORKDIR

# separiamo l'output
echo
# interrompiamo per un breve break :)
# se l'utente decide di procedere, puliamo lo schermo e andiamo avanti.
read -p "Continuiamo? [S/n]: " ANDIAMO
case "$ANDIAMO" in
	[sS]|"" ) 
		$ECHO "${CLEAR}"
		;;
	[nN]) 
		$ECHO "${YELLOW}Operazione annullata.${RESET}"
		exit $USER_ABORT
		;;
	*) 
		$ECHO "${BOLD_RED}Non ho capito. Per sicurezza annullo l'operazione.${RESET}"
		exit $UNKNOWN_INPUT
		;;
esac

# separiamo l'output
echo
$ECHO "${BRIGHT}\tH) La prossima operazione ci chiede di rimuovere${RESET}"
$ECHO "${BRIGHT}\tla directory amici sotto matteo.${RESET}"
$ECHO "${BRIGHT}\tSiccome si tratta di una directory vuota potremo usare${RESET}"
$ECHO "${BRIGHT}\til comando \"rmdir\" che è molto più sicuro da usare in quanto${RESET}"
$ECHO "${BRIGHT}\tquesto comando si rifiuta di procedere se sono presenti dei files.${RESET}"
$ECHO "${GREEN}rmdir ${WORKDIR}/studenti/matteo/amici${RESET}"
rmdir ${WORKDIR}/studenti/matteo/amici

# separiamo l'output
echo
$ECHO "${BRIGHT}\tI) L'ultimo task ci chiede di rimuovere tutte le directory${RESET}"
$ECHO "${BRIGHT}\tcreate fin ora nell'esercizio.${RESET}"
$ECHO "${BRIGHT}\tQuindi per procedere ci sposteremo nella nostra home${RESET}"
$ECHO "${BRIGHT}\tprima di cancellare tutto.${RESET}"
$ECHO "${GREEN}cd ${HOME}${RESET}"
cd ${HOME}
$ECHO "${GREEN}rm -rf ${WORKDIR}${RESET}"
rm -rf ${WORKDIR}

# separiamo l'output
echo
# mostriamo il risultato delle operazioni
$ECHO "${BOLD_GREEN}\t\t~~~ QUESTO E' LO STATO ATTUALE. ~~~${RESET}"
$ECHO "${BOLD}${PWD}${RESET}"
$LS .

$ECHO "${BOLD_GREEN}\t\t~~~ ALLA PROSSIMA. ~~~${RESET}"
$ECHO "${BOLD_GREEN}DM${RESET}"

# the end
