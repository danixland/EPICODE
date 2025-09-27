#! /usr/bin/env python

my_words = ["epicode", "is", "the", "best", "Danilo", "very", "smart", "CyberSecurity", "hacker", "ethical"]

def conta_caratteri(lista_char):
	output = []
	for i in lista_char:
		output.append(len(i))

	return output

print(f"La lista di parole è:\n{my_words}")
print(f"La lunghezza di ogni parola è:\n{conta_caratteri(my_words)}")

print("\t### Visualizzazione Alternativa ###")
for w in my_words:
	print(f"{w} -->\t {len(w)} caratteri")
