from tkinter import *

def coords(event):
    print(f"The current position of the button on the screen is: x = {event.x}, y = {event.y}")
    return

root = Tk()

root.geometry("300x500")
root.title("Experimenting with Event handlings")
btn = Button(root, text = "Khlikh")
btn.pack(side = TOP, anchor = "n")

#To see all the events,google it
btn.bind('<Button-1>', coords)
btn.bind('<Double-Button-1>', quit)

root.mainloop()