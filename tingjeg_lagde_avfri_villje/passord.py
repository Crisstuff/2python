#!/bin/python
passord = ("teller32")

def sjekk_passord(test):
    if test == passord:
        return "riktig passord du er inne"
    else:
        return "feil passord"

# testing av passord
test = int(input("Skriv inn passordet:"))
print(sjekk_passord(test))
    
