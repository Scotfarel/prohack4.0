import RPi.GPIO as GPIO


def fan_command(pin_voltage, pin=18):
    """
    A function to set the mode and state of a pin in BCM mode.
    Enable and shutdown a fan.

    1. PIN is int (0..26)
    2. VOLTAGE is str ('HIGH'/'LOW')

    #   SIGNAL_WAY is str ('IN'/'OUT')
    Returns nothing.
    """

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    voltage = GPIO.HIGH if pin_voltage == 'HIGH' else GPIO.LOW
    GPIO.output(pin, voltage)


def get_pollution_rate():
    return 15
