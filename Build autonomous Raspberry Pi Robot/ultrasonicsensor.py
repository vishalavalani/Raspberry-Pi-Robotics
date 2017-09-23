import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 18
ECHO = 22

print "Distance Measurement In Progress"

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(2)

def ReadSensorReading():
    GPIO.output(TRIG, False)  # Set TRIG as LOWd
    time.sleep(0.1)  # Delay

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return  distance

try:
    while (True):
        distanceincm = ReadSensorReading()
        print str(distanceincm) + " cm"

finally:
    print("Cleaning Up!")
    GPIO.cleanup()
