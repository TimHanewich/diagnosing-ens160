import machine
import time
import ENS160

i2c = machine.I2C(0, scl=machine.Pin(17), sda=machine.Pin(16), freq=50000)
print(i2c.scan())

# set up ENS160
sensor = ENS160.ENS160(i2c)

def loop() -> None:

    print("Putting sensor in operating mode 2 (sensing)...")
    sensor.operating_mode = 2
    print("Sensor now in operating mode 2. Waiting 10 seconds for warm up before proceeding...")
    time.sleep(10)

    print("Now entering loop!")
    while True:

        # read + report
        aqi = sensor.AQI # a dict
        tvoc = sensor.TVOC
        eco2 = sensor.ECO2
        print("AQI: " + str(aqi) + ", TVOC: " + str(tvoc) + ", ECO2: " + str(eco2))

        # sleep 
        time.sleep(5)