#!/bin/python
class konto:
    def __init__(self, saldo, navn):
        self.__saldo = saldo
        self.__navn = navn

    def innskudd(self, inn):
        self.__saldo += inn
    
    def uttak(self, ut):
        if ut <=self.__saldo:
            self.__saldo -= ut
        else:
            print("ikke nok penger")
        
    def get_saldo(self):
        return self.__saldo
    def get_navn(self):
        return self. __navn
    def set_navn(self, nytt):
        self.__navn = str(nytt)

min_konto = konto(150,"bruks")
print(min_konto.get_saldo())
min_konto.uttak(200)
min_konto.innskudd(50)
print(min_konto.get_saldo())
min_konto.set_navn("Spare")
print(min_konto.get_navn())
  