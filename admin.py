import tkinter as tk
from database import *
from tkinter import messagebox

class Admin:
    def __init__(self):
        self.adminpage = tk.Tk()
        self.adminpage.geometry("430x430")
        
        self.nameText = tk.Label(self.adminpage, text="Enter name")
        self.nameText.pack()

        self.nameInput = tk.Text(self.adminpage,width="30",height="2")
        self.nameInput.pack()

        self.listOfIngredients = tk.Listbox(self.adminpage,selectmode="multiple")
        self.pseudoIngredients = ['bread', 'rice', 'chicken','eggs', 'garlic','turmeric','coriander']
        self.selectIngred = tk.Label(self.adminpage, text="Choose ingredients")
        self.selectIngred.pack()


        for i in range(0,len(self.pseudoIngredients)):
            self.listOfIngredients.insert(i,self.pseudoIngredients[i])


        self.listOfIngredients.pack()

        self.timeText = tk.Label(self.adminpage, text="Enter cooktime")
        self.timeText.pack()
        self.cooktimeinput = tk.Entry(self.adminpage)
        self.cooktimeinput.pack()


        self.diet_var = tk.StringVar()
        self.diet_var.set(None) 

        self.diet1 = tk.Radiobutton(self.adminpage, text="Veg", variable=self.diet_var, value="Veg")
        self.diet2 = tk.Radiobutton(self.adminpage, text="Non-Veg", variable=self.diet_var, value="Non-Veg")

        self.diet1.pack()
        self.diet2.pack()

        self.submitButton = tk.Button(self.adminpage,text="submit", command=self.getInfo)
        self.submitButton.pack()
        self.adminpage.mainloop()

    def getInfo(self):
        try:
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

            insertValue(name, *dummyList, time=cooktime, diet=dietSelected)
        
        except Exception as e:
            messagebox.showerror("Error", "You have entered some invalid info. Please check and try again")

def launch_admin_page():
    adminInstance = Admin()

if __name__ == "__main__":
    launch_admin_page()
        