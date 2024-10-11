#!/bin/python

import tkinter as tk

class Innhold_boks:
    def __init__(self, master, id):
        self.master = master
        self.ramme = tk.Frame(self.master, borderwidth=2, relief="sunken")
        self.ramme.pack(padx=10, pady=5, fill="x")

        self.etikett = tk.Label(master=self.ramme, text=f"Element nr. {id}")
        self.etikett.pack(side="left", padx=10)

        self.knapp_slett = tk.Button(
            self.ramme, 
            text="Slett",
            command=self.remove
        )
        self.knapp_slett.pack(side="right")

    def remove(self):
        self.ramme.destroy()


class Applikasjon:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamisk app")

        self.hoved_ramme = tk.Frame(root)
        self.hoved_ramme.pack(fill="both", expand=True)

        self.knapp_opprett = tk.Button(
            self.root,
            text="Legg til ny widget",
            command=self.opprett    
        )
        self.knapp_opprett.pack(pady=20)
        self.widget_teller = 0
        self.widgets = []

    def opprett(self):
        self.widget_teller += 1
        ny_widget = Innhold_boks(self.hoved_ramme, self.widget_teller)
        self.widgets.append(ny_widget)




root = tk.Tk()
app = Applikasjon(root)
root.mainloop()