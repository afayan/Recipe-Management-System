#name #ingredients #process

from database import *

from tkinter import messagebox


def getInfo():

    try:
        name = nameInput.get('1.0', 'end-1c')
        print(name)
        dummyList = []

        for index in listOfIngredients.curselection():
            dummyList.insert(index,listOfIngredients.get(index)) 

        print(dummyList)

        cooktime = int(cooktimeinput.get()) 
        print(cooktime)

        dietSelected = diet_var.get()

        print(dietSelected)

        insertValue(name,*dummyList,time=cooktime,diet=dietSelected)
    
    except Exception as e:
         messagebox.showerror("Error", "You have entered some invalid info. Please check and try again")




import tkinter as tk

adminpage = tk.Tk()
adminpage.geometry("430x430")

nameText = tk.Label(adminpage, text="Enter name")
nameText.pack()

nameInput = tk.Text(adminpage,width="30",height="2")
nameInput.pack()





listOfIngredients = tk.Listbox(adminpage,selectmode="multiple")
pseudoIngredients = ['bread', 'rice', 'chicken','eggs', 'garlic','turmeric','coriander']

selectIngred = tk.Label(adminpage, text="Choose ingredients")
selectIngred.pack()

for i in range(0,len(pseudoIngredients)):
    listOfIngredients.insert(i,pseudoIngredients[i])
    
listOfIngredients.pack()

timeText = tk.Label(adminpage, text="Enter cooktime")
timeText.pack()
cooktimeinput = tk.Entry(adminpage)
cooktimeinput.pack()


diet_var = tk.StringVar()
diet_var.set(None) 

diet1 = tk.Radiobutton(adminpage, text="Veg", variable=diet_var, value="Veg")
diet2 = tk.Radiobutton(adminpage, text="Non-Veg", variable=diet_var, value="Non-Veg")

diet1.pack()
diet2.pack()

submitButton = tk.Button(adminpage,text="submit", command=getInfo)
submitButton.pack()
adminpage.mainloop()

