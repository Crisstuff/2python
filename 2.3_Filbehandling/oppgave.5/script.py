#!/bin/python

# Eksempel på bruk
filnavn = 'bruker_tekst_op3.txt'
søkeord = 'potet'

def søk_etter_ord(filnavn, søkeord):
    try:
        with open(filnavn, 'r', encoding='utf-8') as fil:
            linjer = fil.readlines()
            
            print(f"Linjer som inneholder '{søkeord}':")
            for linje_nummer, linje in enumerate(linjer, 1):
                if søkeord in linje:
                    print(f"Linje {linje_nummer}: {linje.strip()}")
                    
    except FileNotFoundError:
        print(f"Filen '{filnavn}' ble ikke funnet.")

# Eksempel på bruk
søk_etter_ord(filnavn, søkeord)
