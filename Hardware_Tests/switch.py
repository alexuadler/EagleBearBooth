import RPi.GPIO as GPIO
import time
from PIL import Image
import subprocess
from subprocess import call
import commands

def capture_image():
    call ("gphoto2 " +
          "--capture-image-and-download " +
	  "--filename=%Y%m%d_%H%M%S.%C",
          shell=True)

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        capture_image()
        time.sleep(0.2)
