import RPi.GPIO as rpi

rpi.setwarnings(False)
rpi.setmode (rpi.BCM)
rpi.setup(4,rpi.IN) #GPIO 14 -> IR sensor as input

while True:
    if(rpi.input(4)==True): #object is far away
        print('far')
    elif(rpi.input(4)==False): #object is far away
        print('close')