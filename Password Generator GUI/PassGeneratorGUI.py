from tkinter import *
import random
import string
root = Tk()
root.title(" Password Generator")
root.geometry("400x350")
root.resizable(False, False)
genpass2 = StringVar()
def Passwordgen():

    letter = string.ascii_uppercase
    letter2 = string.ascii_lowercase
    digit = string.digits
    punc = string.punctuation


    ch = random.choice(letter)
    ch4 = random.choice(letter2)
    ch2 = random.choice(digit)
    ch3 = random.choice(punc)
    genpass = ch + ch2 + ch3 + ch4

    sample=" "
    for i in range(passw.get()):
        char_type = random.choice(genpass)  # to randomize the occurance of alphabet, digit or symbol
        sample = sample + random.choice(char_type)


    genpass2.set(sample)


root.config(background="#ffffe0")
# Declare variables
passw = IntVar()


# Design labels
Label(root, text="Password Generator", bg="#ffffe0", fg="#E74C3C", font="verdana 22 ").place(x=60, y=10)
Label(root, text="-------------------------------------------------", bg="#ffffe0", fg="#E74C3C"
            , font="verdana 12 ").place(x=15, y=50)

Label(root, text="Enter Password length ", bg="#2C3E50", fg="#EAECEE", font="verdana 10 bold"
            , padx=2, pady=2).place(x=7, y=100)
Entry(root,textvariable=passw,font="verdana 12", width=30).place(x=7, y=120)
#length = Spinbox(root, from_ = 4, to_ = 32 , textvariable = pass_len , width = 24, font='arial 16').pack()

Button(root, text="Generate", bg="#fdde6c", fg="#000", font="verdana 12 "
        , command=Passwordgen, relief=GROOVE).place(x=7, y=180)

Label(root, text="Generated Password", bg="#2C3E50", fg="#EAECEE"
            , font="verdana 10 bold", padx=2, pady=2).place(x=7, y=250)
Entry(root, textvariable=genpass2, width=35, font="verdana 12").place(x=7, y=270)

statusvar = StringVar()
statusvar.set("By Mayuri Narute")
Label(root, textvariable=statusvar, relief=GROOVE,  bg="#ffffe0"
            , fg="#2C3E50", width=60).place(x=-1, y=328)
root.mainloop()