from flask import Flask, request, json
import serial
import os
import time


# https://www.electronicwings.com/raspberry-pi/raspberry-pi-uart-communication-using-python-and-c

if os.path.exists('/dev/ttyACM0'):
    ser = serial.Serial(f"/dev/ttyACM0", 2000000)    # ls -l /dev | grep serial to get tty*  115200
elif os.path.exists('/dev/ttyACM1'):
    ser = serial.Serial(f"/dev/ttyACM1", 2000000)
else:
    raise Exception("no /dev/ttyACM0 or /dev/ttyACM1")

api = Flask(__name__)

ser.reset_input_buffer()
ser.reset_output_buffer()


cube_buffer = bytearray(381)


def convert_color(scaler: int) -> int:
    # 0 off, 1 to 15, 15 mostly off, 1 mostly on
    if scaler == 0:
        return 0
    else:
        return int((255 - scaler) / 18) + 1


@api.route('/cube', methods=['POST'])
def send_cube_data():
    content = request.json
    cube = content['cube']

    print('writing cube to arduino')

    total_frames = len(cube['frames'])

    for frame_idx, frame in enumerate(cube['frames']):
        cycle_bytes = int(frame['cycles']).to_bytes(4, 'big')
        cube_buffer[0] = frame_idx
        cube_buffer[1] = total_frames
        matrix = frame['matrix']

        for i in range(4):
            cube_buffer[i+2] = cycle_bytes[i]

        for zi in range(5):
            for xi in range(5):
                for yi in range(5):
                    buff_i = (zi * 25) + (xi * 5) + yi + 6
                    voxel = matrix[zi][xi][yi]
                    cube_buffer[buff_i] = convert_color(voxel['r'])
                    cube_buffer[buff_i + 125] = convert_color(voxel['g'])
                    cube_buffer[buff_i + 250] = convert_color(voxel['b'])

        ser.write(cube_buffer)
        ser.flush()
        # print(f"written [{cube_buffer}]")
        print(f"written ")
        while ser.out_waiting > 0:
            print("waiting for buffer")

    return json.dumps({"success": True}), 201


@api.route('/hello', methods=['GET'])
def say_hello():
    return json.dumps({"Hello World": True}), 200


if __name__ == '__main__':
    print("starting server on port 3000")
    api.run(port=3000)