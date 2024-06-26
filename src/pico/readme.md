# Raspberry Pi Pico (MicroPython) tests
- [test1](./test1/) - direct I2C manipulation.
    - After letting this run for 93 minutes, 22 failures were encountered. But, every time it was "rebooted" by setting operating mode to 2, it immediately started returning values. Not sure if these values are "stable" or not though... they may be out of whack after completing resetting (i.e. when you first boot up, the values seem very high).
- [test2](./test2/) - Using ENS160.py class from [here](https://github.com/TimHanewich/MicroPython-Collection/blob/master/ENS160/ENS160.py) (designed this to also confirm the functionality of this helper class)
    - After running this for 25 miutes, 3 failures were encountered. And again, after each failure, after "rebooting" by setting operating mode back to 2 and then waiting 10 seconds, readings again were coming through.
    - After running this for 138 minutes, 25 failures were encountered. Again, setting it back to operating mode 2 and then waiting 10 seconds before reading again worked immediately.
    - This test confirmed that even when the sensor stops working and has to be "rebooted" by putting the sensing mode to 2 again, the values appear t be stable:
        - Example error: https://i.imgur.com/882fhGz.png
        - Example error: https://i.imgur.com/caZDYkT.png
    - In another test that I ran **immediately** after powering-on the pico, it worked as well. The readings were high initially, but values were coming in sure enough.
- [test3](./test3/) - Same as test1 (direct I2C interfacing), but with a 50,000 frequency
    - I learned that the Raspberry Pi 3 uses a 100,000 frequency by default. But if you don't specify it in MicroPython, it defaults to 400,000. This may be an issue. I found some verbiage on this in the datasheet too. Haven't dug too much into it yet.
- [test4](./test4/) - Same as test2 (using ENS160.py driver), but with a 50,000 frequency.
- [test5](./test5/) - Using the driver, but now abandoning "rebooting" by re-selecting operating mode 2. Just continuously read and print!


## Optimistic Signs on June 12, 2024
I set up a test on June 12, 2024 with the following conditions:
- Raspberry Pi Pico, I2C via pins 16 and 17 (bus 0), powered by USB (using Thonny in REPL)
- External powered supplied via a 18650 battery, lifted to 5.13 volts via a MT3608 converter.
- 4.7k Ohm pull up resistors on I2C lines

It ran for over 2 hours without a hiccup at all.

I then tried reproducing this. Wasn't able to get it to work. Maybe I could if I tried again, I don't know.