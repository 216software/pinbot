# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

import logging
import time

import RPi.GPIO as GPIO

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger("pinbot.relayfun")

if __name__ == "__main__":

    # This describes the PIN ordering notation.
    GPIO.setmode(GPIO.BCM)

    for pin_number in [2, 3, 4, 17]:

        GPIO.setup(pin_number, GPIO.OUT)
        GPIO.output(pin_number, GPIO.HIGH)
        GPIO.output(pin_number, GPIO.LOW)
        time.sleep(0.2)

    log.debug("Finished loop")

    time.sleep(3)

    GPIO.cleanup()

    log.info("All done!")
