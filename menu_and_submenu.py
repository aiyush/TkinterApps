from tkinter import *
from tqdm import tqdm
from time import *

def myfunc():
    print("Performing the opertation...Please hold.",end = "\n\n\n")
    for i in tqdm(range(50), desc = "Loading Enviornment Variables..."):
        sleep(0.001)
    print("Initialization Complete!",end = "\n\n\n")
    return

root = Tk()

root.geometry("500x400")

# The title of the app at top left corner
root.title("SwitchBoard")

# Creating a main menu bar

# We create a main menu in root
mainmenu = Menu(root)

# Now we create a section in the main menu named "File"
m1 = Menu(mainmenu,tearoff = 0) #Initialising file menu
m1.add_command(label = "New File", command = myfunc) # adding options for this section
m1.add_separator() # We can place it anywhere to draw a line/seperate the options
m1.add_command(label = "Save", command = myfunc)
m1.add_command(label = "Save As", command = myfunc)
m1.add_separator()
m1.add_command(label = "Exit", command = quit)
mainmenu.add_cascade(label = "File",menu = m1) # giving the cascade menu a name.ie. "File"

m2 = Menu(mainmenu,tearoff = 0) #Initialising file menu
m2.add_command(label = "Undo", command = myfunc) # adding options for this section
m2.add_separator() # We can place it anywhere to draw a line/seperate the options
m2.add_command(label = "Copy", command = myfunc)
m2.add_command(label = "Paste", command = myfunc)
m2.add_separator()
m2.add_command(label = "Delete", command = myfunc)
mainmenu.add_cascade(label = "Edit",menu = m2) # giving the cascade menu a name.ie. "File"

root.config(menu = mainmenu)

root.mainloop()