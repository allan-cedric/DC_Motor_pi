import RPi.GPIO as GPIO
import time
from DC_Motor_pi import DC_Motor

# pins setup
clockwise_pin = 0
counterclockwise_pin = 0
pwm_pin = 0

motor = DC_Motor(clockwise_pin, counterclockwise_pin, pwm_pin)

try:
    while True:
        motor.forward(100)
        time.sleep(3)

        motor.stop()
        time.sleep(3)

        motor.backwards(100)
        time.sleep(3)

        motor.stop()
        time.sleep(3)
except:
    del motor
    GPIO.cleanup()