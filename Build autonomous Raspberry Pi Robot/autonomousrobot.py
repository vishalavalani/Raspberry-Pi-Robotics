import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

TRIG = 18
ECHO = 22
servo_pin = 40
duty_cycle = 7.5
distance_obstacle = 40

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(servo_pin, GPIO.OUT)

GPIO.output(TRIG, False)
pwm_servo = GPIO.PWM(servo_pin, 50)
pwm_servo.start(duty_cycle)
print "Waiting For Sensor To Settle"
time.sleep(2)

# "Waiting For Sensor To Settle"


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
    return distance


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


def GetSensorReadings():
    pwm_servo.ChangeDutyCycle(13)
    time.sleep(0.1)
    distincmsleft = ReadSensorReading()
    print "distincmsleft " + str(distincmsleft)

    time.sleep(0.1)
    pwm_servo.ChangeDutyCycle(10)
    time.sleep(0.1)
    distincmsleft1 = ReadSensorReading()
    print "distincmsleft1 " + str(distincmsleft1)

    time.sleep(0.1)
    pwm_servo.ChangeDutyCycle(7.5)
    time.sleep(0.1)
    distincmsstraight = ReadSensorReading()
    print "distincmsstraight " + str(distincmsstraight)

    time.sleep(0.1)
    pwm_servo.ChangeDutyCycle(5)
    time.sleep(0.1)
    distincmsright1 = ReadSensorReading()
    print "distincmsright1 " + str(distincmsright1)

    time.sleep(0.1)
    pwm_servo.ChangeDutyCycle(3)
    time.sleep(0.1)
    distincmsright = ReadSensorReading()
    print "distincmsright " + str(distincmsright)
    time.sleep(0.1)
    return distincmsleft, distincmsleft1, distincmsstraight, distincmsright1, distincmsright


try:
    while (True):
        distincmsleft, distincmsleft1, distincmsstraight, distincmsright1, distincmsright = GetSensorReadings()
        if distincmsstraight < distance_obstacle:
            Brake()
            if distincmsleft < distance_obstacle or distincmsleft1 < distance_obstacle:
                Brake()
                for x in range(1, 3, 1):
                    Right()
                    time.sleep(0.1)
                    Brake()
            elif distincmsright < distance_obstacle or distincmsright1 < distance_obstacle:
                Brake()
                for x in range(1, 3, 1):
                    Left()
                    time.sleep(0.1)
                    Brake()
            else:
                Brake()
                for x in range(1, 3, 1):
                    Right()
                    time.sleep(0.1)
                    Brake()
        elif distincmsleft < distance_obstacle or distincmsleft1 < distance_obstacle:
            Brake()
            for x in range(1, 3, 1):
                Right()
                time.sleep(0.1)
                Brake()
        elif distincmsright < distance_obstacle or distincmsright1 < distance_obstacle:
            Brake()
            for x in range(1, 3, 1):
                Left()
                time.sleep(0.1)
                Brake()
        else:
            Forward()
            time.sleep(0.5)
            Brake()
finally:
    pwm_servo.ChangeDutyCycle(7.5)
    Brake()
    print("Cleaning Up!")
    GPIO.cleanup()
