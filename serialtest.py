import serial

# Should I add a timeout
ser = serial.Serial("/dev/ttyUSB0")
while 1 == 1:
    string = ser.readline()
    print(string)
#    Read 10 bytes from buffer
