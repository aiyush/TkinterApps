from tkinter import *
import tkinter.messagebox as tmsg
import sys
import os

def rate():
    a = myslider.get()
    if a <= 7:
        tmsg.showinfo("Ohh no!!","Sorry for the bad experience.We will take this into account and improve upon our mistakes")
    else:
        tmsg.showinfo("Thanks",f"Thanks for the {a} stars.Hope to see you soon")

    
    with open("rating.txt", "a+") as w:
        w.write(f"The user gave a rating of {a} stars"+"\n\n")

    return

root = Tk()

root.geometry("320x300")
myslider = Scale(root, from_=0, to_=10, orient = HORIZONTAL, tickinterval = 1)
myslider.pack()

mybutton = Button(root, text = "Rate", command = rate)
mybutton.pack()

root.mainloop()