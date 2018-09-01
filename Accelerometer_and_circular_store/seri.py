import csv

import serial
import time
import numpy

z1baudrate = 115200
z1port = 'COM3'  # set the correct port before run it
b = 0.00
z1serial = serial.Serial(port=z1port, baudrate=z1baudrate)
z1serial.timeout = 2  # set read timeout
# print z1serial  # debug serial.
print(z1serial.is_open)  # True for opened
if z1serial.is_open:
    while True:
        size = z1serial.inWaiting()
        if size:
            data = z1serial.read(size)
            a = data.decode()
            a.split(',')
            if a[7]=='-':
                s=(a[7]+a[8]+a[9]+a[10]+a[11])
                b=float(s)

                print(b)
                c = (a[20]+a[21]+a[22]+a[23]+a[24])
                d = float(c)
                g = 29.0
                if b / g <= -1:
                    print("PROBABLE ACCIDENT")
                    exit(0)
            else:
                s = (a[7]+a[8]+a[9]+a[10])
                b=float(s)
                print(b)
                c = (a[20] + a[21] + a[22] + a[23])
                d = float(c)
                h = 10
                if d/h >=1:
                    print("PROBABLE ACCIDENT")
            print(data)

        else:
            print('no data')
        time.sleep(1)
else:
    print('z1serial not open')
# z1serial.close()  # close z1serial if z1serial is open.
