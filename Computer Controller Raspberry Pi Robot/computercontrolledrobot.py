import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)


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
        direction = raw_input("Enter Direction: ")
        if direction == '8':
            Forward()
            print("Forward")
        elif direction == '2':
            Reverse()
            print("Reverse")
        elif direction == '4':
            print("Left")
            for x in range(1, 3 , 1):
                Left()
                time.sleep(0.1)
            Brake()
        elif direction == '6':
            print("Right")
            for x in range(1, 3 , 1):
                Right()
                time.sleep(0.1)
            Brake()

        elif direction == '5':
            Brake()
            print("Brake")
        else:
            Brake()
            print("Brake")
finally:
    print("Cleaning Up!")
GPIO.cleanup()
