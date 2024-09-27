#!/bin/bash
class Dyr: 
    def __init__(self, navn):
        self.navn = navn

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
        

hund1 = Hund("Fido")
hund1.lag_lyd()
hund1.logre()
hund1.lag_lyd()

katt1 = Katt("pus")
katt1.lag_lyd()
