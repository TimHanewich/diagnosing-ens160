import time
import machine

i2c = machine.I2C(0, scl=machine.Pin(17), sda=machine.Pin(16))
print(i2c.scan())

def loop() -> None:
    
    print("Putting sensor in operating mode 2 (sensing)...")
    i2c.writeto_mem(0x53, 0x10, bytes([2]))
    print("Sensor now in operating mode 2. Waiting 10 seconds for warm up before proceeding...")
    time.sleep(10)

    start_at:int = time.ticks_ms()
    failures:int = 0
    print("Now entering loop!")
    while True:

        # read
        data = i2c.readfrom_mem(0x53, 0x21, 5) # AQI (1 byte), TVOC (2 bytes), ECO2 (2 bytes)

        # handle
        if data[0] == 0 and data[1] == 0 and data[2] == 0 and data[3] == 0 and data[4] == 0:
            print("Failure on last read attempt!")
            failures = failures + 1
            i2c.writeto_mem(0x53, 0x10, bytes([2]))
            print("Op Mode restores to 2. Waiting 10 seconds before proceeding...")
            time.sleep(10)
        else:
            print("Data collected successfully: " + str(data))

            # calcualte error rate
            seconds_elapsed:float = (time.ticks_ms() - start_at) / 1000
            minutes_elapsed:float = seconds_elapsed / 60
            hours_elapsed:float = minutes_elapsed / 60
            if hours_elapsed > 0:
                failures_per_hour:float = failures / hours_elapsed
            else:
                failures_per_hour = 9999999

            print("\t" + str(failures) + " failures in " + str(round(minutes_elapsed, 0)) + " minutes, averaging " + str(failures_per_hour) + " failures per hour")

        # sleep 
        time.sleep(1)
