#!/usr/bin/python3

from piclap import *
from gpiozero import LED


class PiController:
    '''Describes the controller methods which are usually used while connected
    to a raspberry pi controller using the module `gpiozero`.
    '''

    def toggleLight(self, pin=24):
        led = LED(pin)
        led.toggle()
        print("Light toggled on pin", pin)

    def lightBlinker(self, pin, times=10):
        led = LED(pin)
        led.blink(n=times)
        print("Light blinks", times, "times on pin", pin)


class Config(Settings):
    '''Describes custom configurations and action methods to be executed based
    on the number of claps detected.
    '''

    def __init__(self):
        super().__init__()
        self.controller = PiController()
        self.chunk_size = 512       # Reduce as power of 2 if pyaudio overflow
        self.interval = 0.5         # Adjust interval between claps
        self.method.value = 10000   # Threshold value adjustment

    def on2Claps(self):
        '''Custom action for 2 claps'''
        led = LED(4)
        led.blink()
        print("Light flashed on pin 4")

    def on3Claps(self):
        '''Custom action from PiController for 3 claps'''
        self.controller.toggleLight(pin=6)

    def on5Claps(self):
        '''Custom action from PiController for 5 claps'''
        self.controller.lightBlinker(pin=5, times=5)


def main():
    config = Config()
    listener = Listener(config)
    listener.start()


if __name__ == '__main__':
    main()