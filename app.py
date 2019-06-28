from flask import Flask
from gpio_device.gpio_device import GpioDevice
app = Flask(__name__)

"""
Currently there is only one light device, LED diode connected to GPIO pin 21. This setup
is to be used as MVP version, to be refactored into more devices in next iterations of app.
"""
test_light = GpioDevice('dioda-1', 21)
devices = {
    'dioda-1': test_light
}


#TODO
@app.route('/all_on')
def all_on():
    # turn all available devices on
    pass


#TODO
@app.route('/all_off')
def all_off():
    # turn all available devices off
    pass


@app.route('/on/<str:device_name>', method=['POST'])
def on(device_name):
    # turn device specified by <device_name> on
    try:
        devices[device_name].turn_on()
    except KeyError:
        return "no such device"


@app.route('/off/<str:device_name>', methods=['POST'])
def off(device_name):
    # turn device specified by <device_name> off
    try:
        devices[device_name].turn_off()
    except KeyError:
        return "no such device"


#TODO
@app.route('/available')
def available_devices():
    # return list of available lightning devices
    pass


@app.route('/about')
def about():
    # return device info, gpio devices list and status, all in json file
    pass


if __name__ == '__main__':
    app.run()
