from tkinter import *
from tkinter import ttk, font
# from PIL import ImageTk, Image
# from MCP3008 import MCP3008
from time import sleep
import serial
import random


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
        self.PercentageFont = font.Font(family='Courier', size=30)
        

        self.SolarFlag = False
        self.WindFlag = False
        
        self.FullBatteryImage = PhotoImage(file='./battery/full.png').subsample(6)
        self.MediumBatteryImage = PhotoImage(file='./battery/medium.png').subsample(6)
        self.LowBatteryImage = PhotoImage(file='./battery/low.png').subsample(6)
        self.ChargingBatteryImage = PhotoImage(file='./battery/charging.png').subsample(6)
        self.SolarEnergyImage = PhotoImage(file='./battery/solar-energy.png').subsample(6)



        self.BatteryPercentage = ttk.Button(self.rootFrame, image=self.FullBatteryImage, command=self.Voltage)
        self.BatteryPercentage.grid(column=2, row=0, pady=10)
        self.BatteryStatus = StringVar(self.rootFrame, '50%')
        self.BatteryLabel = ttk.Label(self.rootFrame, textvariable=self.BatteryStatus, font=self.PercentageFont).place(x=630, y=40)

        self.SolarPower = ttk.Button(self.rootFrame, image=self.SolarEnergyImage, command=self.Power)
        self.SolarPower.grid(column=1, row=0, pady=10)
        self.SolarPowerStatus = StringVar(self.rootFrame, '200W')
        self.SolarPowerLabel = ttk.Label(self.rootFrame, textvariable=self.SolarPowerStatus, font=self.PercentageFont).place(x=250, y=40)



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


        # self.root.after(3000, self.VoltageReading)

        # self.VoltageReading()
        self.root.mainloop()


    def SolarSwitch(self):
        if self.SolarFlag:
            self.SolarFlag = False
            self.WindFlag = False
            self.Voltage()
            self.Power()
            self.SolarStatus.set('Solar System: OFF')
        else:
            self.SolarFlag = True
            self.WindFlag = False
            self.Power()
            self.SolarStatus.set('Solar System: On')
            self.WindStatus.set('Wind System: OFF')
            self.BatteryStatus.set('')
            # self.BatteryStatus.set('Charging')
            self.BatteryPercentage.config(image=self.ChargingBatteryImage)
            




    def WindSwitch(self):
        if self.WindFlag:
            self.WindFlag = False
            self.SolarFlag = False
            self.Voltage()
            self.Power()
            self.WindStatus.set('Wind System: OFF')
        else:
            self.WindFlag = True
            self.SolarFlag = False
            self.Power()
            self.WindStatus.set('Wind System: On')
            self.SolarStatus.set('Solar System: OFF')
            self.BatteryStatus.set('')
            # self.BatteryStatus.set('Charging')
            self.BatteryPercentage.config(image=self.ChargingBatteryImage)
            
 
            
    # def VoltageReading(self):
           
    #     VoltageValue = 12.00    
    #     # ser = serial.Serial('/dev/ttyACM0',9600)
    #     # x=0
    #     self.Voltage(VoltageValue)
    #     # self.root.after(3000, self.VoltageReading)

    #     # while x<2:

    #     #         # read_serial=ser.readline()
    #     #         # self.VoltageOutput(self, read_serial)
    #     # self.Voltage(VoltageValue)


            
    def Voltage(self):
    
        VoltageValue = random.uniform(11.00, 12.75)

        
        if (VoltageValue <= 11.51):
            self.BatteryStatus.set('10%')
            self.BatteryPercentage.config(image=self.LowBatteryImage)
            
        elif (VoltageValue <= 11.66 and VoltageValue > 11.51):
            self.BatteryStatus.set('20%')
            self.BatteryPercentage.config(image=self.LowBatteryImage)

        elif (VoltageValue <= 11.81 and VoltageValue > 11.66):
            self.BatteryStatus.set('30%')
            self.BatteryPercentage.config(image=self.LowBatteryImage)
            
        elif (VoltageValue <= 11.96 and VoltageValue > 11.81):
            self.BatteryStatus.set('40%')
            self.BatteryPercentage.config(image=self.MediumBatteryImage)
            
        elif (VoltageValue <= 12.10 and VoltageValue > 11.96):
            self.BatteryStatus.set('50%')
            self.BatteryPercentage.config(image=self.MediumBatteryImage)
            
        elif (VoltageValue <= 12.24 and VoltageValue > 12.10):
            self.BatteryStatus.set('60%')
            self.BatteryPercentage.config(image=self.MediumBatteryImage)
            
        elif (VoltageValue <= 12.37 and VoltageValue > 12.24):
            self.BatteryStatus.set('70%')
            self.BatteryPercentage.config(image=self.MediumBatteryImage)
            
        elif (VoltageValue <= 12.50 and VoltageValue > 12.37):
            self.BatteryStatus.set('80%')
            self.BatteryPercentage.config(image=self.FullBatteryImage)
            
        elif (VoltageValue <= 12.62 and VoltageValue > 12.50):
            self.BatteryStatus.set('90%')
            self.BatteryPercentage.config(image=self.FullBatteryImage)
            
        elif (VoltageValue <= 12.73 and VoltageValue > 12.62):
            self.BatteryStatus.set('100%')
            self.BatteryPercentage.config(image=self.FullBatteryImage)
        
    def Power(self):
        
        PowerValue = random.randint(100, 400)
        self.SolarPowerStatus.set(str(PowerValue) + 'W')


App = Grid()
# App.VoltageReading()













