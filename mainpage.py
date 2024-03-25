class Recipe:
    recipeNo = 1
   

    def __init__(self, name):
        self.name = name
        self.ingredientList = {}
        Recipe.recipeNo+=1

    def changeRecipe(self, recipe):
        self.recipe = recipe 

    def assignIngredients(self, ingredient, amount):
        self.ingredientList[ingredient] = amount

    def __str__(self):
        return self.ingredientList
    
    def giveList(self):
        return self.ingredientList





        
#r1 = Recipe("Fried rice")
    
mainData = {}

while True:
    print("1.\tAdd dish\n2.\tCheck recipe\n3.\tExit")
    ch = int(input("Choice: "))
    if ch ==1:
    #lets assign ingredients
        dishname = input("Enter name of dish ")
        r1 = Recipe(dishname)

        print("Enter ingredients, type ok to exit")

        while True:

            ingred = input("Enter ingredients: ")

            if ingred == "ok":
                    break   

            else:
                print("Enter amount for",ingred)
                amt = input("Amount: ")
                r1.assignIngredients(ingred,amt)

        dict = r1.giveList()

        print("The name of dish", r1.name,"has ingredients",dict)

        mainData[r1.name] = r1


    elif ch == 2:
        requiredDish = input("For what dish would you like a recipe for?")
        reqRecipe = mainData[requiredDish] #we have got an object now
        reqDictionary = reqRecipe.ingredientList
        print(reqDictionary)

    else:
        break

