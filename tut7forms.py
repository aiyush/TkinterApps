from tkinter import *

def sub():
    print("----------------Entries Begin----------------")
    print(f"\nname : {nameentry.get()}")
    print(f"age : {ageentry.get()}")
    print(f"email id : {emailentry.get()}")
    print(f"Button Checked : {bool(int(recieveval.get()))}")
    print("\n----------------Entries Complete----------------")

    with open("gui_records.txt", "a") as gr:
        gr.write(f"\n------------------------Entries Begin------------------------ \nname : {nameentry.get()} \nage : {ageentry.get()} \nemail id : {emailentry.get()} \nButton Checked : {bool({recieveval.get()})} \n------------------------Entries Complete------------------------")
    
    if "@" and ".com" in emailentry.get():
        pass
    else:
        print("Error: Invalid email id")
    return

root = Tk()

root.geometry("300x500")
root.maxsize(300,500)
root.minsize(300,500)

#Heading
Label(root, text = "Welcome to Tiru's forum :)", borderwidth = 4,
relief = RIDGE).grid( row = 1, columnspan = 2, ipadx = 62, ipady = 10
,sticky = N)

#Form questions
name = Label(root, text = "Name")
name.grid(row = 3, column = 0, sticky = W)

age = Label(root, text = "Age")
age.grid(row = 5,column = 0, sticky = W)

email = Label(root, text = "email id")
email.grid(row = 7, column = 0, sticky = W)

#form client input
#class types
nameval = StringVar()
ageval = IntVar()
emailval = StringVar()
recieveval = IntVar()

#getting the vals now
nameentry = Entry(root, textvariable = nameval)
nameentry.grid(row = 3, column = 1)
ageentry = Entry(root, textvariable = ageval)
ageentry.grid(row = 5, column = 1, sticky = E)
emailentry = Entry(root, textvariable = emailval)
emailentry.grid(row = 7, column = 1, sticky = E)
recieveentry = Checkbutton(text = "Do you wish to recieve \nupdates regularly?", variable = recieveval)
recieveentry.grid(row = 9, column = 1, sticky = W)

#Submitting the form
Button(text = "Submit", command = sub, relief = RAISED).grid(row = 12, column = 1)

root.mainloop()