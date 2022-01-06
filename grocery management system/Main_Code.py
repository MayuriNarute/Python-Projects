import pyttsx3
import customer_login
import admin
all_products = [
    [1, 'milk', 20, 200],
    [2, 'biscuit', 100, 30],
    [3, 'Rice',200, 5],
    [4, 'peas',    100, 10],
    [5, 'wheat',120, 50]
]
text_speech=pyttsx3.init()
msg="Welcome to Raj Laxmi grocery store "
msg2="THANKU FOR VISITING OUR store "
def banner():

    print("\t\t=================================================================")
    print("\t\t\t\tRaj Laxmi Grocery Store")
    print("\t\t________________________________________________________________")
    print("\t\t\t\t1.Admin Login")
    print("\t\t\t\t2.Customer Login")
    print("\t\t\t\t3.Exit")
    print("\t\t================================================================")

text_speech.say(msg)
text_speech.runAndWait()
msg3=" please Enter your choice "
while (True):

    banner()
    print("Enter your choice :")

    choice = int(input())
    if choice == 1:
        text_speech.say("You have entered in Admin section")
        text_speech.runAndWait()
        admin.addminfun()

    elif choice == 2:
        text_speech.say("You have entered in customer section")
        text_speech.runAndWait()
        customer_login.cut()

    elif choice==3:

        print("\t\t________________________________________________________________")
        print("\t\t\t\tTHANKU FOR VISITING OUR Store :)")
        print("\t\t________________________________________________________________")
        text_speech.say("THANKU FOR VISITING OUR Store")
        text_speech.runAndWait()
        break

3