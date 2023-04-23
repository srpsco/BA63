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

region = bytes("\033R00", "utf-8")  #Set region to USA (Standard ASCII)
ser.write(region)


cls = bytes("\033[2J", "utf-8") #send escape sequence to clear screen
ser.write(cls)

line1 = bytes("\033[1;1H", "utf-8") #Escape seqence to start on line 1 char 1
line2 = bytes("\033[2;1H", "utf-8") #Escape seqence to start on line 2 char 1

#splash screen
#string1 = bytes("~~~~~~Les' Lab~~~~~~", "utf-8")
#ser.write(line1+string1)
string2 = bytes("~Raspberry Pi Clock~", "utf-8")
ser.write(line1+string2)
time.sleep(3)

ser.write(cls)

#clock and spinner!
spinner = bytes('|/-\|/-', "utf-8")
spin = 0

while True:
	now = datetime.now()
	now = now.strftime("%Y/%m/%d %H:%M:%S")
	line2txt = line1+(bytes(now, "utf-8"))
	line2bytes = line2txt
	ser.write(line2txt)
	#ser.write(bytes(line1+now+spinner[spin]), "utf-8")
	time.sleep(0.001)

	unixtime = str(round(time.time(),1))
	padding = bytes("    ", "utf-8")
	line2txt = line2+padding+bytes(unixtime, "utf-8")
	ser.write(line2txt)
#	ser.write(line2+bytes("    "+unixtime), "utf-8" )
#	degree = chr(176)
#	ser.write(line2+ str(80) + chr(248) + "F")

	spin+=1
	if spin > len(spinner)-1:
		spin = 0

ser.close
