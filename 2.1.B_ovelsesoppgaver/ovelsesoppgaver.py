#!/bin/bash
class Dyr: 
    def __init__(self, navn):
        self.navn = navn
    
    def habitat(self, habitat):
        print(f"{self.navn} {habitat}")

    def lag_lyd(self, lyd):
        print(f"{self.navn} {lyd}")

class Hund(Dyr):
    def lag_lyd(self):
        super().lag_lyd("bjeffer")
    def logre(self):
        print(f"{self.navn} logrer")

class Katt(Dyr):
    def lag_lyd(self):
        super().lag_lyd("mjauer")

class Daniel(Dyr):
    def lag_lyd(self):
        super().lag_lyd("ikke rør PCen min")
    def habitat(self):
        super().habitat("bor hjemme")
    

hund1 = Hund("Fido")
hund1.lag_lyd()
hund1.logre()

katt1 = Katt("pus")
katt1.lag_lyd()

daniel = Daniel("Daniel")
daniel.lag_lyd()
daniel.habitat()