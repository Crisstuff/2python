#!/bin/python
#listerligger under her
tekst = "Hello World!"
vokal_liste = "aeiouyæøåAEIOUYÆØÅ"  # Små og store vokaler

#functioner ligger under her
def tell_vokaler(tekst):
    vokaler = tekst - vokal_liste
    char_count = len(vokaler) #Teller antall caracters som blir igjen i vokaler
    return char_count

def speilvend(tekst):
    speilvendt_tekst = tekst[::-1]
    return speilvendt_tekst

def erstatt_vokal():
    erstatt = tekst - vokal_liste
    return erstatt
