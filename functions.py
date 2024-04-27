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
    changeType = "deposit" if (isDeposit) else "withdrawal"
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
        chosenAccount = int(input(f"\nPick an account to make a {changeType} (1, 2, 3, etc.) >>>> "))
        if (chosenAccount > 0 and chosenAccount <= len(myresult)):
            dollarAmount = "{:.2f}".format(float(input(f"What amount would you like to {changeType}? >>> ")))
            cursor.execute(f"UPDATE Checking_Accounts SET balance = balance {changeTypeSQL} {dollarAmount} WHERE uid = {uid} AND name = '{myresult[chosenAccount-1][0]}'")
            # give the user feedback on their new balance
            cursor.execute(f"SELECT balance FROM Checking_Accounts WHERE name='{myresult[chosenAccount-1][0]}' AND uid={uid}")
            myresult = cursor.fetchall()
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
# def createAccount(uid):
    

# # deleting acc

# # modifying account details