#from lib import lib
import serial


ser = serial.Serial('COM7', 9600)
x=[]
dataSize=0
while (1==1):
    y=ser.readline()[:-2]
    y=int(y)
    print(y)
    x.append(y)
    if (((y+x[dataSize]+x[dataSize-1])/3)>=200):
        print(((y+x[dataSize]+x[dataSize-1])/3))
        sms = lib.utils.sms["@1.0.9"]

        result = sms(
            to="6476956470", # (required)
            body="Door has been opened" # (required)
        )

        break;
    dataSize+=1

    


    


#while True:
#    print ser.readline()
"""  
sms = lib.utils.sms["@1.0.9"]

result = sms(
  to="6476274247", # (required)
  body="1st try at combining" # (required)
)

"""
