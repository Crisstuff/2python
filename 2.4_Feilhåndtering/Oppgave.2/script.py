#!/bin/python

try:  
    tall = int(input("Skriv inn et tall: "))  
    input = 10 / tall  
    print(f"Resultatet er {input}")  

except ZeroDivisionError:  
    print("Du kan ikke dele på null!")  

except ValueError:  
    print("Dette er ikke et gyldig tall!")