
filnavn = "eksempel.txt"

def read_file(filnavn):
    try:
        if open (filnavn, 'r') :
            innhold = fil.read(filnavn)
            print(innhold)
        with open(filnavn, 'r') as fil:
            innhold = fil.read()
            print(innhold)
        else; print("Filen ble lest uten problemer")
    finally:
        print("det oppstår en feil eller ikke.")




read_file(filnavn)