from tkinter import *

def getvals():
    print(f"The username is {usrvalue.get()}")
    print(f"The password is {passvalue.get()}")
    return

root = Tk()

root.geometry("300x700")

user = Label(root, text = "Username: ")
user.grid(row = 1, column = 3)

password = Label(root, text = "Password: ")
password.grid(row = 3, column = 3)

#Types of variables represented in tkinter are:
#BooleanVar, DoubleVar, IntVar, StringVar

usrvalue = StringVar()
usrentry = Entry(root, relief = SUNKEN, textvariable = usrvalue) 
usrentry.grid(row = 1, column = 4)

passvalue = StringVar()
passentry = Entry(root, relief = SUNKEN, textvariable = passvalue)
passentry.grid(row = 3, column = 4)

btn = Button(root, text = "Submit", relief = RAISED, command = getvals)
btn.grid(row = 5, column = 5)

root.mainloop()