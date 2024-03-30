import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "rollsroyce",
    database = "recipe"
)



mycursor = db.cursor(buffered=True)

#mycursor.execute("create database pythonfun")

def insertValue(name,ing,time,diet):
    #print(name)
    ingredients = ', '.join(ing)
    mycursor.execute("insert into recipes(name, ingredient_list,cooktime,diet) values(%s,%s,%s,%s)",(name, ingredients, time,diet))
    db.commit()

def givenames():
    nameList = []
    mycursor.execute("select distinct name from recipes")

    for x in mycursor:
        nameList.append(x)

    return nameList
        

def giveInfo(nameOfFoodTuple):
    info = {}
    ings = []

    print("Name of food 1:", nameOfFoodTuple)  # Debugging print

    if isinstance(nameOfFoodTuple, tuple):
        nameOfFood = nameOfFoodTuple[0]
    else:
        nameOfFood = nameOfFoodTuple

    print("Name of food 2:", nameOfFood)  # Debugging print
    #print(type(nameOfFood))

    mycursor.execute("select diet from recipes where name = %s", (nameOfFood,))
    diet_result = mycursor.fetchone()
    if diet_result:
        info['diet'] = diet_result[0]
    else:
        info['diet'] = "Information not available"

    print('diet',diet_result)

    mycursor.execute("SELECT cooktime FROM recipes WHERE name = %s", (nameOfFood,))
    cooktime_result = mycursor.fetchone()
    if cooktime_result:
        info['cooktime'] = cooktime_result[0]
    else:
        info['cooktime'] = "Information not available"

    print(cooktime_result)

    mycursor.execute("SELECT ingredient_list FROM recipes WHERE name = %s", (nameOfFood,))
    ingredient_results = mycursor.fetchall()
    for row in ingredient_results:
        ings.append(row[0])
    info['ingredients'] = ings
    print(ingredient_results)

    info['name'] = nameOfFood

    print(info)

    return info

def searchByIngredient(*list3):

    print(list3)

    query = "select distinct name from recipes r where "

    counter = 1

    for list2 in list3:
        for mylist in list2:
            for ingred in mylist:
                if counter > 1:
                    query = query + ' and '

                query = query + f"EXISTS (SELECT 1 FROM recipes r1 WHERE r.name = r1.name AND r1.ingredient_list = '{ingred}')"

                counter +=1

                
    query = query + ';'

    print(query)

    mycursor.execute(query)

    info = []
    for x in mycursor:
        info.append(x)

    print(info)

    return info
    
#giveInfo('random')

def addIngredsToDatabase(ingred):
    mycursor.execute("insert into ingredients(name) values(%s)",(ingred,))
    db.commit()


def giveIngredients():
    mycursor.execute("select distinct name from ingredients")
    ingredientList = []

    for i in mycursor:
        ingredientList.append(i)
    
    print(ingredientList)

    return ingredientList
    

givenames()