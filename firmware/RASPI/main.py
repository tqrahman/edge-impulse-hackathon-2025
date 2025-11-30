import sys
import serial
import ast
import time

ser = serial.Serial('/dev/serial0', 9600, timeout=2)

for line in sys.stdin:
    if 'http' in line:
        print(line)
    
    open_spots = 0
    if 'label' in line and 'value' in line:
        
        line_items = line.split(' ')
        objs = ast.literal_eval(line_items[2])
        for obj in objs:
            # print(objs)
            if 'open' in line:
                open_spots += 1
        print(open_spots)
        ser.write(f'spots:{open_spots}\n'.encode('utf8'))
        time.sleep(3)

