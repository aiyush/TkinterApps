from tkinter import *
from PIL import Image,ImageTk

root = Tk()

# sizes take arguments in this order: width x height
root.geometry("728x920")

root.minsize(100,150)
root.maxsize(800,1000)

#Displaying texts in the box
txt = Label(text = "Hello there,I am being created for screen buttons!")
txt.pack()

#Displaying image in box
#NOTE: .jpg format is not supported by Tkinter for now
#So we use PIL module for converting the image into .png format
#photo = PhotoImage(file ="cocytus-overlord-crossdress-horns-demiurge-overlord-wallpaper-preview.jpg")

image = Image.open("cocytus-overlord-crossdress-horns-demiurge-overlord-wallpaper-preview.jpg")
photo = ImageTk.PhotoImage(image)

image_label = Label(image = photo)
image_label.pack()

root.mainloop() 