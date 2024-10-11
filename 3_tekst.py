import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Min notepad")

tekst_felt = tk.Text(root, height=10, width=50)
tekst_felt.pack()

def lagre_tekst():
    tekst_innhold = tekst_felt.get("1.0", tk.END) #1.0 = linje 1, posisjon 0 - tk.END = slutten av filen
    file = filedialog.asksaveasfile(mode="w", defaultextension=".txt") 
    file.write(tekst_innhold)
    file.close() #dette er viktig ettersom vi åpnet med filedialig og ikke brukte "with open"

def hente_tekst():
    filsti = filedialog.askopenfilename(filetypes=[("Tekst-filer", "*.txt")])
    with open(filsti,"r") as file:
        tekst_felt.delete("1.0",tk.END)         #vi tømmer først tekstfeltet
        tekst_felt.insert("1.0",file.read())    #så fyller vi det med innholdet fra filen

ramme_knapper = tk.Frame(root)

knapp_lagre = tk.Button(ramme_knapper, text="Lagre", command=lagre_tekst)
knapp_lagre.pack(side=tk.LEFT)

knapp_hente = tk.Button(ramme_knapper, text="Åpne", command=hente_tekst)
knapp_hente.pack()

ramme_knapper.pack()

root.mainloop()