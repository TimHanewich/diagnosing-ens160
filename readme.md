# ENS160 working perfectly on Raspberry Pi 3 but returns 0's on Raspberry Pi Pico
I posted about this problem:
- [In the /raspberrypipico subreddit](https://www.reddit.com/r/raspberrypipico/comments/1dckzoc/i2c_sensor_returning_0s_on_pico_but_works/)
- [In the /MicroPythonDev subreddit](https://www.reddit.com/r/MicroPythonDev/comments/1dckzmt/i2c_sensor_returning_0s_on_pico_but_works/)
- [On the Raspberry Pi Stack Exchange](https://raspberrypi.stackexchange.com/questions/148230/i2c-sensor-returning-0s-on-pico-but-works-perfectly-on-rpi-3)

I was not able to get any meaningful solutions.

## Known Observables
- After proving a sensor works on a Raspberry Pi 3, it works for a period of time on the Raspberry Pi Pico. Usually between 10 seconds and 5 minutes. Usually about 1 minute or less.
- After immediately moving a sensor from a Raspberry Pi 3 (where it worked) to the Pico, the readings on the Pico will be stable. Then, they go to their bare minimums (AQI of 1, TVOC of 0, ECO2 of 400) and the sensor grows increasingly insensitive. Then, readings stop altogether.
- Oftentimes me breathing on it will trigger the readings to stop altogether. 
- A brand-new sensor seems to work well. For quite some time as well, oftentimes days! The ones I have used for a while have little endurance and fail right away.
- Pull-up resistors seem to have no effect. I've tried everything between 10k ohms to 220 ohms, no result.
- The issue occurs on both 5V and 3.3V power.
- I've tried extenral power source. No luck.
- I've tried a range of I2C clock speeds. 50,000 to 400,000 Hz. No luck.
- I've tried numerous buses and pins on the pico. All the same result.
- I've emulated every I2C read and write that happens on the RPi3 on the Pico. No luck.
- I've tried both VBUS and VSYS on the Raspberry Pi Pico. Same results.

## Observation of RPi 3's interfacing with the sensor (RPi 3 gets it to work perfectly)
At init:
```
Read 2 byte(s) from register 0x0 at address 0x53: 96,1
Writing 1 byte(s) to register 0x10 at address 0x53: 2
Read 1 byte(s) from register 0x10 at address 0x53: 2
Writing 1 byte(s) to register 0x11 at address 0x53: 0
Writing 2 byte(s) to register 0x13 at address 0x53: 137,74
Writing 2 byte(s) to register 0x15 at address 0x53: 0,100
```

At read TVOC:
```
Read 1 byte(s) from register 0x20 at address 0x53: 131
Read 6 byte(s) from register 0x20 at address 0x53: 129,2,174,0,148,2
```

At read AQI: 
```
Read 1 byte(s) from register 0x20 at address 0x53: 131
Read 6 byte(s) from register 0x20 at address 0x53: 129,2,176,0,151,2
```

At read ECO2:
```
Read 1 byte(s) from register 0x20 at address 0x53: 131
Read 6 byte(s) from register 0x20 at address 0x53: 129,2,176,0,150,2
```

## Seems to work on Raspberry Pi 3
On June 8, 2024, I had an ENS160 sensor that was NOT working at all on a Raspberry Pi Pico. I plugged it into a Raspberry Pi 3, it started working perfectly right away.

What I saw when using it for the first time, running `main.py` on commit `c6634ce58400f9b807fe5c89328a88f866316022`:
```
Init sequence: reading part ID
Read 2 byte(s) from register 0x0 at address 0x53: 96,1
Init sequence: part ID was correct!
Init sequence: Turning on operating mode
Writing 1 byte(s) to register 0x10 at address 0x53: 2
Init sequence: Reading back op mode...
Read 1 byte(s) from register 0x10 at address 0x53: 2
Writing 1 byte(s) to register 0x11 at address 0x53: 0
Writing 2 byte(s) to register 0x13 at address 0x53: 137,74
Writing 2 byte(s) to register 0x15 at address 0x53: 0,100
Read 1 byte(s) from register 0x20 at address 0x53: 3
Read 6 byte(s) from register 0x20 at address 0x53: 1,0,0,0,0,0
Read 1 byte(s) from register 0x20 at address 0x53: 1
Read 1 byte(s) from register 0x20 at address 0x53: 1
    AQI: 0 [invalid]
   TVOC: 0 ppb
   eCO2: 0 ppm [invalid]
Read 1 byte(s) from register 0x20 at address 0x53: 1
 Status: operating ok
--------------------------------
Read 1 byte(s) from register 0x20 at address 0x53: 135
Read 6 byte(s) from register 0x20 at address 0x53: 133,1,24,0,144,1
Read 1 byte(s) from register 0x20 at address 0x53: 133
Read 1 byte(s) from register 0x20 at address 0x53: 133
    AQI: 1 [excellent]
   TVOC: 24 ppb
   eCO2: 400 ppm [excellent]
Read 1 byte(s) from register 0x20 at address 0x53: 133
 Status: warm-up
--------------------------------
Read 1 byte(s) from register 0x20 at address 0x53: 133
Read 1 byte(s) from register 0x20 at address 0x53: 133
Read 1 byte(s) from register 0x20 at address 0x53: 133
    AQI: 1 [excellent]
   TVOC: 24 ppb
   eCO2: 400 ppm [excellent]
Read 1 byte(s) from register 0x20 at address 0x53: 133
 Status: warm-up
```

After seeing it work for a few minutes, I then removed it from the Raspberry Pi 3 and then plugged it back in to the Raspberry Pi Pico, ran a test script. Again, didn't work. Same error from before. Bizarre.

Again, I plug it into a Raspberry Pi 3. It works: 

```
Init sequence: reading part ID
Read 2 byte(s) from register 0x0 at address 0x53: 96,1
Init sequence: part ID was correct!
Init sequence: Turning on operating mode
Writing 1 byte(s) to register 0x10 at address 0x53: 2
Init sequence: Reading back op mode...
Read 1 byte(s) from register 0x10 at address 0x53: 2
Writing 1 byte(s) to register 0x11 at address 0x53: 0
Writing 2 byte(s) to register 0x13 at address 0x53: 137,74
Writing 2 byte(s) to register 0x15 at address 0x53: 0,100
Read 1 byte(s) from register 0x20 at address 0x53: 3
Read 6 byte(s) from register 0x20 at address 0x53: 1,0,0,0,0,0
Read 1 byte(s) from register 0x20 at address 0x53: 1
Read 1 byte(s) from register 0x20 at address 0x53: 1
    AQI: 0 [invalid]
   TVOC: 0 ppb
   eCO2: 0 ppm [invalid]
Read 1 byte(s) from register 0x20 at address 0x53: 1
 Status: operating ok
--------------------------------
Read 1 byte(s) from register 0x20 at address 0x53: 135
Read 6 byte(s) from register 0x20 at address 0x53: 133,1,24,0,144,1
Read 1 byte(s) from register 0x20 at address 0x53: 133
Read 1 byte(s) from register 0x20 at address 0x53: 133
    AQI: 1 [excellent]
   TVOC: 24 ppb
   eCO2: 400 ppm [excellent]
Read 1 byte(s) from register 0x20 at address 0x53: 133
 Status: warm-up
--------------------------------
Read 1 byte(s) from register 0x20 at address 0x53: 133
Read 1 byte(s) from register 0x20 at address 0x53: 133
Read 1 byte(s) from register 0x20 at address 0x53: 133
    AQI: 1 [excellent]
   TVOC: 24 ppb
   eCO2: 400 ppm [excellent]
Read 1 byte(s) from register 0x20 at address 0x53: 133
 Status: warm-up
--------------------------------
```

### Recap of what the Raspberry Pi 3 does to get it to work, step by step
I translated the exact I2C reads/writes to MicroPython so we can easily mimick the reads/writes the RPi 3 made on the Pico. Written in MicroPython:

```
# init and loop 1
i2c.readfrom_mem(0x53, 0x00, 2) # reads part ID to validate part
i2c.writeto_mem(0x53, 0x10, bytes([2])) # operating mode 2
i2c.readfrom_mem(0x53, 0x10, 1) # read back operating mode 2.      In a test, I only had to get this far to get it back working again on Raspberry Pi Pico
i2c.writeto_mem(0x53, 0x11, bytes([0])) # CONFIG address (interupt-pin related)
i2c.writeto_mem(0x53, 0x13, bytes([137,74])) # set temperature
i2c.writeto_mem(0x53, 0x15, bytes([0, 100])) # set relative humidity 
i2c.readfrom_mem(0x53, 0x20, 1) # read status
i2c.readfrom_mem(0x53, 0x20, 6) # read data (and other)
i2c.readfrom_mem(0x53, 0x20, 1) # read status
i2c.readfrom_mem(0x53, 0x20, 1) # read status
i2c.readfrom_mem(0x53, 0x20, 1) # read status

# loop 2
i2c.readfrom_mem(0x53, 0x20, 1)
i2c.readfrom_mem(0x53, 0x20, 6) # all data
i2c.readfrom_mem(0x53, 0x20, 1)
i2c.readfrom_mem(0x53, 0x20, 1)
i2c.readfrom_mem(0x53, 0x20, 1)
```

## Monitoring it and observing it turning off
After setting operating mode to 2, waiting a few seconds, and then continuously reading 6 bytes starting at register 0x20, it was working. I had it continuously reading the 6 bytes starting at register 0x20. It was reading data for a few minutes. And then it eventually stopped:

```
b'\x87\x03\x02\x01\xf8\x02'
b'\x87\x03\xf9\x00\xee\x02'
b'\x87\x03\x02\x01\xf9\x02'
b'\x87\x03\x12\x01\t\x03'
b'\x87\x03\xfe\x00\xf4\x02'
b'\x87\x03\xfc\x00\xf2\x02'
b'\x87\x03\x17\x01\x0e\x03'
b'\x87\x03\xf3\x00\xe8\x02'
b'\x87\x03\xdf\x00\xd1\x02'
b'\x87\x03\xfd\x00\xf3\x02'
b'\x87\x03\x15\x01\x0c\x03'
b'\x87\x03\xf9\x00\xef\x02'
b'\x87\x03\xfb\x00\xf1\x02'
b'\x87\x03\xf1\x00\xe5\x02'
b'\x87\x03\x10\x01\x08\x03'
b'\x85\x03\x10\x01\x08\x03'
b'\x87\x03\xed\x00\xe1\x02'
b'\x87\x03\xf3\x00\xe8\x02'
b'\x03\x00\x00\x00\x00\x00'
b'\x01\x00\x00\x00\x00\x00'
b'\x01\x00\x00\x00\x00\x00'
b'\x01\x00\x00\x00\x00\x00'
b'\x01\x00\x00\x00\x00\x00'
b'\x01\x00\x00\x00\x00\x00'
b'\x01\x00\x00\x00\x00\x00'
b'\x01\x00\x00\x00\x00\x00'
b'\x01\x00\x00\x00\x00\x00'
```

## Raspberry Pi Voltage Ratings:
- Pico VSYS: 4.87V
- Pico VBUS: 5.05V
- Raspberyr Pi 3 +5V: __

## Bit Notation
```
Bit 7  Bit 6  Bit 5  Bit 4  Bit 3  Bit 2  Bit 1  Bit 0
1      0      0      0      1      0      1      1
```

This post seems to suggest adding a capacitor might work: https://community.home-assistant.io/t/issue-with-ens160-aht21-ens160-readings-unavailable/697522s
