import mysql.connector
import time
import os

# function to retrieve checking balance
def checkBalance(uid):
    # retrieve all the accounts associated with the user's UID. 
    # will require an SQL statement - SELECT * FROM checking_accounts WHERE uid = {uid}
    # create a connection and cursor
    connection = mysql.connector.connect(user = 'root', database = 'c2c_bank', password = '')
    cursor = connection.cursor()

# get all the accounts and print them for the user to pick
    cursor.execute(f"SELECT name FROM Checking_Accounts WHERE uid={uid}")
    myresult = cursor.fetchall()
    count = 0
    for x in myresult:
        count+=1
        print(f"{count}.) " + x[0])
    print("----------------")
    
# run a loop that lets the user pick an account to check their balance
    isChecking = True
    while (isChecking):
        chosenAccount = int(input("\nPick an account (1, 2, 3, etc.) >>>> "))
        # once the user has chosen an account, use sql to retrieve and format the data of that account
        if (chosenAccount > 0 and chosenAccount <= len(myresult)):
            os.system('clear')
            print("Checking balance...")
            time.sleep(2)
            cursor.execute(f"SELECT balance FROM Checking_Accounts WHERE name='{myresult[chosenAccount-1][0]}' AND uid={uid}")
            myresult = cursor.fetchall()
            print(f"\nBalance: ${"{:.2f}".format(myresult[0][0])}")
            isChecking = False
        else:
            os.system('clear')
            print("Invalid account chosen Try again or `Ctrl+C` to exit.")    
    cursor.close()
    connection.close()
    return True

# deposit funds and withdraw funds
def changeBalance(uid, isDeposit):
    # create a connection and give the user options to pick from 
    changeType = "deposit" if (isDeposit) else "withdraw"
    changeTypeSQL = "+" if (isDeposit) else "-"
    connection = mysql.connector.connect(user = 'root', database = 'c2c_bank', password = '')
    cursor = connection.cursor()
    cursor.execute(f"SELECT name FROM Checking_Accounts WHERE uid={uid}")
    myresult = cursor.fetchall()
    count = 0
    for x in myresult:
        count+=1
        print(f"{count}.) " + x[0])
    print("----------------")
    
    # have the user pick an account
    isChecking = True
    while (isChecking):
        chosenAccount = int(input(f"\nPick an account to {changeType} (1, 2, 3, etc.) >>>> "))
        if (chosenAccount > 0 and chosenAccount <= len(myresult)):
            os.system('clear')
            dollarAmount = "{:.2f}".format(float(input(f"What amount would you like to {changeType}? >>> ")))
            cursor.execute(f"UPDATE Checking_Accounts SET balance = balance {changeTypeSQL} {dollarAmount} WHERE uid = {uid} AND name = '{myresult[chosenAccount-1][0]}'")
            # give the user feedback on their new balance
            cursor.execute(f"SELECT balance FROM Checking_Accounts WHERE name='{myresult[chosenAccount-1][0]}' AND uid={uid}")
            myresult = cursor.fetchall()
            # print(myresult)
            balance = float("{:.2f}".format(myresult[0][0]))
            print(f"\nYour new balance: ${balance}")
            if (balance < 0):
                print("Your balance is negative, and you're in debt! Please make a deposit soon.")
            isChecking = False
        else:
            os.system('clear')
            print("Invalid account chosen Try again or `Ctrl+C` to exit.")    
    cursor.close()
    connection.commit()
    connection.close()
    return True

# # creating a new acc
def createAccount(uid):
    accName = input(f"What would you like to name this account? >>>> ")
    startAmt = 0
    if (input("Would you like to make a starting deposit for this new account (Y or N)? >>>> ") == 'Y'):
        startAmt = float("{:.2f}".format(float(input("Please specify an amount >>>> "))))
    connection = mysql.connector.connect(user = 'root', database = 'c2c_bank', password = '')
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Checking_Accounts(uid, balance, name) VALUES({uid}, {startAmt}, '{accName}')")
    myresult = cursor.fetchall()
    cursor.close()
    connection.commit()
    connection.close()
    print("New account created!")
    return True

# # deleting acc
def deleteAccount(uid):
    # create connection
    connection = mysql.connector.connect(user = 'root', database = 'c2c_bank', password = '')
    cursor = connection.cursor()
    # get all accounts to provide a menu for users to pick from
    cursor.execute(f"SELECT name FROM Checking_Accounts WHERE uid={uid}")
    myresult = cursor.fetchall()
    count = 0
    for x in myresult:
        count+=1
        print(f"{count}.) " + x[0])
    print("6.) I don't want to delete an account. Return to main menu.")
    print("----------------\n")
    unsure = True
    userOption = 0
    # while the user is deciding what account to pick, loop. 
    # provide a reminder that the user can always exit using `Ctrl+C` if they don't want to delete their account
    while (unsure):
        userOption = int(input("Pick an account to delete >>>> "))
        unsure = False if (input("Are you sure you want to pick this option? (Y or N) >>>> ")=='Y') else True
    
    # if the user wants to proceed, then proceed
    if (userOption != 6):
        os.system('clear')
        print("Deleting account ... ")
        time.sleep(3)
        cursor.execute(f"DELETE FROM Checking_Accounts WHERE uid={uid} AND name='{myresult[userOption-1][0]}'")
        cursor.close()
        connection.commit()
        connection.close()
        print("Account deleted!")
    # if the user doesn't want to delete their acc, exit
    else:
        os.system('clear')
        print("Returning to main menu ... ")
        time.sleep(3)
    return True
        
# # modifying account details
def updateAccount(uid, name):
    # first, retrieve all accounts and have the user pick an account
    connection = mysql.connector.connect(user = 'root', database = 'c2c_bank', password = '')
    cursor = connection.cursor()
    
    # get all accounts to provide a menu for users to pick from
    cursor.execute(f"SELECT name FROM Checking_Accounts WHERE uid={uid}")
    myresult = cursor.fetchall()
    count = 0
    for x in myresult:
        count+=1
        print(f"{count}.) " + x[0])
    print("6.) I don't want to modify an account. Return to main menu.")
    print("----------------\n")
    
    unsure = True
    accountChoice = 0
    # while the user is deciding what account to pick, loop. 
    # provide a reminder that the user can always exit using `Ctrl+C` if they don't want to delete their account
    while (unsure):
        accountChoice = int(input("Pick an account to modify >>>> "))
        unsure = False if (input("Are you sure you want to pick this option? (Y or N) >>>> ")=='Y') else True
        
    # if the user wants to proceed, then proceed. save the old account details.
    if (accountChoice != 6):
        os.system('clear')
        oldName = myresult[accountChoice-1][0]
        #provide the user with a display of the account, its name, balance, and owner
        print("\nAccount Details:\n----------------")
        print(f"Name: {myresult[accountChoice-1][0]}")
        cursor.execute(f"SELECT balance FROM Checking_Accounts WHERE name='{myresult[accountChoice-1][0]}' AND uid={uid}")
        myresult = cursor.fetchall()
        print(f"Balance: ${"{:.2f}".format(myresult[0][0])}")
        print(f"Owner: {name}\n----------------\n")
        balance = myresult[0][0]
        
        # offer options to modify the account: either name or owner
        unsure = True
        userOption = 0
        while (unsure):
            print("Your Options:\n----------------\n1.) Change account name")
            print("2.) Transfer ownership")
            userOption = int(input("\nPick an action >>>> "))
            unsure = False if (input("Are you sure you want to pick this option? (Y or N) >>>> ")=='Y') else True
        
        # if user chose to change account name
        if (userOption != 1 or userOption!= 2):
            os.system('clear')
            if (userOption == 1):
                newName = input("\nWhat would you like your account's new name to be? >>>> ")
                cursor.execute(f"UPDATE Checking_Accounts SET name = '{newName}' WHERE name='{oldName}' AND uid={uid}")
            # elif user chose to transfer ownership
            elif(userOption == 2):
                newOwner =int(input("\nPlease type in the UID of the user you would like to transfer this account to >>>> "))
                cursor.execute(f"UPDATE Checking_Accounts SET uid = {newOwner} WHERE name='{oldName}' AND uid={uid}")
                # if transferring ownership, save to a new uid
                uid = newOwner
            print("Updating your account ... ")
            time.sleep(3)
            print("Done!")
            
            # after updating details, print out the user's new account information (a list of all accounts)
            # if an account is missing, it's been transferred
            # if an account's name is different, it's been modified
            
            cursor.execute(f"SELECT name FROM Checking_Accounts WHERE uid={uid}")
            myresult = cursor.fetchall()
            count = 0
            os.system('clear')
            print("\n\n----------------\nYour accounts:")
            for x in myresult:
                count+=1
                print(f"{count}.) " + x[0])
            print("----------------\n")
            
            cursor.close()
            connection.commit()
            connection.close()
                
            
    # if the user doesn't want to delete their acc, exit
    else:
        os.system('clear')
        print("Returning to main menu ... ")
        time.sleep(3)
    return True
