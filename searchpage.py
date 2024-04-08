from database import *
import tkinter as tk
from tkinter import ttk


class searchPage:
    def launchSearch():
        searchPage()

    def __init__(self):

        self.searchframe = tk.Tk()
        #self.searchByIngredients = tk.Tk()
        self.searchframe.geometry("1320x500")
        #self.searchframe.configure(bg="#ffd700")


        self.myNotebook = ttk.Notebook(self.searchframe)

        self.searchByNameTab = tk.Frame(self.myNotebook,bg="#ffd700")
        self.searchByIngredientTab = tk.Frame(self.myNotebook,bg="#ffd700")

        #code to be repeated in other tab
        self.listOfFoodNames = tk.Listbox(self.searchByNameTab)
        self.nameList = givenames()

        for i in self.nameList:
            j = 1
            self.listOfFoodNames.insert(j,i)
            j+=1


        self.listOfFoodNames.pack()

        self.submitButton = tk.Button(self.searchByNameTab,text="search recipe",command=self.submit_items)
        self.submitButton.pack()


        self.infoLabel = tk.Label(self.searchByNameTab, text="select items")
        self.infoLabel.pack()

        #repeated code ends here
        self.listOfIngredients = tk.Listbox(self.searchByIngredientTab,selectmode="multiple")
        self.pseudoIngredients = giveIngredients()
        #self.pseudoIngredients = ['eggs', 'butter','corn','ketchup']
        self.selectIngred = tk.Label(self.searchByIngredientTab, text="Choose ingredients")
        self.selectIngred.pack()




        for i in range(0,len(self.pseudoIngredients)):

        
            self.listOfIngredients.insert(i,self.pseudoIngredients[i])

  


        self.listOfIngredients.pack()

        self.submitButton2 = tk.Button(self.searchByIngredientTab,text="search by ingredients",command=self.searchByIngreds)
        self.submitButton2.pack()


        self.infoLabel2 = tk.Label(self.searchByIngredientTab, text="search items")
        self.infoLabel2.pack()

        #repeated code ends here
        


        self.myNotebook.add(self.searchByNameTab, text="search by name")
        self.myNotebook.add(self.searchByIngredientTab, text="search by ingredient")
        self.myNotebook.pack(fill="both", expand=True)

        self.searchframe.mainloop()



    def submit_items(self):
        selectedname = self.listOfFoodNames.get(self.listOfFoodNames.curselection())
        #checking all the selected names
        print(type(selectedname))

        infoList = giveInfo(selectedname)

        #for item in infoList:
        #    for element in item:
         #       print(element)
        print(infoList)

        self.displayItems(infoList)

    def displayItems(self, infoList): #function to display given list in gui

        self.infoLabel.config(text=infoList)

    def searchByIngreds(self):

        dummyList = []

        for index in self.listOfIngredients.curselection():
            dummyList.insert(index, self.listOfIngredients.get(index)) 

        print(dummyList)
        #dummylist is a list of tuples

        info = searchByIngredient(dummyList)
        self.infoLabel2.config(text=info)

                


if __name__ == "__main__":
    searchPage.launchSearch()



    