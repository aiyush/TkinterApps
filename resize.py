from tkinter import *

def res():
    w = str(xentry.get())
    h = str(yentry.get())
    root.geometry(w+"x"+h)
    return

root = Tk()

root.geometry("400x400")
#root.minsize(400,400)
#root.maxsize(400,400)

Label(root, text = "Enter the resolution in which you want to resize this window",bg = "#87afff", relief = RIDGE).pack(anchor = "n", side = TOP , ipadx = 40, ipady = 30)

xf = Frame(root, borderwidth = 2)
xf.pack(side = TOP, fill = X)

yf = Frame(root, borderwidth = 2)
yf.pack(side = TOP, fill = X)

buttn = Frame(root, borderwidth = 2)
buttn.pack(side = TOP, fill = X)
# Making a label for width

x = Label(xf, text = "Enter the Width of this window")
x.pack(side = LEFT)

# making an entry space for width
xval = IntVar()
xentry = Entry(xf, textvariable = xval, relief = RIDGE)
xentry.pack(side = RIGHT)

# making a label for height
y = Label(yf, text = "Enter the Height of this window")
y.pack(side = LEFT)

# making an entry space for height
yval = IntVar()
yentry = Entry(yf, textvariable = yval)
yentry.pack(side = RIGHT)

# making an apply button
Button(buttn, text = "Apply", command = res).pack(side = BOTTOM, anchor = "s")

root.mainloop()