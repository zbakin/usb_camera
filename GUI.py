from tkinter import *

def doNothing():
    print("okok i wont")

root = Tk() #blink window

# ***** Main Menu *******

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File",menu=subMenu) #drop down menu

subMenu.add_command(label="New Project...", command=doNothing) # one item in the drop down menu
subMenu.add_command(label="New... ", command=doNothing)
subMenu.add_separator()#adds like between 2 commands
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Redo",command=doNothing)

# ***** Toolbar*******

toolbar = Frame(root, bg = "blue")
insertButt = Button(toolbar, text="Insert Image", command = doNothing)
insertButt.pack(side=LEFT, padx=2,pady=2)
printButt = Button(toolbar, text="Print", command = doNothing)
printButt.pack(side=LEFT, padx=2,pady=2)

toolbar.pack(side=TOP, fill = X)


# ***** Status Bar *******

status = Label(root, text="Preparing to do nothing...",bd=1,relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop() # keep displaying stuff continiously
