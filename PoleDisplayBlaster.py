#PoleDisplayBlaster.py
#Forrest Erickson
#11 Oct, 2017.
# GUI developed with ideas from Object Orented crash course from: https://www.youtube.com/watch?v=A0gaXfM1UN0&t=38s
#TTK introduced at: https://www.youtube.com/watch?v=oV68QJJUXTU


from datetime import datetime #So we can use datetime.now()

import tkinter as tk
from tkinter import ttk
import string

VERSION = "1.0.0"
SMALL_FONT=("Verdana", 10)
LARGE_FONT=("Verdana", 12)
XLARGE_FONT=("Verdana", 18)

ICONFILENAME = "PoleDisplay.ico"

def blastText(theText):
    print("Blasting text:\n", end='')
    print(theText)

def blastTime():
    stringTime=("Now it is: " + str(datetime.now()))
    print("Blasting text:\n", end='')
    print(stringTime)
    
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
        self.T.insert(tk.END, "Just a text Widget\nin two lines\n")
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
        
        button3 = ttk.Button(self, text="Setup Page",        
                            command=lambda: controller.show_frame(SetupPage))       
        button3.pack()
        
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


app = PoleDisplayBlaster()
app.mainloop()

        
        
