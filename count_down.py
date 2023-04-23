# TODO add shebang

import time
from datetime import datetime
import serial
import socket

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
time.sleep(1.5)

line1 = bytes("\033[1;1H", "utf-8") #Escape seqence to start on line 1 char 1
line2 = bytes("\033[2;1H", "utf-8") #Escape seqence to start on line 2 char 1


def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '  {:02d} Min. {:02d} Sec.     '.format(mins, secs)
        print(timer, end="\r")
        timer_bytes = bytes(timer, "utf-8") 
        ser.write(line2 + timer_bytes)
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')


time_remaining = bytes("  Time Remaining", "utf-8")
ser.write(line1 + time_remaining)

t = 3660 # 70 mins in seconds
countdown(int(t))


'''
def scroll(text):
	mytext = (" " * 20) + text + (" " * 20)
	for character in mytext:
		if len(mytext) >= 20:
			substring = mytext[:20]
			mybytes = bytes(substring, "utf-8")
			ser.write(line1+mybytes)
			mytext =  mytext[2:]
			time.sleep(0.2)

#scroll("The quick brown fox jumped over the lazy dog")
#scroll("The quick brown fox jumped over the lazy dog")

#time.sleep(2)


def blink(text, repitions):
	#get text length
	text_length = len(text)
	if text_length < 20:
		padding = int((20 - text_length)/2)
		mytext = bytes(" " * padding + text, "utf-8")

	for i in range(repitions):
		ser.write(cls)
		time.sleep(0.5)
		ser.write(line1+mytext)
		time.sleep(0.5)

#blink ("WARNING", 4)


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

# mytext = bytes("this text is too long for a single line", "utf-8")
# ser.write(line2+mytext)

hostname = str(socket.gethostname())
hostname.upper()
hostname = hostname + " "
hostname = bytes(hostname.upper(), "utf-8")

ip = get_ip()
ipaddress = bytes(ip, "utf-8")


ser.write(line1 + hostname + ipaddress)

while(1):
    utc = datetime.utcnow()
    utc_string = str(utc)
    #print(utc_string)
    utc = bytes(utc_string, "utf-8")
    #scroll(utc_string)
    ser.write(line2 + utc)
# TODO format the date as month and day and format seconds without extra decimal places
'''





