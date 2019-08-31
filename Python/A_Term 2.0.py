#Testing breaks in this file because I have no idea what I'm doing.
import time
import os



print("Starting system...")
time.sleep(1)


x = 3
while x > 0:
    print("Startup in" , x)
    time.sleep(.5)
    x = x - 1
    if x == 0:
        break


print("System startup successful")
input("Press Enter to begin...")



os.system('cls')

# Asks the user what their passcode is, then defines "pass_code":
print("Hello, what is your passcode?")
pass_code = input()


# Determines what to do for each "pass_code" input:
if pass_code == "1234":
    os.system('cls')
    print("Welcome Level 1 staff, what would you like to do today?")
    answer1 = input()
    if answer1 == "test":
       os.system('cls') 
       print("Test successful")
       input("Press Enter key to exit")
    if answer1 == "crash sys":
        os.system('cls')
        print("You are not authorized for this command!")
        time.sleep(.900)
        print("Locking Terminal...")
        time.sleep(2)

elif pass_code == "6524":
    os.system('cls')
    print("Welcome Level 10 staff, what would you like to do today?")
    answer1 = input()
    if answer1 == "test":
       os.system('cls') 
       print("Test successful")
       input("Press Enter key to exit")
    elif answer1 == "crash sys":
        os.system('cls')
        print("Please wait...")
        time.sleep(.900)
        os.system('cls')
        print("!ERROR! Fatal exception has occured! Terminating program...")
        time.sleep(1.5)
    elif answer1 == "access main network":
        os.system('cls')
        print("Accessing network teminal...")
        time.sleep(2)
        os.system('cls')
        print("Unable to access network, sorry!")
        input("Press Enter key to exit")
    else:
        os.system('cls')
        print("Invalid command")
        input("Press Enter key to exit")


elif pass_code == "Vadim":
    while 3 > 2:
        print("Vadim blyat")

else:
    os.system('cls')
    print("Unfortunately, you are not authorized, have a nice day!")
    input("Press Enter key to exit")
