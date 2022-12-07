import termios, fcntl, sys, os, threading  
import Arm

arm = Arm.Arm()
fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)



def checkInput():
    try:
        while 1:
            arm.update()
            try:
                c = sys.stdin.read(1)
                if c:
                    if c == "a":
                        if arm.angles[0] < 1: arm.angles[0] += 0.1
                    if c == "d":
                        if arm.angles[0] > -1: arm.angles[0] -= 0.1
                    if c == "w":
                        if arm.angles[1] < 1: arm.angles[1] += 0.1
                    if c == "s":
                        if arm.angles[1] > -1: arm.angles[1] -= 0.1
                    if c == "e":
                        if arm.angles[2] < 1: arm.angles[2] += 0.1
                    if c == "q":
                        if arm.angles[2] > -1: arm.angles[2] -= 0.1 


            except IOError: pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

x = threading.Thread(target=checkInput)
x.start()