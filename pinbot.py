# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

import logging
import time

import RPi.GPIO as GPIO

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger("pinbot")

if __name__ == "__main__":

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(12, GPIO.OUT)

    GPIO.output(12, GPIO.LOW)

    GPIO.output(12, GPIO.HIGH)

    time.sleep(3)

    GPIO.cleanup()

    log.info("All done!")
