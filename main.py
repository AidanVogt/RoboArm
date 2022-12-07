import Arm
import time
#import test

arm = Arm.Arm()



while(1):
    arm.update()

    try:
        index = int(input("index: "))
        arm.angles[index] #test for out of bound index before asking for next input
        arm.angles[index] = float(input("value: "))
    except(IndexError, ValueError):
        print('invalid input')
