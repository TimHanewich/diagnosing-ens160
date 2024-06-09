
## Raw Observation of it working
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

## Reverse-Engineering how it works

### At Init:
- Reads 2 bytes from register `0x00`, validating device identity (96,1 are the correct bytes)
- Writes byte `2` to register `0x10`, turning the operating mode to on (sensing)
- Reads back byte `2` from register `0x10`, validating

## Seems to work on Raspberry Pi 3
On June 8, 2024, I had an ENS160 sensor that was NOT working at all on a Raspberry Pi Pico. I plugged it into a Raspberry Pi 3, it started working throuhg that.

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
Written in MicroPython (you can use this):

```
# loop 1
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




## Bit Notation
```
Bit 7  Bit 6  Bit 5  Bit 4  Bit 3  Bit 2  Bit 1  Bit 0
1      0      0      0      1      0      1      1
```