from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import numpy as np
import gpiozero

class Arm:

    factory = PiGPIOFactory()

    pivot = Servo(26, pin_factory=factory)
    shoulder = Servo(19, pin_factory=factory)
    elbow = Servo(13, pin_factory=factory)
    wrist = Servo(6, pin_factory=factory)
    hand = Servo(5, pin_factory=factory)
    fingers = Servo(11, pin_factory=factory)

    servos = {0:pivot, 1:shoulder, 2:elbow, 3:wrist, 4:hand, 5:fingers}

    pos = np.array([0, 0, 0])

    angles = [0, -1, -1, 0, 0, 0]

    def __init__(self):
        pass
        
    def runServo(self, servo: Servo, value: float):
        servo.value = value

    def setPosition(self, x, y, z):
        self.pos[0] = x
        self.pos[1] = y
        self.pos[2] = z

    def valToAngle(self, index: int, val: float) -> int:
        pass
    
    def calcThetas(self):
        pass

    def elbowMax(self, shoulderAngle:float) -> float:
        if shoulderAngle >= 0.8: return -1
        shoulderAngle *= -1.1
        shoulderAngle -= 0.2
        return shoulderAngle

    def update(self):

        #maxes out shoulder angle at 0.8
        if self.angles[1] > 0.8:
            self.angles[1] = 0.8

        #make sure that elbow doesn't go out of range for given shoulder angle
        if self.angles[2] > self.elbowMax(self.angles[1]):
                self.angles[2] = self.elbowMax(self.angles[1])

        #set the servos to their angle
        for servo in self.servos:
            #clamp servo input between -1 and 1
            if self.angles[servo] > 1.0: self.angles[servo] = 1.0    
            if self.angles[servo] < -1.0: self.angles[servo] = -1.0

            self.runServo(self.servos.get(servo), self.angles[servo])

    def kill(self):
        self.factory.close()
     
