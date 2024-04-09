user = "";
passW = "";

# function to loop through a welcome msg/options for the user
def option():
  # boolean to control loop
  exit = False

  # user choice input
  userInput = 0

  # loop to provide menu to user; for now, this will print what the user enters (if it's a valid option)
  while (exit == False):
    print(
        "Please choose from these options:\n1.) View my checking account balance\n2.) Make a deposit\n3.) Make a withdrawal\n4.) Update my account\n5.) Help\n6.) Exit"
    )
    userInput = input("What would you like to do today?  >>> ")
    if (userInput == "1"): # this will make an API call including the user's zip code to find schools nearby
      # write a function to get nearby schools
      exit = True
      print("Option 1\n")
      exit=True;
    elif (userInput == "2"):
      print("Option 2")
      exit=True;
    elif (userInput == "3"):
      print("Option 3")
      exit=True;
    elif (userInput == "4"):
      print("Option 4")
      exit=True
    elif (userInput == "5"):
      print("option 5")
      exit = True
    elif (userInput == "6"):
      print("Goodbye!")
      exit = True
    else:
      continue

def login(userName, userPass):
#   SQL STUFF!! we want to connect this to the back end of our sql project
    # using the userName and userPass supplied, call a select query
    # if null is returned, display an incorrect login msg
    # else, save the user's userName and pass
    if (userName=='bob' and userPass == 'huhu'):
        user = userName;
        passW = userPass;
        print("\n")
        return True;
    else:
        print("\nUsername/Password is incorrect. Please try again.\n")


# main calls to function here
print("\n----------------------------------------------------------------")
print("    Welcome to Code2College Bank! Please log in to continue    ")
print("----------------------------------------------------------------\n")
# variable continuing to loop if login fails
isloggingIn = True
while (isloggingIn):
    userInput1 = input("Username: ")
    userInput2 = input("Password: ")
    if (login(userInput1, userInput2)==True):
       isloggingIn=False
       
option()