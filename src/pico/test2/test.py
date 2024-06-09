import machine
import time
import ENS160

i2c = machine.I2C(0, scl=machine.Pin(17), sda=machine.Pin(16))
print(i2c.scan())

# set up ENS160
sensor = ENS160.ENS160(i2c)

def loop() -> None:

    print("Putting sensor in operating mode 2 (sensing)...")
    sensor.operating_mode = 2
    print("Sensor now in operating mode 2. Waiting 10 seconds for warm up before proceeding...")
    time.sleep(10)

    start_at:int = time.ticks_ms()
    failures:int = 0
    print("Now entering loop!")
    while True:

        # read
        aqi = sensor.AQI # a dict
        tvoc = sensor.TVOC
        eco2 = sensor.ECO2

        # handle
        if aqi["value"] == 0: # invalid
            print("Failure on last read attempt!")
            failures = failures + 1
            sensor.operating_mode = 2
            print("Op Mode restored to 2. Waiting 10 seconds before proceeding...")
            time.sleep(10)
        else:
            print("Data collected successfully - AQI: " + str(aqi) + ", TVOC: " + str(tvoc) + ", ECO2: " + str(eco2))

            # calcualte error rate
            seconds_elapsed:float = (time.ticks_ms() - start_at) / 1000
            minutes_elapsed:float = seconds_elapsed / 60
            hours_elapsed:float = minutes_elapsed / 60
            if hours_elapsed > 0:
                failures_per_hour:float = failures / hours_elapsed
            else:
                failures_per_hour = 9999999

            print("\t" + str(failures) + " failures in " + str(int(round(minutes_elapsed, 0))) + " minutes, averaging " + str(round(failures_per_hour,1)) + " failures per hour")

        # sleep 
        time.sleep(1)