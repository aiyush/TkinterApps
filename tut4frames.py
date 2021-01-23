from tkinter import *

root = Tk()

root.geometry("300x700")

f1 = Frame(root,borderwidth = 4, bg = "grey", relief = RIDGE)
txt1 = Label(f1, text = "This is the 1st frame in this gui",
bg = "grey", fg = "white", font = "Helvetica 10 bold")
f1.pack(side = LEFT, anchor = "w", fill = Y)
txt1.pack(pady = 100)

f2 = Frame(root, borderwidth = 4,bg = "grey", relief = RIDGE)
txt2 = Label(f2, text = "This is the 2nd frame in this gui",
fg = "white", bg = "grey", font = "Roboto 10 italic")
f2.pack(side = TOP, anchor = "n", fill = X)
txt2.pack(padx = 100)

root.mainloop()