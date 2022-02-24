from machine import Pin
import utime
from servoPico import ServoMotor

ir_sensor_l = Pin(9, Pin.IN)
ir_sensor_r = Pin(0, Pin.IN)
sm_l = ServoMotor(start_pos=180, sm_pin=17)
sm_r = ServoMotor(start_pos=0, sm_pin=15)

while True:
    #print(ir_sensor.value())
    if ir_sensor_l.value() == 1:
        sm_l.rotate(0)
    elif ir_sensor_l.value() == 0:
        sm_l.rotate(130)
        
        
    if ir_sensor_r.value() == 1:
        sm_r.rotate(130)
    elif ir_sensor_r.value() == 0:
        sm_r.rotate(0)