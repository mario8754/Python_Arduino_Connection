# Importing Libraries
import serial
import time
from tkinter import *
ser = serial.Serial(port='COM3',
                    baudrate=9600, timeout=.1)


def led_On():
    time.sleep(0.1)
    ser.write(b"A")
    print("LED is on...")


def led_off():
    time.sleep(0.1)
    ser.write(b"B")
    print("LED is off...")


window = Tk()


window.title("Arduino app")  # Title of the app

window.geometry("350x200")  # Widht and height

lbl = Label(window, text="Lamp 1")  # Text Button
lbl.grid(column=0, row=0)


btn = Button(window, text="Aan", bg="green", padx=5, command=led_On)

btn.grid(
    column=1,
    row=0,
)

btn1 = Button(window, text="uit", padx=5, command=led_off)  # The button
btn1.grid(column=3, row=0)  # Where button needs to be


window.mainloop()
