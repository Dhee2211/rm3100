import RPI.GPIO as GPIO 
import sys
STATUS = False
#Intializing I2CEN pin raspberry pi 
I2CEN_PIN = 21 #Should be low when using SPI and High when I2C
SSN_OR_SA_PIN = 20 #Should be low prior to read the message.
DRDY_PIN = 16 # Status pin high when the data is ready 

def gpio_initialization():
    'Program to initalize Respberry Pi pins'
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(I2CEN_PIN, GPIO.OUT)
        GPIO.setup(SSN_OR_SA_PIN, GPIO.OUT)
        GPIO.setup(DRDY_PIN, GPIO.IN)
        return True
    except:
        print("Unexpected Error:", sys.exc_info())
        return False

def gpio_setup():
    GPIO.setup(I2CEN_PIN, GPIO.LOW)
    GPIO.setup(SSN_OR_SA_PIN, GPIO.LOW)
    #GPIO.setup(DRDY_PIN, GPIO.IN)
