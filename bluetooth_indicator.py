import RPi.GPIO as GPIO
import subprocess as sp
import atexit

def cleanup():
    print('Cleaning up pins')
    GPIO.cleanup()
    
atexit.register(cleanup)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
while True:
    stdoutdata = sp.getoutput("hcitool con")
    if "" in stdoutdata.split():
        GPIO.output(18, GPIO.HIGH)
    else:
        GPIO.output(18, GPIO.LOW)
    time.sleep(1)
