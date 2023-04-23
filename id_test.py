import time
from datetime import datetime
import serial

ser=serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

cls = bytes("\033[2J", "utf-8") #send escape sequence to clear screen
ser.write(cls)





line1 = bytes("\033[1;1H", "utf-8") #Escape seqence to start on line 1 char 1


#id = line1+bytes("\033[0c", "utf-8")
#region = bytes("\033R00", "utf-8")  #Set region to USA (Standard ASCII)



buffer = [0x00] * 32
buffer[1] = 0x1B
buffer[2] = 0x5B
buffer[3] = 0x30
buffer[4] = 0x63

ser.write(buffer)



#ser.write(line1)

time.sleep(10)
