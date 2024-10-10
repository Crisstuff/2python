#!/bin/python
import os

# Åpen en løkke slik at brukeren kan skrive flere linjer
while True:
    bruker_input = input("Skriv inn noe tekst (eller skriv 'STOPP' for å avslutte): ")
    
    if bruker_input.lower() == 'stopp':
        break
    
    elif bruker_input.lower() == 'delete':
        os.remove("bruker_tekst_op3.txt") 
        

    # Åpne filen i "append"-modus ('a') for å legge til tekst i stedet for å overskrive
    with open("bruker_tekst_op3.txt", "a") as fil:
        fil.write(bruker_input + "\n")

print("Teksten er lagret i 'bruker_tekst_op3.txt'.")

