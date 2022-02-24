from machine import Pin
import utime
from servoPico import ServoMotor

led = Pin(17, Pin.OUT)
ir_sensor = Pin(18, Pin.IN)
sm = ServoMotor()

while True:
    #print(ir_sensor.value())
    if ir_sensor.value() == 1:
        #led.value(1)
        print('off')
        pass
    else:
        print('on')
        pass
        #led.value(0)
    utime.sleep(1)
    
