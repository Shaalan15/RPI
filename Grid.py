from tkinter import *
from tkinter import ttk, font
from gpiozero import LED
import RPi.GPIO as GPIO



class Grid:
    def __init__(self, GPIO):
        self.root = Tk()
        self.root.title("Portable Grid")
        self.rootFrame = ttk.Frame(self.root, width = 800, height = 480, padding= '10 110')
        self.root.geometry('800x480')
        self.rootFrame.grid(column=0, row=0)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.tk.call("source", "sun-valley.tcl")
        self.root.tk.call("set_theme", "dark")
        self.Font = font.Font(family='Courier', size=22)
        
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        GPIO.setup(32,GPIO.OUT)
        GPIO.setup(40,GPIO.OUT)



        self.led = LED(14)
        self.led2 = LED(15)
        self.led.on()
        self.led2.on()


        self.SolarFlag = False
        self.WindFlag = False

        self.SolarImage = PhotoImage(file='solar-panel.png')
        self.SolarImage = self.SolarImage.subsample(2)
        self.SolarButton = ttk.Button(self.rootFrame, image=self.SolarImage, command = self.SolarSwitch).grid(column=1, row=1,padx=50)

        self.SolarStatus = StringVar(self.rootFrame, 'Solar System: OFF')
        self.SolarLabel = ttk.Label(self.rootFrame, textvariable=self.SolarStatus, font=self.Font).grid(column=1, row=2, pady=20)


        self.WindImage = PhotoImage(file='wind-turbine.png')
        self.WindImage = self.WindImage.subsample(2)
        self.WindButton = ttk.Button(self.rootFrame, image=self.WindImage, command = self.WindSwitch).grid(column=2, row=1, padx=50)
        
        self.WindStatus = StringVar(self.rootFrame, 'Wind System: OFF')
        self.WindLabel = ttk.Label(self.rootFrame, textvariable=self.WindStatus, font=self.Font).grid(column=2, row=2,pady=20)


        GPIO.output(32,GPIO.LOW)
        GPIO.output(40,GPIO.LOW)

        self.root.mainloop()


    def SolarSwitch(self):
        if self.SolarFlag:
            self.SolarFlag = False
            self.WindFlag = False
            GPIO.output(40,GPIO.LOW)
            self.SolarStatus.set('Solar System: OFF')
        else:
            self.SolarFlag = True
            self.WindFlag = False
            GPIO.output(32,GPIO.LOW)
            GPIO.output(40,GPIO.HIGH)
            self.SolarStatus.set('Solar System: On')
            self.WindStatus.set('Wind System: OFF')



    def WindSwitch(self):
        if self.WindFlag:
            self.WindFlag = False
            self.SolarFlag = False
            GPIO.output(32,GPIO.LOW)
            self.WindStatus.set('Wind System: OFF')
        else:
            self.WindFlag = True
            self.SolarFlag = False
            GPIO.output(40,GPIO.LOW)
            GPIO.output(32,GPIO.HIGH)
            self.WindStatus.set('Wind System: On')
            self.SolarStatus.set('Solar System: OFF')


App = Grid(GPIO)

