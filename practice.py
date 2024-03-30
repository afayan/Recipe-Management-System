import tkinter as tk
from tkinter import ttk

frame = tk.Tk()

myNotebook = ttk.Notebook(frame)

tab1 = tk.Frame(myNotebook)
tab2 = tk.Frame(myNotebook)

myNotebook.add(tab1, text="first")
myNotebook.add(tab2, text="second")

myNotebook.pack(fill="both", expand=True)  # Corrected line

frame.mainloop()
