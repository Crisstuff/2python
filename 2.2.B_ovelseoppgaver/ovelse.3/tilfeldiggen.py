#!/bin/python
import random
import string

def tilfeldig_tall():
    return(random.randint(2,99))

def tilfeldig_karakter():
    string.ascii_letters('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    random.choice(string.ascii_letters)

