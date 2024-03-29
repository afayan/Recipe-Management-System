from database import *
import tkinter as tk


class searchPage:
    def launchSearch():
        searchPage()

    def __init__(self):

        self.searchframe = tk.Tk()
        self.searchframe.geometry("420x420")

        self.listOfFoodNames = tk.Listbox(self.searchframe)

        self.nameList = givenames()

        for i in self.nameList:
            j = 1
            self.listOfFoodNames.insert(j,i)
            j+=1


        self.listOfFoodNames.pack()

        self.submitButton = tk.Button(self.searchframe,text="search recipe",command=self.submit_items)
        self.submitButton.pack()

        self.searchframe.mainloop()



    def submit_items(self):
        selectedname = self.listOfFoodNames.get(self.listOfFoodNames.curselection())
        infoList = giveInfo(selectedname)

        for item in infoList:
            for element in item:
                print(element)
        #print(infoList)
                


if __name__ == "__main__":
    searchPage.launchSearch()



    