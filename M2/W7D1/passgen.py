#! /usr/bin/env python

"""
passgen.py -	Semplice script che riceve un argomento sulla riga di comando e restituisce una password semplice o complessa.
"""

import argparse
import random
import string

def generate_password(length):
    # Genera una password random della lunghezza specificata.
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description="Genera una password casuale.")
    parser.add_argument('-c', action='store_true', help='Genera una password complessa con 20 caratteri')
    parser.add_argument('-s', action='store_true', help='Genera una password semplice con 8 caratteri')

    args = parser.parse_args()

    if args.c:
        password_length = 20
    elif args.s:
        password_length = 8
    else:
        print("Si deve specificare -c per la password complessa o -s per quella semplice.")
        return

    password = generate_password(password_length)
    print(f"La tua Password è: {password}")

if __name__ == "__main__":
    main()