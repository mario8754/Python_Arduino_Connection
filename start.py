# Importing Libraries
import serial
import time
ser = serial.Serial(port='/dev/tty.usbmodem141401',
                    baudrate=9600, timeout=.1)


def led_on_off():
    user_input = input("\n Type on / off / servo /quit : ")
    if user_input == "on":
        print("LED is on...")
        time.sleep(0.1)
        ser.write(b'H')
        led_on_off()
    elif user_input == "off":
        print("LED is off...")
        time.sleep(0.1)
        ser.write(b'L')
        led_on_off()
    elif user_input == "open":
        print("Controling servo")
        time.sleep(0.1)
        ser.write(b'W')
        ser.read
    elif user_input == "close":
        print("Controling servo")
        time.sleep(0.1)
        ser.write(b'V')
        ser.read
        led_on_off()
    elif user_input == "sensor":
        print("Controling servo")
        time.sleep(0.1)
        ser.write(b'S')
        ser.read
        led_on_off()
    elif user_input == "quit" or user_input == "q":
        print("Program Exiting")
        time.sleep(0.1)
        ser.write(b'L')
        ser.read
        led_on_off()
    else:
        print("Invalid input. Type on / off / quit.")
        led_on_off()


time.sleep(2)  # wait for the serial connection to initialize

led_on_off()

# Serial read section
