from tkinter import *

root = Tk()

root.geometry("744x800")
root.minsize(300,400)
root.maxsize(900,1080)
root.title("My Home automation console")

#important label options
#fg = foreground
#bg = background
#text = add texts to the box
#font = customise fonts
#padx = x padding
#pady = y padding
#relief(border styling) = SUNKEN,RAISED,GROOVE,RIDGE, FLAT,SOLID


txt = Label(text = '''In a fast-paced, highly intense military conflict situation, 
\nBrahMos, encompassing an “across the spectrum” warfare capability in all-weather, 
\nday-and-night conditions, can ensure a clear, decisive outcome in the battlefield...''',
fg = "white", bg = "black", padx = 50, pady = 40, font = "Roboto 10 bold italic",
borderwidth = 5, relief = SUNKEN)

#We can change the position and much more for the above pack
#by using pack options
#anchor = nw,sw,ne,se(directions...north east,south east...etc)
#side = top,bottom,left,right
#fill(for automatically adjusting the pack) = X, Y 
#padx
#pady 

txt.pack(side = TOP, anchor = "se", fill = X)

txt_ready = Label(text = "-------------------- READY----------------------",
fg = "red", font = "ROBOTO 12 bold", borderwidth = 5, relief = RAISED)
txt_ready.pack(anchor = "s", side = BOTTOM, fill = X)

root.mainloop()