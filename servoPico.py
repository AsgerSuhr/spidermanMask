from machine import Pin, PWM
from time import sleep

class ServoMotor():

    def __init__(self, start_pos = 0, sm_pin=21):
        self.pwm = PWM(Pin(sm_pin))
        self.pwm.freq(50)
        self.maxDuty=9000
        self.minDuty=1000
        self.rotate(start_pos)

    #Function to set an angle
    #The position is expected as a parameter
    def setServoCycle(self, position):
        self.pwm.duty_u16(position)
        sleep(0.001)

    def test(self):
        for degree in range(0,180,1)[::-1]:
            self.rotate(degree)
            sleep(0.01)
            #print("increasing -- "+str(degree))       
        for degree in range(0,180,1):
            self.rotate(degree)
            sleep(0.01)
            #print("increasing -- "+str(degree))
            
    def rotate(self, degrees):
        # seems like it can actually only go down to 5 and up to 170
        # and not from 0 - 180
        if degrees > 170:
            degrees = 170
        elif degrees < 5:
            degrees = 5
        #elif degrees == self.current_pos:
        #    return
                
        newDuty=self.minDuty+(self.maxDuty-self.minDuty)*(degrees/180)
        self.setServoCycle(int(newDuty))
        self.current_pos = degrees

if __name__ in '__main__':
    sm = ServoMotor(start_pos = 0,sm_pin=17)
    #sm.test()
    sm.rotate(0)
    sleep(2)
    sm.rotate(130)
    sleep(2)
    sm.rotate(0)