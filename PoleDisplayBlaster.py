#PoleDisplayBlaster.py
#Forrest Erickson
#11 Oct, 2017.
# GUI developed with ideas from Object Orented crash course from: https://www.youtube.com/watch?v=A0gaXfM1UN0&t=38s
#TTK introduced at: https://www.youtube.com/watch?v=oV68QJJUXTU


from datetime import datetime #So we can use datetime.now()

import tkinter as tk
from tkinter import ttk
import string
import seriallib

VERSION = "1.0.0"
SMALL_FONT=("Verdana", 10)
LARGE_FONT=("Verdana", 12)
XLARGE_FONT=("Verdana", 18)

IEE_CLEAR = b'\x0c'             #ASCII FF
IEE_HIDECURSOR = b'\x0e'
IEE_SHOWCURSOR = b'\x0f'
IEE_NORMALDATAENTERY = b'\x11'
IEE_RESET = b'\x14'
IEE_DISPLAYCLEAR = b'\x15'
IEE_HOME = b'\x16'
IEE_WRAPAROUND = b'\x1a'

ICONFILENAME = "PoleDisplay.ico"

def initSerialPort():
    #Set up serial port
    seriallib.mySerialport() #Create serial port.
    seriallib.myOpenSerialPort() #Open the port.
    

def initPoleDisplay():
    #Set up IEE Pole Display.
    seriallib.myWritechr(IEE_RESET.decode())
    seriallib.myWritechr(IEE_NORMALDATAENTERY.decode())    
#    seriallib.myWritechr(IEE_HIDECURSOR.decode())
#    seriallib.myWritechr(IEE_WRAPAROUND.decode())
    
def cursorHome():
    #Set IEE Pole cursor homw.
    seriallib.myWritechr(IEE_HOME.decode())

    
def blastText(theText):
    #Now to Python Shell
    print("Blasting text:\n", end='')
    print(theText)
    #Now to serial port using myWritechr(c)
    #Clear and Home display 
#    seriallib.myWritechr(IEE_HIDECURSOR.decode())
#    seriallib.myWritechr(IEE_CLEAR.decode())
    seriallib.myWritechr(IEE_CLEAR.decode())    
    seriallib.myWritechr(IEE_HOME.decode())
#    foo = input("Any key to continue")
    for i in range(len(theText)):
        seriallib.myWritechr(theText[i])


def blastTime():
    #Now to Python Shell
#    stringTime=("Now it is: " + str(datetime.now()))
    stringTime = str(datetime.now())
    stringTime = stringTime[:19]
    print("Blasting text:\n", end='')
    print(stringTime)
    #Now to serial port using myWritechr(c)
    #Clear and Home display 
#    seriallib.myWritechr(IEE_HIDECURSOR.decode())
    seriallib.myWritechr(IEE_CLEAR.decode())    
    seriallib.myWritechr(IEE_HOME.decode())   
    for i in range(len(stringTime)):
        seriallib.myWritechr(stringTime[i])
    
#Main application class.
class PoleDisplayBlaster(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default = ICONFILENAME)
        tk.Tk.wm_title(self, "Pole Display Blaster " + VERSION)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight =1)
        container.grid_columnconfigure(0, weight =1)

        self.frames = {}
        #Add to the list in the for loop all the page classes
        for F in (StartPage, PageOne, PageTwo, SetupPage):            
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid( row=0,column=0, sticky="nsew")        
        self.show_frame(StartPage)        
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#Each page is a class.
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Blast it!", font=XLARGE_FONT)
        label.pack(pady=10, padx=10)

        label_2 = tk.Label(self, text="Input Text Here", font=LARGE_FONT)
        label_2.pack(pady=10, padx=10)

        self.T = tk.Text(self, height=2, width=20, bd=10)        
        self.T.insert(tk.END, "Just a text Widget in two lines.")
        self.T.focus_set()
        self.T.pack()
        
        button1 = ttk.Button(self, text="Message Blast Display",
                             command=lambda: blastText(self.T.get("1.0",tk.END+"-1c")))
                                #From: https://stackoverflow.com/questions/34112085/pycharm-end-statement-not-working
                                #The first part, "1.0" means that the input should be
                                #read from line one, character zero (ie: the very first character).
                                #END is an imported constant which is set to the string "end"
                                # The only issue with this is that it actually adds a newline
                                #to our input. So, in order to fix it we should change END to end-1c
                                #(Thanks Bryan Oakley) The -1c deletes 1 character, while -2c
                                #would mean delete two characters, and so on.

        button1.pack()

        button2 = ttk.Button(self, text="Time Blast Display",        
                            command=lambda: blastTime())
#                            command=lambda: controller.show_frame(PageTwo))       
        button2.pack()
        
        button3 = ttk.Button(self, text="Cursor Home",        
                            command=lambda: cursorHome())
        button3.pack()

        button4 = ttk.Button(self, text="Setup Page",        
                            command=lambda: controller.show_frame(SetupPage))       
        button4.pack()
        
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text="Back to Home",        
                            command=lambda: controller.show_frame(StartPage))       
        button1.pack()

        button2 = ttk.Button(self, text="Page Two",        
                            command=lambda: controller.show_frame(PageTwo))       
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text="Back to Home",        
                            command=lambda: controller.show_frame(StartPage))       
        button1.pack()

        button2 = ttk.Button(self, text="Page One",        
                            command=lambda: controller.show_frame(PageOne))       
        button2.pack()
        
class SetupPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label_1 = tk.Label(self, text="Setup Page", font=SMALL_FONT)
        label_1.pack(pady=10, padx=10)

        label_2 = tk.Label(self, text="Now it is: " + str(datetime.now()), font=SMALL_FONT)
        label_2.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text="Back to Home",        
                            command=lambda: controller.show_frame(StartPage))       
        button1.pack()


initSerialPort()
initPoleDisplay()

app = PoleDisplayBlaster()
app.mainloop()

        
        
