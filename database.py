import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "rollsroyce",
    database = "recipe"
)

mycursor = db.cursor()

#mycursor.execute("create database pythonfun")

def insertValue(name,*ing,time,diet):
    #print(name)
    ingredients = ', '.join(ing)
    mycursor.execute("insert into recipes(name, ingredient_list,cooktime,diet) values(%s,%s,%s,%s)",(name, ingredients, time,diet))
    db.commit()

def givenames():
    nameList = []
    mycursor.execute("select name from recipes")

    for x in mycursor:
        nameList.append(x)

    return nameList
        

def giveInfo(nameOfFood):
    info = []

    mycursor.execute("select * from recipes where name = %s",(nameOfFood))
    
    for x in mycursor:
        info.append(x)
    return info


givenames()