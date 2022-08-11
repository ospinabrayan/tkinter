from tkinter import *
master = Tk()
elemento = StringVar()
listbox = Listbox(master)
for item in ["pincel", "acuarela", "oleo", "lapices", "carboncillo"]:
 listbox.insert(END, item)
listbox.pack()
label = Label(text="Lista de instrumentos artisticos")
label.pack()
master.mainloop()
