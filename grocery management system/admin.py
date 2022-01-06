import pyttsx3
import  productlist

def banner():
    print("\t\t=================================================================")
    print("\t\t\t\tRaj Laxmi Grocery Store")
    print("\t\t_________________________________________________________________")
    print("\t\t\t\t1.Show All Products")
    print("\t\t\t\t2.Add Products")
    print("\t\t\t\t3.Remove Product")
    print("\t\t\t\t4.Exit")
    print("\t\t================================================================")


def display_all():
    print("\t\t________________________________________________________________")
    print("\t\t\tSNO\tProduct\t\tPrice")
    print("\t\t________________________________________________________________")
    for item in productlist.all_products:
        print("\t\t\t{0}\t{1}\t\t{2}".format(item[0], item[1], item[2]))

text_speech=pyttsx3.init()
msg="please Enter your choice"
msg2="Enter your Admin Id"
msg3="Enter your password"
def addminfun():
    print("Enter Admin UserID: ")
    text_speech.say(msg2)
    text_speech.runAndWait()
    username = input()
    print("Enter the Password: ")
    text_speech.say(msg3)
    text_speech.runAndWait()
    password = input()
    if username != "rajlaxmiadmin" and password != "rajlaxmi@10":
         print("Please enter correct Username and Password")
    else:
        print("\n\tAdmin Login Successfully...")
        text_speech.say("admin login successfully")
        text_speech.runAndWait()
        while (True):
            banner()
            print("Enter your choice :")
            choice = int(input())
            if choice == 1:
                display_all()

            elif choice == 2:
                ts = 0

                prod = []
                prod.append(len(productlist.all_products) + 1)
                prod.append(input("Enter the Product Name: "))
                prod.append(int(input("Product Price: ")))
                productlist.all_products.append(prod)
                ts = 1
                if ts == 1:
                    print("\t\tProduct Added Successfully....\n")
                    text_speech.say("Product added successfully")
                    text_speech.runAndWait()
                else:
                    print("\t\t...Incorrect username and password...")

            elif choice == 3:
                rid = int(input("Enter item id to remove"))
                productlist.all_products.pop(rid - 1)
                print("\t\t...Item has been Removed...\n")
                text_speech.say("item hass been removed")
                text_speech.runAndWait()


            elif choice == 4:
                break
