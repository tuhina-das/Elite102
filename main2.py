import functions
import mysql.connector
import time
import os

# login function
def login(userName, userPass):
    connection = mysql.connector.connect(user = 'root', database = 'c2c_bank', password = '')
    # print(connection)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Users WHERE username = '{userName}' AND password = '{userPass}'")
    myresult = cursor.fetchall()
    if not myresult:
        return False
    else:
        return True

# main menu function
def menu(uid, name):
    isDeciding = True
    while (isDeciding):
        print("Your options are:\n----------------\n1.) Check my balance\n2.) Make a withdrawal/deposit\n3.) Create a new account\n4.) Edit account details\n5.) Delete an account\n6.) Quit\n----------------\n")
        userInput = int(input("Pick an option >>>> "))
        if (userInput==6):
            isDeciding=False
        elif (userInput==1):
            os.system('clear')
            print("\n\n----------------\nYour accounts:")
            functions.checkBalance(uid)
            time.sleep(5)
            os.system('clear')
            isExiting = True if input("\nWould you like to do anything else? (Y or N) >>> ")=='Y' else False
            isDeciding=isExiting
        elif (userInput==2):
            os.system('clear')
            isDeposit = input("Would you like to make a deposit (D) or a withdrawal (W)? >>> ")
            print("\n\n----------------\nYour accounts:")
            functions.changeBalance(uid, (isDeposit=='D'))
            time.sleep(5)
            os.system('clear')
            isExiting = True if input("\nWould you like to do anything else? (Y or N) >>> ")=='Y' else False
            isDeciding=isExiting
        elif (userInput==3):
            os.system('clear')
            functions.createAccount(uid)
            time.sleep(5)
            os.system('clear')
            isExiting = True if input("\nWould you like to do anything else? (Y or N) >>> ")=='Y' else False
            isDeciding=isExiting
        elif (userInput==4):
            os.system('clear')
            print("\n\n----------------\nYour accounts:")
            functions.updateAccount(uid, name)
            time.sleep(5)
            os.system('clear')
            isExiting = True if input("\nWould you like to do anything else? (Y or N) >>> ")=='Y' else False
            isDeciding=isExiting
        elif (userInput==5):
            os.system('clear')
            print("\n\n----------------\nYour accounts:")
            functions.deleteAccount(uid)
            time.sleep(5)
            os.system('clear')
            isExiting = True if input("\nWould you like to do anything else? (Y or N) >>> ")=='Y' else False
            isDeciding=isExiting
    os.system('clear')
    print("Thank you for using our app. Have a lovely day!\n\n")

#---------------- MAIN SEQUENCE ----------------
print("\n----------------------------------------------------------------")
print("    Welcome to Code2College Bank! Please log in to continue    ")
print("----------------------------------------------------------------\n")

connection = mysql.connector.connect(user = 'root', database = 'c2c_bank', password = '')
cursor = connection.cursor()

isLoggingIn = True
while (isLoggingIn):
    userInput1 = input("Username >>> ")
    userInput2 = input("Password >>> ")
    if (login(userInput1, userInput2)):
        print("Login successful!\n")
        isLoggingIn = False
        cursor.execute(f"SELECT uid FROM Users WHERE username = '{userInput1}' AND password = '{userInput2}'")
        uid = cursor.fetchall()[0][0]
        cursor.execute(f"SELECT first_name FROM Users WHERE uid = {uid}")
        name = cursor.fetchall()[0][0]
        os.system('clear')
        print(f"Welcome, {name}! What would you like to do today?")
        menu(uid, name)
    else: 
        print("Unsuccessful login, try again.")
        