from tkinter import *

from mainpage import Recipe


recipeObject = Recipe()
Frame = Tk()

Frame.title("hello World")
Frame.geometry("420x420")

searchRecipeButton = Button(Frame,text = "Search Recipe")

searchRecipeButton.pack()

addRecipeButton = Button(Frame,text="Add recipe")

addRecipeButton.pack()
Frame.mainloop()