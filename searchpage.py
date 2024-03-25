from database import *

def submit_items():
    selectedname = listOfFoodNames.get(listOfFoodNames.curselection())
    infoList = giveInfo(selectedname)

    for item in infoList:
        for element in item:
            print(element)
    #print(infoList)



import tkinter as tk

searchframe = tk.Tk()
searchframe.geometry("420x420")

listOfFoodNames = tk.Listbox(searchframe)

nameList = givenames()

for i in nameList:
    j = 1
    listOfFoodNames.insert(j,i)
    j+=1


listOfFoodNames.pack()

submitButton = tk.Button(searchframe,text="search recipe",command=submit_items)
submitButton.pack()

searchframe.mainloop()