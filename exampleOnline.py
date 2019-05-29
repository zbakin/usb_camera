from tkinter import *
from tkinter import ttk
import serial
import time

def disp():
    ser = serial.Serial('COM12', baudrate = 9600, timeout=1)
    time.sleep(1)
    arduinoData = (ser.readline().strip())
    a=arduinoData.decode('utf-8')
    dispe.delete(0,"end")
    dispe.insert(0, a)

def dis(event):
    disp()

root=Tk()
button=Button(root,text="press")
button.bind("<Button-1>",dis)
button.pack(side=LEFT)
dispe=Entry(root)
dispe.pack(side=LEFT)
root.mainloop()
