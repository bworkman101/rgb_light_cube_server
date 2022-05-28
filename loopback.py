import serial
import time


with serial.Serial('/dev/ttyS0', 115200) as ser:
    print("started")

    ser.reset_input_buffer()
    ser.reset_output_buffer()

    ser.write(bytes([69]))
    # ser.flush()
    time.sleep(5)
    print("bytes sent")

    while True:
        if ser.in_waiting > 0:
            b_read = ser.read(1)
            print(f"read [{b_read}]")
