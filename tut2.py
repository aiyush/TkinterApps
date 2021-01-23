from  tkinter import *
from PIL import Image,ImageTk
import os

root = Tk()

root.geometry("300x400")
root.minsize(100,100)
root.maxsize(600,1400)

img = Image.open("background-montagne-6.jpg")
imgo = ImageTk.PhotoImage(img)

imgo_label = Label(image = imgo)
imgo_label.pack()

root.mainloop()