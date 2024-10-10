#!/bin/python

# Filnavnet til tekstfilen
filnavn = "bruker_tekst_op3.txt"


# Funksjon for å telle linjer i en tekstfil
def tell_linjer(filnavn):
    linje_teller = 0
    try:
        with open(filnavn, 'r') as fil:
            for linje in fil:
                linje_teller += 1
        print(f"I filen '{filnavn}': er det {linje_teller} linjer med tekst")
    except FileNotFoundError:
        print(f"Filen '{filnavn}' ble ikke funnet.")

# Kall funksjonen for å telle linjene
tell_linjer(filnavn)
