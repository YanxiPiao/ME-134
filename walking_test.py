import time
from adafruit_motor import servo
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685

i2c_bus  = busio.I2C(SCL, SDA)

pca = PCA9685(i2c_bus)

pca.frequency = 50
side = servo.Servo(pca.channels[0])
updown = servo.Servo(pca.channels[3])


side.angle = 0
updown.angle = 0
input()




pca.deinit()

