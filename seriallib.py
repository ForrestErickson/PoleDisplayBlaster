#!/usr/bin/python
#Seriallib.py
#Lee Erickson
#Copyright 26 August 2017
#Update with USB1 port for USB Display on RPi.

SPLASH = 'Seriallib.py by Lee Erickson, Copyright 25 October 2017\r\n'

def mySerialport():
#class mySerialport():
    import serial, time    #initialization and open the port
    global ser
    ser = serial.Serial()        
#    ser.port = "/dev/ttyUSB0"
#    ser.port = "/dev/ttyUSB1"  #For USB pole display on RPi
#    ser.port = "COM8"
    ser.port = "COM4"
#    ser.port = "COM2"
    ser.baudrate = 9600
    ser.bytesize = serial.EIGHTBITS #number of bits per bytes
    ser.parity = serial.PARITY_NONE #set parity check: no parity
    ser.stopbits = serial.STOPBITS_ONE #number of stop bits
    #ser.timeout = None          #block read
    ser.timeout = 1            #non-block read
    #ser.timeout = 2              #timeout block read
    ser.xonxoff = False     #disable software flow control
    ser.rtscts = False     #disable hardware (RTS/CTS) flow control
    ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
    ser.writeTimeout = 2     #timeout for write
                            #possible timeout values:
                            #    1. None: wait forever, block call
                            #    2. 0: non-blocking mode, return immediately
                            #    3. x, x is bigger than 0, float allowed, timeout block call
    
if __name__ == "__main__":    
#    import serial, time    #initialization and open the port
    import serial    #initialization and open the port
    mySerialport()  #initialization and open the portsd
    print (SPLASH) 
    
def mySetSerialPort(serial_port="COM4"):
    myserial_port = serial_port
    ser.port = myserial_port

def myOpenSerialPort():
    try: 
        ser.open()
    except ser.SerialException:
        print ("error open serial port: " + ser.port )
        exit()

def myCloseSerialPort():
    ser.close()
    
#Read from serial port
def myReadln():
    if ser.isOpen():
        try:
            ser.flushInput() #flush input buffer, discarding all its contents
            ser.flushOutput()#flush output buffer, aborting current output 
                     #and discard all that is in buffer
            response = ser.readline()         
            return(response.decode())   
        except serial.SerialException:
            print ("error communicating...: " + str(e1))
    else:
        print ("cannot open serial port ")

def myReadchr():
    if ser.isOpen():
        try:            
            response = ser.readline(1)
            return(response.decode())
        #except Exception, e1:
        except serial.SerialException:
            print ("error communicating...: " + str(e1))
    else:
        print ("cannot open serial port ")

def myReadbyte():
    if ser.isOpen():
        try:            
            response = ser.readline(1)
            return(response)
        #except Exception, e1:
        except serial.SerialException:
            print ("error communicating...: " + str(e1))
    else:
        print ("cannot open serial port ")

def myWritechr(c):  #A single character.
    my_c = str(c)
    if ser.isOpen():
        try:
#            print("Lets write out serial port a character: " + repr(my_c))
            writeStatus = ser.write(my_c.encode())
            return(True)

        except ser.SerialException:
            print ("error communicating serial write...: " + str(e1))
    else:
        print ("cannot open serial port to write ")

print("End of module seriallib.py")
