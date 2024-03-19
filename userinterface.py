from tkinter import *

Frame = Tk()

Frame.title("hello World")
Frame.geometry("420x420")

searchRecipeButton = Button(Frame,text = "Search Recipe")

searchRecipeButton.pack()

addRecipeButton = Button(Frame, text="Add recipe")
Frame.mainloop()