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

buttonWidth = 15
buttonHeight = 2

frame = tk.Tk()
frame.title("RMS")
frame.geometry("1320x500")
title = tk.Label(frame, text="Welcome to RMS")
title.pack()
searchRecipe = tk.Button(frame, text="Search recipe", command=openSearch, height=buttonHeight, width=buttonWidth)
searchRecipe.place(x=400,y=300)

adminButton = tk.Button(frame, text="Admin Settings",command=openadmin,  height=buttonHeight, width=buttonWidth)
adminButton.place(x=600, y=300)

frame.mainloop()