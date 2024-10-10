#!/bin/python

# Åpne filen i lese-modus ('r')
with open('fil.txt', 'r') as fil:
    # Les hele innholdet av filen
    innhold = fil.read()
    # Skriv ut innholdet til terminalen
    print(innhold)

# for å Run scriptet kan du skrive (python les_fil.py) i terminalen 
