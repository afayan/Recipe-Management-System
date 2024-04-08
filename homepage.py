from database import *
import tkinter as tk
from tkinter import messagebox
from admin import *
from searchpage import *
from tkinter import PhotoImage
#from PIL import Image, ImageTk


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
frame.title("Recipe Management system")
frame.geometry("626x417")

backg = PhotoImage(file="images/backg2.png")
image = tk.Label(frame, image=backg)
image.place(relheight=1, relwidth=1)


title = tk.Label(frame, text="Welcome to RMS" ,font=("Trajan Pro", 24), fg="#ffd700", bg="#000000")
title.place(x=168, y=150)
searchRecipe = tk.Button(frame, text="Search recipe", command=openSearch, height=buttonHeight, width=buttonWidth, bg="#ffd700")
searchRecipe.place(x=100,y=300)

#image = tk.Image.open("images/360_F_292203735_CSsyqyS6A4Z9Czd4Msf7qZEhoxjpzZl1.jpg")
#photo = tk.ImageTk.PhotImage(image)

#canvas = tk.Canvas(frame,width=image.width(), height=image.height())
#canvas.pack(fill="both", expand=True)
#canvas.create_image(0, 0, image=photo, anchor="nw")



adminButton = tk.Button(frame, text="Admin Settings",command=openadmin,  height=buttonHeight, width=buttonWidth, bg="#ffd700")
adminButton.place(x=400, y=300)

frame.mainloop()