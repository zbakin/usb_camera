# import libraries for serial port and Tkinter GUI
import os
os.chdir("C:\\Users\\Zhanibek\\Desktop")
import serial
from tkinter import *
 
# Open serial port
s = serial.Serial('COM12', 9600)
 
