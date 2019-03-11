import gpiozero as gpio
from enums.gpio_device_state import GpioDeviceState


class GpioDevice():
    def __init__(self, device_name, pin):
        self.device_name = device_name
        self.pin = pin #TODO validate if pin in right GPIO pins pool
        self.__device = gpio.LED(pin)
        self.device_state = GpioDeviceState.OFF

    def turn_on(self):
        if self.device_state == GpioDeviceState.OFF:
            self.__device.on()
            return f"turned on device: {self.device_name}"
        else:
            return "device already on!"

    def turn_off(self):
        if self.device_state == GpioDeviceState.ON:
            self.__device.off()
            return f"turned off device: {self.device_name}"
        else:
            return "device already off!"
