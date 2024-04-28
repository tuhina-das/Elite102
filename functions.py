import mysql.connector
import time

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
    
    isChecking = True
    while (isChecking):
        chosenAccount = int(input("\nPick an account (1, 2, 3, etc.) >>>> "))
        if (chosenAccount > 0 and chosenAccount <= len(myresult)):
            print("Checking balance...")
            time.sleep(2)
            cursor.execute(f"SELECT balance FROM Checking_Accounts WHERE name='{myresult[chosenAccount-1][0]}' AND uid={uid}")
            myresult = cursor.fetchall()
            print(f"\nBalance: ${"{:.2f}".format(myresult[0][0])}")
            isChecking = False
        else:
            print("Invalid account chosen Try again or `Ctrl+C` to exit.")    
    cursor.close()
    connection.close()

# deposit funds and withdraw funds
def changeBalance(uid, isDeposit):
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
    isChecking = True
    while (isChecking):
        chosenAccount = int(input(f"\nPick an account to {changeType} (1, 2, 3, etc.) >>>> "))
        if (chosenAccount > 0 and chosenAccount <= len(myresult)):
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
            print("Invalid account chosen Try again or `Ctrl+C` to exit.")    
    cursor.close()
    connection.commit()
    connection.close()

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
        unsure = False if (input("Are you sure you want to pick thi option? (Y or N) >>>> ")=='Y') else True
    
    # if the user doesn't want to delete their acc, exit
    if (userOption != 6):
        print("Deleting account ... ")
        time.sleep(3)
        cursor.execute(f"DELETE FROM Checking_Accounts WHERE uid={uid} AND name='{myresult[userOption-1][0]}'")
        cursor.close()
        connection.commit()
        connection.close()
        print("Account deleted!")
    else:
        print("Returning to main menu ... ")
        time.sleep(3)
        
# # modifying account details
