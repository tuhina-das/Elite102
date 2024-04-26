import functions
import mysql.connector
import time

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
def menu(uid):
    isDeciding = True
    while (isDeciding):
        print("Your options are:\n----------------\n1.) Check my balance\n2.) Make a withdrawal/deposit\n3.) Create a new account\n4.) Edit account details\n5.) Delete an account\n6.) Quit\n----------------\n")
        userInput = int(input("Pick an option >>>> "))
        if (userInput==6):
            isDeciding=False
        elif (userInput==1):
            print("\n\n----------------\nYour accounts:")
            functions.checkBalance(uid)
            isDeciding=False
        elif (userInput==2):
            print("Make a withdrawal/deposit")
            isDeciding=False
        elif (userInput==3):
            print("Create a new account")
            isDeciding=False
        elif (userInput==4):
            print("Edit an account")
            isDeciding=False
        elif (userInput==5):
            print("Delete an account")
            isDeciding=False

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
        print(f"Welcome, {name}! What would you like to do today?")
        menu(uid)
    else: 
        print("Unsuccessful login, try again.")
        # TODO: option to exit
        # x = input("Would you like to try again? (Y or N) >>> ")
        # if (x=='Y'):
        #     return 
        