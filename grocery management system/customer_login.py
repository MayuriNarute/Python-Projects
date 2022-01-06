from builtins import print
from datetime import datetime
import random
import sys
import productlist
import  pyttsx3

def cut():



    def banner():
        print("\t\t=================================================================")
        print("\t\t\t\tRaj Laxmi Grocery Store")
        print("\t\t________________________________________________________________")
        print("\t\t\t\t1.Show All Products")
        print("\t\t\t\t2.Buy Product")
        print("\t\t\t\t3.Remove Products from cart")
        print("\t\t\t\t4.Show Order Details")
        print("\t\t\t\t5.Exit")
        print("\t\t=================================================================")

    def display_all():
        print("\t\t_____________________________________")
        print("\t\t\tSNO\tProduct\t\tPrice")
        print("\t\t_____________________________________")
        for item in productlist.all_products:
            print("\t\t\t{0}\t{1}\t\t{2}".format(item[0], item[1], item[2]))
        print("\t\t_____________________________________")
        print()

    #
    def order_summary(bill, name, list):
        print("\t\t**____________________________________________________________**")
        print("\t\t\t\tRaj Laxmi Grocery Store")
        print("\t\t**____________________________________________________________**")
        print("\t\t\t\tOrder Summary\tDate:{}".format(str(datetime.now())))
        print("\t\t\t\tCustomer Name: " + name)
        print("\t\t\t\t\t(( YOUR PURCHASED ITEMS ))")
        print("\t\t________________________________________________________________")
        for item in list:
            print("\t\t\t\t{0}\t{1}\t{2}".format(item[0], item[1], item[2]))
        print("\t\t________________________________________________________________")
        print("\t\t\t\tTotal Amount:  " + str(bill))
        print("\t\t\t\tTax Amount :"+ str(0.13 * bill))
        print("\t\t\t\tTotal Cost :"+ str(bill+0.13*bill))
        print("\t\t________________________________________________________________")
        print("\t\t\t\tTHANKU FOR SHOPPING, VISIT AGAIN...")

    text_speech = pyttsx3.init()
    Buylist = []
    addi = 0
    cust_name = ''
    index=len(productlist.all_products)
    while (True):
        banner()
        print("Enter your choice :")

        choice = int(input())
        if choice == 1:
            display_all()
        elif choice == 2:
            display_all()
            cust_name = input("Enter your name :")
            n = int(input("Enter how many products you want to buy :"))
            print("Which product you want to buy (enter item id):- ")
            for i in range(0, n):
                id = int(input())
                Buylist.append(productlist.all_products[id - 1])
                addi = addi + productlist.all_products[id - 1][-1]
                no=len(Buylist)

            print("\tTotal Amount is:- " + str(addi))
            print("\t\t...Thanks For shopping with Us...\n")
            text_speech.say("thanku for shopping with us")
            text_speech.runAndWait()

        elif choice == 3:

                if Buylist == []:
                    print("\t\t...Your cart is empty, please purchase some products first!...\n")
                    text_speech.say("Your cart is empty, please purchase some products first")
                    text_speech.runAndWait()
                else:
                    rid = int(input("Enter item id to remove"))

                    Buylist.pop(rid - 1)
                    priceofid = productlist.all_products[rid - 1][-1]
                    addi = addi - priceofid
                    print("\tTotal Amount is:- " + str(addi))


        elif choice == 4:
            if Buylist == []:
                print("\t\t...Your cart is empty, please purchase some products first!...\n")
                text_speech.say("Your cart is empty, please purchase some products first")
                text_speech.runAndWait()
            else:
                print("\t\t*_____________________________________________________________*")
                print("\t\t\t\t(( YOUR FINAL ORDER BILL ))")
                text_speech.say("your final order bill")
                text_speech.runAndWait()
                order_summary(addi, cust_name, Buylist)

        elif choice == 5:
            print("\t\t________________________________________________________________")
            print("\t\t\t\tTHANKU FOR VISITING OUR Store:)")
            print("\t\t________________________________________________________________")
            text_speech.say("thanku for visiting our store please visit again")
            text_speech.runAndWait()
            break