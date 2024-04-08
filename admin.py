import tkinter as tk
from tkinter import ttk
from database import *
from tkinter import messagebox

class Admin:
    def __init__(self):
        self.adminpage = tk.Tk()
        self.adminpage.geometry("1320x500")

        self.notebookAdmin = ttk.Notebook(self.adminpage)

        self.insertDish = tk.Frame(self.adminpage)
        self.insertIngreds = tk.Frame(self.adminpage)
        
        self.nameText = tk.Label(self.insertDish, text="Enter name")
        self.nameText.pack()

        self.nameInput = tk.Text(self.insertDish,width="30",height="2")
        self.nameInput.pack()

        self.listOfIngredients = tk.Listbox(self.insertDish,selectmode="multiple")
        self.pseudoIngredients = giveIngredients()
        #self.pseudoIngredients = ['eggs', 'butter','corn','ketchup']
        self.selectIngred = tk.Label(self.insertDish, text="Choose ingredients")
        self.selectIngred.pack()


        for i in range(0,len(self.pseudoIngredients)):

        
            self.listOfIngredients.insert(i,self.pseudoIngredients[i])

  


        self.listOfIngredients.pack()

        self.timeText = tk.Label(self.insertDish, text="Enter cooktime")
        self.timeText.pack()
        self.cooktimeinput = tk.Entry(self.insertDish)
        self.cooktimeinput.pack()


        self.diet_var = tk.StringVar()
        self.diet_var.set(None) 

        self.diet1 = tk.Radiobutton(self.insertDish, text="Veg", variable=self.diet_var, value="Veg")
        self.diet2 = tk.Radiobutton(self.insertDish, text="Non-Veg", variable=self.diet_var, value="Non-Veg")

        self.diet1.pack()
        self.diet2.pack()

        self.submitButton = tk.Button(self.insertDish,text="submit", command=self.getInfo)
        self.submitButton.pack()

        #insert ingredients code starts here....
        self.enterIngredNameLabel = tk.Label(self.insertIngreds, text="Enter ingredient name")
        self.enterIngredNameLabel.pack()

        self.ingredEntry = tk.Entry(self.insertIngreds)
        self.ingredEntry.pack()

        self.submitIngreds = tk.Button(self.insertIngreds,text="submit", command=self.addIngreds)
        self.submitIngreds.pack()


        

        self.notebookAdmin.add(self.insertDish, text="insert Dish")
        self.notebookAdmin.add(self.insertIngreds, text="insert Ingredients")
        self.notebookAdmin.pack(fill="both", expand=True)

        self.adminpage.mainloop()

    def getInfo(self):
        #try:
            name = self.nameInput.get('1.0', 'end-1c')
            print(name)
            dummyList = []

            for index in self.listOfIngredients.curselection():
                dummyList.insert(index, self.listOfIngredients.get(index)) 

            print(dummyList)


            cooktime = int(self.cooktimeinput.get()) 
            print(cooktime)

            dietSelected = self.diet_var.get()

            print(dietSelected)

            for item in dummyList:
                insertValue(name, item, time=cooktime, diet=dietSelected)
        
        #except Exception as e:
            #messagebox.showerror("Error", "You have entered some invalid info. Please check and try again")
            #print(e)
                
    def addIngreds(self):
        ingredient = self.ingredEntry.get()
        print(ingredient)
        addIngredsToDatabase(ingredient)
         
         

def launch_admin_page():
    adminInstance = Admin()

if __name__ == "__main__":
    launch_admin_page()
        