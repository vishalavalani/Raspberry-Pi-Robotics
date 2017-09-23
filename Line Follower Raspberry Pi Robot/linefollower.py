import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

GPIO.setup(31, GPIO.IN)  # Left Line Sensor Reading
GPIO.setup(32, GPIO.IN)  # Right Line Sensor Reading

print "Waiting For Sensor To Settle"
time.sleep(2)



def GetSensorReadings():
    print "Taking sensor readings"
    leftlinesensor = GPIO.input(31)
    rightlinesensor = GPIO.input(32)
    print leftlinesensor
    print rightlinesensor
    return leftlinesensor, rightlinesensor


def Forward():
    GPIO.output(11, 1)
    GPIO.output(13, 0)
    GPIO.output(15, 1)
    GPIO.output(16, 0)


def Reverse():
    GPIO.output(11, 0)
    GPIO.output(13, 1)
    GPIO.output(15, 0)
    GPIO.output(16, 1)


def Right():
    GPIO.output(11, 1)
    GPIO.output(13, 0)
    GPIO.output(15, 0)
    GPIO.output(16, 1)


def Left():
    GPIO.output(11, 0)
    GPIO.output(13, 1)
    GPIO.output(15, 1)
    GPIO.output(16, 0)


def Brake():
    GPIO.output(11, 1)
    GPIO.output(13, 1)
    GPIO.output(15, 1)
    GPIO.output(16, 1)


try:
    while (True):
        rightlinesensor, leftlinesensor = GetSensorReadings()
        if leftlinesensor == 1 and rightlinesensor == 0:
            Brake()
            time.sleep(0.15)
            Right()
            time.sleep(0.15)
        elif rightlinesensor == 1 and leftlinesensor == 0:
            Brake()
            time.sleep(0.15)
            Left()
            time.sleep(0.15)
        else:
            Forward()

finally:
    Brake()
    print("Cleaning Up!")
    GPIO.cleanup()
