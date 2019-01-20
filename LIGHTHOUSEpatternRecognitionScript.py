#from lib import lib
import serial
import numpy
import matplotlib.pyplot

ser = serial.Serial('COM7', 9600)
x=[]
time=[]
dataSize=0
while (dataSize<200):
    y=ser.readline()[:-2]
    y=int(y)
    print(y)
    x.append(y)
    time.append(dataSize)
    dataSize+=1


signal=numpy.array(x)
time=numpy.array(time)
"""
matplotlib.pyplot.plot(time, signal) 
matplotlib.pyplot.show()
"""


#Feature 1: 
#takes in indices array and filtered signal; 
#outputs amplitude for at each index, giving height of each peak. 

def findFeature1(signal, time):
    feature1=numpy.empty([dataSize])

    for i in range(dataSize):
        feature1[i] = (signal[i])
    
    return feature1

#Feature 2:
   

        
def findFeature2(signal, time):
    feature2=numpy.empty([dataSize])
    for i in range(dataSize):
        
        feature2[i]=(signal[i]+signal[i-1]) 
        #slope should ideally be divided by change in x (i.e. 100 data or 0.27s).
        #However, as this would be the constant denominator for all peaks, the slope for
        #each peak relative to other peaks is the same. I.e. dividng by change in x is
        #unnecessary for separating the data
        
        #Please note that this is also not the exact slope, as the data along the rising
        #edge of the spike is not a perfect line and prone to fluctuation. This is really the
        #secant average between the peak and 100 points prior to estimate the slope. 
            

    return feature2
            



feature1=findFeature1(signal, time)
feature2=findFeature2(signal, time)
             

#c)

                                  
for i in range(dataSize):
    if feature1[i]>0 and feature2[i]>0:
        matplotlib.pyplot.plot(feature1[i], feature2[i], 'rs')
    else:
        matplotlib.pyplot.plot(feature1[i], feature2[i], 'bs')

    

matplotlib.pyplot.xlabel('Feature 1 (amplitude)')
matplotlib.pyplot.ylabel('Feature 2 (slope of rising edge)')
matplotlib.pyplot.show()