# Raspberry Pi Pico (MicroPython) tests
- [test1](./test1/) - direct I2C manipulation.
    - After letting this run for 93 minutes, 22 failures were encountered. But, every time it was "rebooted" by setting operating mode to 2, it immediately started returning values. Not sure if these values are "stable" or not though... they may be out of whack after completing resetting (i.e. when you first boot up, the values seem very high).
- [test2](./test2/) - Using ENS160.py class from [here](https://github.com/TimHanewich/MicroPython-Collection/blob/master/ENS160/ENS160.py).