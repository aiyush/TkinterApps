from tkinter import *

root = Tk()

# Geometry of the board
root.geometry("1920x1080")

# Deviding the board into sections
bulbAlmirah1 = Frame(root,borderwidth = 4, relief = RIDGE)
bulbAlmirah1.pack(side = TOP, anchor = "ne", fill = Y)

root.mainloop()