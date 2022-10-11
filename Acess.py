
from random import randrange
from struct import pack
import time

#--------------------------------------------------------------------------
def execution():
    print("-----------------------------------------------")
    print("This is true")
    time.sleep(4)
    dictionary = {"Cat":"Meet", "Goat":"Herbs", "Monkey":"Fruits"}
    for key in dictionary.keys():
        print(key, "->", dictionary[key])
        time.sleep(1)
    time.sleep(5)
    print("--------------------------------------------------")
    print("Thank you for compliting all")
    print("--------------------------------------------------")
    return commpliting_data()

#-------------------------------------------------------------------------
def access(password):
    passw = password
    time.sleep(3)
    print("Enter the password that was generated for you above...")
    try:
        password1 = int(input("Please Enter the password here: "))
        if(password1 == passw):
          print("You have an access")
          return execution()
        else:
            print("Sorry your password is wrong! didn't you memorize it?")
            print("-----------------------------------------------")
            return access(password)
    except:
            print("Sorry your password is wrong! didn't you memorize it?")
            print("-----------------------------------------------")
            return access(password)
#--------------------------------------------------------------------------
def commpliting_data():
    name = str(input("Enter your full name: "))
    if(name == "" or name == "  " or name == "   " or name == "    " \
       or name == "     " or name == "     " or name == "      " or name == " "):
        print("Please! complite your name the chart cannot be empty")
        time.sleep(2)
        print("-----------------------------------")
        return commpliting_data()
    else:
        sexe_complete(name)
#--------------------------------------------------------------------------
def sexe_complete(name):
    sexe = str(input("Enter your sexe: "))
    if(sexe == "M"):
        print("Hello Mr " + name)
    elif(sexe == "F"):
        print("Hello Madam " + name)
        print("-----------------------------------------------")
    elif (sexe == "m"):
        print("The sexe must be in a capital letter!")
        print("-----------------------------------------------")
        return sexe_complete(name)
    elif (sexe == "f"):
        print("The sexe must be in a capital letter!")
        print("-----------------------------------------------")
        return sexe_complete(name)
    else:
        print("Sorry this kind of sexe doesn't exist...")
        time.sleep(3)
        print("-----------------------------------------------")
        return sexe_complete(name)
#--------------------------------------------------------------------------
    age = int(input("Enter your age: "))
    if (age < 18):
        print("Sorry you cannot have an access!")
        print("-----------------------------------------------")
        return commpliting_data()
    elif(age == 18):
        print("You are 18 years old you must have an experience")
        time.sleep(2)
        password = randrange(1000, 100000)
        print("This is your confirmation password: ", password)
        print("Welcome to the another page...")
        print("-----------------------------------------------")
        return access(password)
    elif(age > 18):
        print("You are allowed for all")
        time.sleep(2)
        password = randrange(1000, 100000)
        print("This is your confirmation password: ", password)
        print("Welcome to the another page...")
        print("-----------------------------------------------")
        return access(password)
#-------------------------------------------------------------------------------
print("Hello! this is the beginning of the program...")
print("-----------------------------------------------")
commpliting_data()

