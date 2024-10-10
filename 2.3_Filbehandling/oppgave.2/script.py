#!/bin/python

# Be om input fra brukeren
bruker_input = input("Skriv inn noe tekst du vil lagre i en fil: ")

# Åpne en ny fil i skrive-modus ('w') og skriv inputen til filen
with open("bruker_tekst_op2.txt", "w") as fil:
    fil.write(bruker_input)

print("Teksten er lagret i 'bruker_tekst_op2.txt'.")
