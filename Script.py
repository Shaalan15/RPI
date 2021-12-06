from tkinter import *
from tkinter import ttk, font
from PIL import ImageTk, Image
# from MCP3008 import MCP3008
from time import sleep


class Grid:
    def __init__(self):
        self.root = Tk()
        self.root.title("Portable Grid")
        self.rootFrame = ttk.Frame(self.root, width = 800, height = 480, padding= '10 10')
        self.root.geometry('800x480')
        self.rootFrame.grid(column=0, row=0)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.tk.call("source", "sun-valley.tcl")
        self.root.tk.call("set_theme", "dark")
        self.Font = font.Font(family='Courier', size=28)
        self.PercentageFont = font.Font(family='Courier', size=20)

        self.SolarFlag = False
        self.WindFlag = False
        
        self.FullBatteryImage = PhotoImage(file='./battery/full.png').subsample(6)
        self.MediumBatteryImage = PhotoImage(file='./battery/medium.png').subsample(6)
        self.LowBatteryImage = PhotoImage(file='./battery/low.png').subsample(6)

        self.BatteryPercentage = ttk.Label(self.rootFrame, image=self.FullBatteryImage)
        self.BatteryPercentage.grid(column=2, row=0, pady=10)
        self.BatteryStatus = StringVar(self.rootFrame, 'Battery Percentage: 50%')
        self.BatteryLabel = ttk.Label(self.rootFrame, textvariable=self.BatteryStatus, font=self.PercentageFont).grid(column=1, row=0, pady=10)

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




        self.root.mainloop()


    def SolarSwitch(self):
        if self.SolarFlag:
            self.SolarFlag = False
            self.WindFlag = False
            self.SolarStatus.set('Solar System: OFF')
        else:
            self.SolarFlag = True
            self.WindFlag = False
            self.SolarStatus.set('Solar System: On')
            self.WindStatus.set('Wind System: OFF')



    def WindSwitch(self):
        if self.WindFlag:
            self.WindFlag = False
            self.SolarFlag = False
            self.WindStatus.set('Wind System: OFF')
        else:
            self.WindFlag = True
            self.SolarFlag = False
            self.WindStatus.set('Wind System: On')
            self.SolarStatus.set('Solar System: OFF')
            
            
            
            
    def Voltage(self):
        
        # adc = MCP3008()
        
        while (True):
            # VoltageReading = adc.read( channel = 1 )
            # VoltageValue = (VoltageReading / 1023.0 * 24.2)
            
            VoltageValue = 11.62
            
            if (VoltageValue <= 11.50):
                
                self.BatteryStatus = 'Battery Percentage: 0%'
                self.BatteryImage = PhotoImage(file='./battery/low.png')
                
            elif (VoltageValue <= 11.66 and VoltageValue > 11.51):
                
                self.BatteryStatus = 'Battery Percentage: 20%'
                self.BatteryPercentage.config(image=self.LowBatteryImage)
                # self.BatteryPercentage.image = self.LowBatteryImage

            elif (VoltageValue <= 11.81 and VoltageValue > 11.66):
                self.BatteryStatus = 'Battery Percentage: 30%'
                self.BatteryImage = PhotoImage(file='./battery/medium.png')
            elif (VoltageValue <= 11.96 and VoltageValue > 11.81):
                self.BatteryStatus = 'Battery Percentage: 40%'
                self.BatteryImage = PhotoImage(file='./battery/medium.png')
            elif (VoltageValue <= 12.10 and VoltageValue > 11.96):
                self.BatteryStatus = 'Battery Percentage: 50%'
                self.BatteryImage = PhotoImage(file='./battery/medium.png')
            elif (VoltageValue <= 12.24 and VoltageValue > 12.10):
                self.BatteryStatus = 'Battery Percentage: 60%'
                self.BatteryImage = PhotoImage(file='./battery/medium.png')
            elif (VoltageValue <= 12.37 and VoltageValue > 12.24):
                self.BatteryStatus = 'Battery Percentage: 70%'
                self.BatteryImage = PhotoImage(file='./battery/medium.png')
            elif (VoltageValue <= 12.50 and VoltageValue > 12.37):
                self.BatteryStatus = 'Battery Percentage: 80%'
                self.BatteryImage = PhotoImage(file='./battery/full.png')
            elif (VoltageValue <= 12.62 and VoltageValue > 12.50):
                self.BatteryStatus = 'Battery Percentage: 90%'
                self.BatteryImage = PhotoImage(file='./battery/full.png')
            elif (VoltageValue <= 12.73 and VoltageValue > 12.62):
                self.BatteryStatus = 'Battery Percentage: 100%'
                self.BatteryImage = PhotoImage(file='./battery/full.png')
            
                



App = Grid()
App.Voltage()
