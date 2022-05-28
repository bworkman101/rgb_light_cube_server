import serial
import time


# with serial.Serial("/dev/ttyS0", 9600) as ser:
with serial.Serial("/dev/ttyACM0", 9600) as ser:

    ser.reset_input_buffer()
    ser.reset_output_buffer()

    print("listening")

    while True:
        if ser.in_waiting > 0:
            print("reading")
            b_read = ser.read()
            print(f"{b_read[0]:b}")
        else:
            print(f"wait 5 seconds waiting=[{ser.in_waiting}]")
            time.sleep(5)


# import wiringpi


# print("setup")
# wiringpi.wiringPiSetup()
# print("open port")
# serial = wiringpi.serialOpen('/dev/ttyS0',9600)
# print("write")
# wiringpi.serialPuts(serial,'hello world!')
