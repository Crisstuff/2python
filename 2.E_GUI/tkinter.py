label = tk.Label(root, text="Hei, Tkinter!")
label.pack()
button = tk.Button(root, text="Klikk meg", command=lambda:
label.config(text="Knappen ble trykket!"))
button.pack()