
#import os
#os.chdir("C:\\Users\\Zhanibek\\Desktop")


from tkinter import *
from tkinter import messagebox

import serial
import time

#start Serial Comms
def connectToCOM():
    try:
        global s
        port = box.get()
        s = serial.Serial(port, 9600,timeout=1)
        time.sleep(1)

        print(s.readline())
        
    except:
        messagebox.showinfo("Error", "Could not connect")
        
    
def isConnected():
    try:
        print(s.is_open)
    except:
        messagebox.showinfo("Error", "Serial port is not initialised")

def close():
    try:
        s.close()
    except:
        messagebox.showinfo("Error", "Serial port is not initialised") 
  
#create GUI
root = Tk()

#Label(root, text="Enter Serial Port").grid(row=2)
text1 = Label(root,text="Enter Serial Port")
text1.pack(side=LEFT)
box = Entry(root)
box.pack(side=LEFT)


button = Button(root,text="Connect",command=connectToCOM)
#button.bind("<Button-1>", d)
button.pack()

buttonCheck = Button(root,text="Check",command=isConnected)
buttonCheck.pack()


buttonClose = Button(root,text="Close Connection",command=close)
buttonClose.pack()

root.mainloop() # keep displaying stuff continiously
