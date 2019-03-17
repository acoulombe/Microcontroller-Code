import serial
import matplotlib.pyplot as plt
from drawnow import *
import atexit

ADCconv = 1024
Vmax    = 5

values = []

plt.ion()

MCU = serial.Serial('COM4', 115200)

def plotValues():
    plt.title('Arduino Oscilloscope Samples')
    plt.grid(True)
    plt.ylabel('Voltages')
    plt.plot(values, 'rx-', label='Voltages')
    plt.legend(loc='upper right')

def doAtExit():
    MCU.close()
    plt.close()

atexit.register(doAtExit)

#pre-load dummy data
for i in range(0,250):
    values.append(0)
    
while True:
    while (MCU.inWaiting()==0):
        pass
    msg = MCU.readline()

    #check if valid value can be casted
    try:
        valueInInt = int(msg)
        print(valueInInt)
        if valueInInt <= 1024:
            if valueInInt >= 0:
                voltage = valueInInt/ADCconv*Vmax
                values.append(voltage)
                values.pop(0)
                drawnow(plotValues)
    except ValueError:
        print("Cannot cast to int")
