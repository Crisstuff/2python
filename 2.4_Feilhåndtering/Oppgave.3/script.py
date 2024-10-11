#!/bin/python
filnavn = input("Vennligst skriv inn navnet på filen du vil åpne: ")

# Funksjon for å lese innholdet av en tekstfil og skrive det ut
def les_fil(filnavn):

    try:
        # Åpner filen i lesemodus ('r')
        with open(filnavn, 'r') as fil:
            innhold = fil.read()
            print(innhold)
    except FileNotFoundError:
        print(f"Filen '{filnavn}' ble ikke funnet.")

# Eksempel på å bruke funksjonen
les_fil(filnavn)

