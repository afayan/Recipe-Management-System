from database import *
import tkinter as tk
from tkinter import messagebox
from admin import *
from searchpage import *


def openadmin():
    messagebox.showwarning(title="Opening admin settings",message="You are opening the admin settings")
    launch_admin_page()

def openSearch():
    #from searchpage import Search
    searchPage.launchSearch()
    pass


frame = tk.Tk()
frame.title("RMS")
frame.geometry("420x420")
title = tk.Label(frame, text="Welcome to RMS")
title.pack()
searchRecipe = tk.Button(frame, text="Search recipe", command=openSearch)
searchRecipe.pack()

adminButton = tk.Button(frame, text="Admin Settings",command=openadmin)
adminButton.pack()

frame.mainloop()