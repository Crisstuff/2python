#!/bin/python
def sjekk_tall(tall):
    if tall % 2 == 0:
        return "Partall"
    else:
        return "Oddetall"

# Eksempel på bruk:

tall = int(input("Skriv inn et tall: "))
print(sjekk_tall(tall))