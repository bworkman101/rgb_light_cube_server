import re
import sys


def to_bytes(red: int, green: int, blue: int) -> bytes:
    return bytes({red}) + bytes({green}) + bytes({blue})

enc = to_bytes(110, 77, 255)
enc2 = to_bytes(55, 0, 145)
enc = enc + enc2
print(enc)
print(enc[0])   
print(enc[1])
print(enc[2])
print(enc[3])   
print(enc[4])
print(enc[5])