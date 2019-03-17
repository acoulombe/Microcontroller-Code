import serial # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt #import matplotlib library

arduinoData = serial.Serial('COM5', 115200) #Creating our serial object named arduinoData
cnt=0
 
def plotFig(x, y): #Create a function that makes our desired plot
    plt.plot(x,y)
    plt.axis([0,1000,0,1025])
    plt.show()

    
voltage = []
sample = [] 
while True: # While loop that loops forever
    arduinoData.readline()
    arduinoString = arduinoData.readline() #read the line of text from the serial port
    voltage.append(int(arduinoString))     #Convert first element to integer number and put in voltage list
    cnt=cnt+0.4                            #losing half the data sampled at 0.2ms to properly sync read time
    sample.append(cnt)
    if(cnt>1000):                          #If you make it to 1000ms or more, plot
        plotFig(sample,voltage)
        break
while True:
    pass                                    #wait for user kill
