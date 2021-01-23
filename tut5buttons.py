from tkinter import *

def on():
    print("On")
    return

root = Tk()

root.geometry("600x300")
root.minsize(600,300)
root.maxsize(600,300)

f1 = Frame(root, bg = "grey", padx = 40, pady = 40, 
borderwidth = 5, relief = RIDGE)
f1.pack(side = LEFT,fill = BOTH)
b1 = Button(f1, bg = "#3586c4", text = "Bulb1", command = on)
b1.pack(side = TOP)

f2 = Frame(root, bg = "grey", padx = 40, pady = 40, 
borderwidth = 5, relief = RIDGE)
f2.pack(side = LEFT,fill = BOTH)
b2 = Button(f2, bg = "#3586c4", text = "Bulb2", command = on)
b2.pack(side = BOTTOM, fill = BOTH)

f3 = Frame(root, bg = "grey", padx = 40, pady = 40, 
borderwidth = 5, relief = RIDGE)
f3.pack(side = LEFT,fill = BOTH)
b3 = Button(f3, bg = "#3586c4", text = "Bulb3", command = on)
b3.pack(side = TOP)

f4 = Frame(root, bg = "grey", padx = 40, pady = 40, 
borderwidth = 5, relief = RIDGE)
f4.pack(side = LEFT, fill = BOTH)
b4 = Button(f4, bg = "#3586c4", text = "Bulb4", command = on)
b4.pack(side = TOP)
root.mainloop()